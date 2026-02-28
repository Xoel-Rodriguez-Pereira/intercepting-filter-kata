from src.administrador.task_manager import TaskManager
from src.clients.mollapp import Mollapp
from src.filters.autentificacion import Autentificacion
from src.filters.autorizacion import Autorizacion
from src.targets.vehicles import Vehicle


def main():
    """
    Configuración del programador de tareas
    del sistema con el tipo de target elegido.
    """
    programador_tasques = TaskManager(Vehicle())

    """
    Añadir al sistema las tareas que queremos
    ejecutar al recibir la petición del cliente.
    """

    programador_tasques.setTask(Autorizacion())
    programador_tasques.setTask(Autentificacion())
    
    """
    Configuración de la app cliente para que
    ejecute las tareas programadas y
    envíe el mensaje al sistema.
    """
    mollapp = Mollapp()
    mollapp.setAdministradorTareas(programador_tasques)
    mollapp.enviarPeticion("Francesc")


if __name__ == "__main__":
    main()
