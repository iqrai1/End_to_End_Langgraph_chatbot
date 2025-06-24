import streamlit as st
from src.langgraph_agenticai.LLMS.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadSteamlitUI
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlitui.display import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    
  
    """

    ui = LoadSteamlitUI()
    user_input = ui.load_streamlit_ui()
    st.write("DEBUG: User input received:", user_input)
    st.write("DEBUG: GROQ_API_KEY (first 6 chars):", user_input.get("GROQ_API_KEY", "")[:6])


    if not user_input:
        st.error("Error: Something went wrong")
        return
        
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM Model could not be initilalized")
                return
            
            usecase =user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            graph_builder =GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph setup failed - {e}")
            return

