from bokeh.models.widgets import Div

def salida(st, controller, ws):
	orden = []
	en_lista = []
	st.title("Registrar Salida de Vehículo")
	for i in range(2, 18): orden.append(int(ws.cell(i,2).value))
	n = int(ws.cell(18,2).value)
	if (n>0):
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
			st.text
			orden.pop(i)
			orden.append(0)
			n -= 1
			ws.update('B18', n)
			for i in range(2, 18):
				celda = "B"+str(i)
				ws.update(celda,orden[i-2])
			st.text("Se eliminó a "+str(seleccion)+" de la cola")
	else:
		st.subheader("Aún no hay conductores en lista")

def entrada(st, controller, ws):
	st.title("Registrar Llegada de Vehículo")
	lista = []
	orden = []
	for i in range(2, 18): orden.append(int(ws.cell(i,2).value))
	n = int(ws.cell(18,2).value)
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
			ws.update('B18', n)
			for i in range(2, 18):
				celda = "B"+str(i)
				ws.update(celda,orden[i-2])
			st.text("Se agregó a "+str(seleccion)+" a la cola")

def acceder_a_historial(st):
	boton = st.button("Ir a Excel")
	if boton:
		link = 'https://docs.google.com/spreadsheets/d/18A8xVpVIUmji5KhsyycquCtoNTCPUEkW8kHISCzJIvM/edit#gid=0'
		st.markdown(link, unsafe_allow_html=True)