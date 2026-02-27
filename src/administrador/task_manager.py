class taskManager():

    def __init__(self):
        self.tasks = None

    def getTasks(self):
        return  self.tasks
    
    def setTask(self, task):
        self.task = task

    def executeTask(self, usuario):
        self.task.ejecucion(usuario)