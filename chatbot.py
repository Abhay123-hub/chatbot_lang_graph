from langgraph.graph import StateGraph,MessagesState,START,END
from langgraph.graph.message import add_messages
from typing import Annotated,Literal,TypedDict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

## let us creating the class for chatbot
class chatbot:
    def __init__(self):
        self.llm = ChatGroq(model_name="Gemma2-9b-It")
    def call_tool(self):
        tool = TavilySearchResults(max_results=2)
        tools = [tool]
        self.tool_node = ToolNode(tools = [tool])
        self.llm_with_tool = self.llm.bind_tools(tools)
    def call_model(self,state:MessagesState):
        messages = state["messages"]
        response = self.llm_with_tool.invoke(messages)
        return {"messages":[response]}
    def router_function(self,state:MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        else:
            return END
    def __call__(self):
        self.call_tool()
        workflow = StateGraph(MessagesState)
        workflow.add_node("agent",self.call_model)
        workflow.add_node("tools",self.tool_node)
        workflow.add_edge(START,"agent")
        workflow.add_conditional_edges("agent",self.router_function,{"tools":"tools",END:END})
        workflow.add_edge("tools","agent")
        self.app = workflow.compile()
        return self.app
if __name__ == "__main__":
    mybot = chatbot()
    workflow = mybot()
    inputs = {"messages":"[So What is my name?]"}
    response = workflow.invoke(inputs)
    print(response['messages'][-1].content)