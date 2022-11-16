class Vehiculo:
    def __init__(self, modelo, año, color ):
        self.modelo = modelo
        self.año = año
        self.color = color
                
    def __str__(self):
        return f'Este vehículo modelo: {self.modelo} es del año {self.año} y viene del color {self.color}'
            
    def __repr__(self):
        '''
            _Class Vehículo_
        '''