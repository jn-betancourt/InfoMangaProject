from InfoMangaProject.noticias.management.commands.startjobs import Command, fetch_somokudasai_noticia
from noticias.management.commands import startjobs

class Inicializador(Command):

    feed = fetch_somokudasai_noticia
    trabajo = startjobs.save_new_episodes

    @classmethod
    def iniciar(cls):
     cls.trabajo(cls.feed)

    Command()

if __name__ == "__main__":

    inicio = Inicializador().iniciar()
