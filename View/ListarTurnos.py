def listarTurnos(st, controller):
    col1, col2, = st.columns(2)
    cont = 0
    with col1:
        for i in range(8):
            st.subheader(str(cont+1)+".   "+str(controller.orden[cont]))
            cont += 1
    with col2:
        for i in range(8):
            st.subheader(str(cont+1) + ".   "+str(controller.orden[cont]))
            cont += 1