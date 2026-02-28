from src.clients.client import Client

class Mollapp(Client):
    def __init__(self):
        self.administrador = None
    
    def setAdministradorTareas(self, administrador):
        self.administrador = administrador

    def enviarPeticion(self, usuario):
        self.administrador.executeTask(usuario)