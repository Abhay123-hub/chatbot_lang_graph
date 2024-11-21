## here i will be writting the code for the UI interface of my chatbot
import streamlit as st
from transformers import pipeline
from chatbot import chatbot
mybot = chatbot()
workflow = mybot()

## set up the streamlit UI(user interface)
st.title("ChatBot With LangGraph 📚 😄 🤖 🧐 ")
st.write("Ask any question I will try to answer it")

## input text box for the question
question = st.text_input("Enter your question here 🤖")

input = {"messages":[question]}

## button to get the answer
if st.button("Get Answer"):
    if input:
        response = workflow.invoke(input)
        st.write("**Answer**",response["messages"][-1].content)
    else:
        st.warning("Please enter the question to get the answer")
## additional styling
st.markdown("-----")
st.caption("Powered by Streamlit and Transformers")
