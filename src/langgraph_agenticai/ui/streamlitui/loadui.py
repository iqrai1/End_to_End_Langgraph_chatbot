import streamlit as st
from src.langgraph_agenticai.ui.uiconfigfile import Config

class LoadSteamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=" " + self.config.get_page_title(), layout="wide")
        st.header(" " + self.config.get_page_title())

        with st.sidebar:
            llm_option = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_option)

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

                self.user_controls["GROQ_API_KEY"] = st.text_input(
                    "API Key",
                    type="password",
                    value=st.session_state.get("GROQ_API_KEY", ""),
                )
                st.session_state["GROQ_API_KEY"] = self.user_controls["GROQ_API_KEY"]

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ API Key to proceed")

            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

        return self.user_controls
