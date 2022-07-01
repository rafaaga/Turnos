def salida(st, controller):
	controller.orden.pop(0)
	controller.orden.append(0)
	controller.n -= 1

def entrada(controller, value):
	controller.orden[controller.n] = value
	controller.n += 1