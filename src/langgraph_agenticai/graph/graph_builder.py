from langgraph.graph import StateGraph,START, END
from langchain_core.runnables import RunnableLambda
from src.langgraph_agenticai.states.state import State
from src.langgraph_agenticai.nodes.basic_chatbot_node import basicChatbotNode

class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
         
         self.basic_Chatbot_Node = basicChatbotNode(self.llm)
         chatbot_runnable = RunnableLambda(self.basic_Chatbot_Node.process)

         self.graph_builder.add_node("chatbot",chatbot_runnable)
         self.graph_builder.add_edge(START,"chatbot")
         self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()