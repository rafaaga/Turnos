class Vehiculos:
    def __init__(self) -> None:
        super().__init__()
        # FIXME convertirlo en diccionario cuya llave sea el id del estudiante y el valor una lista de las evaluaciones que se han hecho para el mismo estudiante
        self.orden = [1,5,4,7,6,3,9,8,2,0,7,4,8,7,5,6]
        self.placas = {1:'VHL234'}

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)