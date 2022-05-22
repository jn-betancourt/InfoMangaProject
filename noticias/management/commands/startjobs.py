# standar library
import logging

# Django
from django.core.management import BaseCommand
from django.conf import settings


# Third Party
import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution


# Models
from noticias.models import Noticia


login = logging.getLogger(__name__)


def save_new_episodes(feed):

    """
    Recive un feed noticias y
    se asegura que no exista la noticia con su "guid",
    si no existe crea un nuevo objeto "noticia",
    de lo contrario la obvia.

    :arg: feed: requere un feedparser
    """

    noti_title = feed.channel.title
    noti_image = feed.channel.image["href"]

    for item in feed.entries:
        if not Noticia.objects.filter(guid=item.guid).exists():
            noticia = Noticia(
                title=item.title,
                category=item.category,
                pag_title=noti_title,
                description=item.description,
                pub_date=parser.parse(item.published),
                image=noti_image,
                guid=item.guid,
                link=item.link,
            )
            noticia.save()


def fetch_somokudasai_noticia():
    """
    Toma una nueva noticia de su link
    :return: _feed
    """
    _feed = feedparser.parse("https://somoskudasai.com/feed/")
    save_new_episodes(_feed)


def delete_old_job_executions(max_age=172_800):
    """Deletes all the schedulerjob execution logs older tha 'max_age'"""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    """
    Hereda 'BaseCommand',
    contiene el 'handler' con sus respectivos trabajos
    """
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # agrega el trabajo de "fetch_somos_kudasai"
        scheduler.add_job(
            fetch_somokudasai_noticia,
            trigger="interval",
            hours=24,
            id="Somos kudasai",
            max_instances=1,
            replace_existing=True,
        )
        login.info("Added job: Somos kudasai")

        # Agrega un trabajo "delete_old_job" para eliminar viejos trabajos
        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete old jobs",
            max_instances=1,
            replace_existing=True
        )
        login.info("Added weekly job: Delete Old Job Executions")

        try:
            login.info("Starting scheduler....")
            scheduler.start()
        except KeyboardInterrupt:
            login.info("Stoping scheduler")
            scheduler.shutdown()
            login.info("Scheduler shut down succesfuly")
