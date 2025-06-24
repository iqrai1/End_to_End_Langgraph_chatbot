from src.langgraph_agenticai.states.state import State

class basicChatbotNode:
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        # Call the function directly instead of .invoke()
        return {"messages": self.llm(state["messages"])}
