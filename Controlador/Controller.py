class Vehiculos:
    def __init__(self) -> None:
        super().__init__()
        # FIXME convertirlo en diccionario cuya llave sea el id del estudiante y el valor una lista de las evaluaciones que se han hecho para el mismo estudiante
        self.placas = {1:'SJS703',
                       2:'TLA614',
                       3:'WHM408',
                       4:'TBS065',
                       5:'TLA611',
                       6:'VZB246',
                       7:'VZB120',
                       8:'SZS115',
                       9:'TLA612',
                       10:'TBO582',
                       11:'TBS435',
                       12:'VZB277',
                       13:'TLA613',
                       14:'VXI875',
                       15:'VXI791',
                       16:'VEG758'
                       }

    def agregar_evaluacion(self, evaluacion_obj):
        self.evaluaciones.append(evaluacion_obj)