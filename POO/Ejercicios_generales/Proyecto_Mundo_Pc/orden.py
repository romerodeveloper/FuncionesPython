
class Orden:
    contandor_ordenes = 0
    def __init__(self, computadoras):
        Orden.contandor_ordenes += 1
        self._id_orden = Orden.contandor_ordenes
        self._computadoras = computadoras
    
    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)
    
    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__()
        return f'''
        Orden: {self._id_orden}
        Computadoras: {computadoras_str}
        '''
        