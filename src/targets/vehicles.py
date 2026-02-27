from src.targets.target import Target

class Vehicle(Target):

    def ejecucion(self, usuario):
        print('Puerta abierta {0}!'.format(usuario)) 

if __name__ == "__main__":
    
    vehicle = Vehicle()
    vehicle.ejecucion("Antonio")