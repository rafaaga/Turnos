
def listarTurnos(st, controller, orden):
    col1, col2, = st.columns(2)
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
            st.subheader(str(cont + 1) + ".   " + str(controller.placas.get(orden[cont])))
        cont += 1
    return cont