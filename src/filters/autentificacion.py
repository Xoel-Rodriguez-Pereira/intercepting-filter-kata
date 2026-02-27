from src.filters.filtre import Filtre

class Autentificacion(Filtre):

    def ejecucion(self, usuario):
        print ('Autenticación OK para {0}'.format(usuario))