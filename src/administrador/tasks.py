class Tasks():

    def __init__(self):
        self.tasks = []
        self.target = None


    def getTasks(self):
        return self.tasks
    
    def getTarget(self):
        return self.target
    
    def addTask(self, task):
        self.tasks.append(task)   

    def setTarget(self, target):
        self.tasks = target  


