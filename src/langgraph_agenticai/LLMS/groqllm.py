import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY", "")
            selected_groq_model = self.user_controls_input.get("selected_groq_model", "")

            env_api_key = os.environ.get("GORQ_API_KEY", "")

            if groq_api_key == "" and env_api_key == "":
                st.error("Please Enter the Groq API Key")
                return None  # Early return if no API key

            # Prefer user input key, otherwise use env key
            api_key_to_use = groq_api_key if groq_api_key else env_api_key

            llm = ChatGroq(api_key=api_key_to_use, model=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception: {e}")
        return llm
