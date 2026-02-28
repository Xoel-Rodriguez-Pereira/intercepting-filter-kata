class TaskManager():

    def __init__(self, task):
        self.tasks = [task]

    def getTasks(self):
        return self.tasks
    
    def setTask(self, task):
        self.tasks.insert(0, task)

    def executeTask(self, usuario):
        for task in self.tasks:
            task.ejecucion(usuario)