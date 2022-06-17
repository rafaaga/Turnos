import streamlit as st
from streamlit_option_menu import option_menu
import Controlador
from Controlador.Controller import Vehiculos
from View.ListarTurnos import listarTurnos


class MainView:
    def __init__(self) -> None:
        super().__init__()

        # Estretagia para manejar el "estado" del controllador y del modelo entre cada cambio de ventana
        if 'main_view' not in st.session_state:
            self.menu_actual = "About"

            # Conexión con el controlador
            self.controller = Vehiculos()

            st.session_state['main_view'] = self
        else:

            # Al exisir en la sesión entonces se actualizan los valores
            self.menu_actual = st.session_state.main_view.menu_actual
            self.controller = st.session_state.main_view.controller

        self._dibujar_layout()

    def _dibujar_layout(self):
        # Set page title, icon, layout wide (more used space in central area) and sidebar initial state
        st.set_page_config(page_title="Turnos", page_icon='https://static.wixstatic.com/media/012503_f8e788dce4c54b428a4d47bac8b85208~mv2.png', layout="wide", initial_sidebar_state="collapsed", menu_items=None)
        # Defines the number of available columns del area principal
        self.col1, self.col2, self.col3, self.col4 = st.columns([1, 1, 1, 1])

        # Define lo que abrá en la barra de menu
        with st.sidebar:
            st.image('https://static.wixstatic.com/media/012503_f8e788dce4c54b428a4d47bac8b85208~mv2.png', '',
                     300)
            self.menu_actual = option_menu("Menú", ['Listar Turnos', 'Registrar LLegada', 'Registrar Salida'],
                                        icons=['bi bi-bar-chart-steps', 'bi bi-arrow-down-left-square', 'bi bi-arrow-up-right-square'], menu_icon="bi bi-view-list", default_index=0, orientation="horizontal")
    def controlar_menu(self):
        if self.menu_actual == "Listar Turnos":
            listarTurnos(st, self.controller)
# Main call
if __name__ == "__main__":
    main = MainView()
    main.controlar_menu()