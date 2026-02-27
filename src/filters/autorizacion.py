from src.filters.filtre import Filtre

class Autorizacion(Filtre):

    def ejecucion(self, usuario):
        print ('Autorización OK para {0}'.format(usuario))

if __name__ == "__main__":
    
    autorizacion = Autorizacion()
    autorizacion.ejecucion("Antonio")