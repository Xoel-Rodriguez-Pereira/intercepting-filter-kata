from src.filters.filtre import Filtre

class Autorizacion(Filtre):

    def ejecucion(self, usuario):
        print ('Autorización OK para {0}'.format(usuario))