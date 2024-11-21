# chatbot_lang_graph
ChatBot with LangGraph 📚 🤖 😄
This project demonstrates how to build an interactive chatbot using LangGraph and Streamlit. The chatbot answers questions from the user using a combination of LangGraph's workflow engine and a large language model. It is built to handle user queries and generate responses effectively.

Features
LangGraph Integration: Uses the LangGraph library to define a flow for processing inputs, executing tools, and generating responses from the chatbot.
Streamlit UI: Provides an interactive web interface where users can ask questions and get answers in real-time.
Model: The chatbot leverages a ChatGroq model (Gemma2-9b-It) to provide responses to user queries.
Workflow
User Input: The user types a question into the input field.
LangGraph Workflow: The question is processed through LangGraph's workflow, which uses the ChatGroq model to generate an appropriate response.
Output: The response from the model is displayed on the screen.
Technologies Used
LangGraph: A framework to create workflows that integrate language models and tools.
Streamlit: A Python library for building interactive web applications.
ChatGroq: A large language model (Gemma2-9b-It) used to generate responses.
Transformers: Hugging Face's library for transformer models.
Requirements
Python 3.x
LangGraph
Streamlit
transformers
ChatGroq (or any LLM of choice)
Setup and Installation
Clone this repository:

bash
Copy code
git clone https://github.com/Abhay123-hub/chatbot-langgraph.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open the app in your browser at localhost:8501.

Usage
Enter any question in the input field.
Press the "Get Answer" button to receive a response from the chatbot.
View the chat history, where user queries and bot responses are displayed.
Limitations
Memory: The current version does not have memory support, meaning each session is stateless. The chatbot does not remember previous conversations between user interactions.
Future Work
Memory Support: Adding memory to the chatbot workflow to allow for more context-aware responses.
Enhanced User Interface: Improving the UI for better user interaction and adding features like multi-turn conversations.
Customization: Allowing users to customize chatbot behavior or switch between different models for varied experiences.
License
This project is licensed under the MIT License - see the LICENSE file for details.

