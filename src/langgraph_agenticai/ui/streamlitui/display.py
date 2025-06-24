import streamlit as st

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        if self.usecase == "Basic Chatbot":
            # Stream events coming from the graph with user message input
            for event in self.graph.stream({'messages': ("user", self.user_message)}):
                for value in event.values():
                    # Display user's message in chat bubble
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    # Display assistant's reply
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
