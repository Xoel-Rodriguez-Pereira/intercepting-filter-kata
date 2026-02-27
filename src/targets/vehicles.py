from src.targets.target import Target

class Vehicle(Target):

    def __init__(self):
        Target.__init__(self)

    def ejecucucion(self, usuario):
        print('Puerta abierta {0}!'.format(usuario)) 