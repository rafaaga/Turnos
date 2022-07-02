import json

def salida(st, controller, info):
	en_lista = []
	st.title("Registrar Salida de Vehículo")
	orden = info["orden"]
	n = info["n"]
	for i in range(n):
		if(orden[i]<10):
			en_lista.append("0"+str(orden[i])+" - " +str(controller.placas.get(orden[i])))
		else:
			en_lista.append(str(orden[i]) + " - " + str(controller.placas.get(orden[i])))
	seleccion = st.selectbox("Selección", en_lista)
	borrar = st.button("REGISTRAR")
	if(borrar == True):
		numero = seleccion[0]+seleccion[1]
		numero = int(numero)
		i = orden.index(numero)
		orden.pop(i)
		orden.append(0)
		n -= 1
		d = {"orden": orden,
		 "n": n }
		with open('orden.json', 'w') as file:
			json.dump(d, file, indent=1)
		st.text("Se eliminó a "+str(seleccion)+" de la cola")

def entrada(st, controller, info):
	st.title("Registrar Salida de Vehículo")
	lista = []
	orden = info["orden"]
	n = info["n"]
	for key in controller.placas:
		if(key<10):
			lista.append("0"+str(key)+" - " +str(controller.placas.get(key)))
		else:
			lista.append(str(key)+" - " +str(controller.placas.get(key)))
	seleccion = st.selectbox("Selección", lista)
	ingresar = st.button("REGISTRAR")
	if(ingresar == True):
		numero = seleccion[0]+seleccion[1]
		numero = int(numero)
		en_cola = False
		for i in range(n):
			if(numero == orden[i]):
				en_cola = True
				st.text(seleccion+" ya está en la cola, no se puede agregar")
		if(en_cola == False):
			orden[n] = numero
			n += 1
			d = {"orden": orden,
			 "n": n }
			with open('orden.json', 'w') as file:
				json.dump(d, file, indent=1)
			st.text("Se agregó a "+str(seleccion)+" a la cola")