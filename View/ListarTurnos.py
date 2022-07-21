
def listarTurnos(st, controller, ws):
    col1, col2, = st.columns(2)
    orden = []
    for i in range(2, 18):
        orden.append(int(ws.cell(i,2).value))
    cont = 0
    with col1:
            cont = imprimir(st,controller,cont, orden)
    with col2:
            cont = imprimir(st, controller, cont, orden)

def imprimir(st, controller, cont, orden):
    for i in range(8):
        if (orden[cont] == 0):
            st.subheader(str(cont+1)+". --- ---")
        else:
            if(orden[cont]<10):
                st.subheader(str(cont + 1) + ". "+" 0"+str(orden[cont]) +" - " + str(controller.placas.get(orden[cont])))
            else:
                st.subheader(str(cont + 1) + ". " + str(orden[cont]) + " - " + str(controller.placas.get(orden[cont])))
        cont += 1
    return cont