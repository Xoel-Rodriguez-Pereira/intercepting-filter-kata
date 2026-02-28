from src.clients.client import Client
from src.administrador.task_manager import taskManager

class Mollapp(Client):

    def __init__(self):
        self.administrador = ''

    def setAdministradorTareas(self, administrador):
        self.administrador = administrador

    def enviarPeticion(self, usuario):
        self.administrador.executeTask(usuario)