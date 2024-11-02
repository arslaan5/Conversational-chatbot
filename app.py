import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import streamlit as st
# from dotenv import load_dotenv

# Loading api key from the environment variable
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# Initializing the model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                            temperature=0.8,
                            api_key="GEMINI_API_KEY")

# Handling empty session state
if "Messages" not in st.session_state:
    st.session_state["Messages"] = [
        SystemMessage(content="You are a specialist chatbot in the field of General studies and life Scienes.")
    ]


# Function for getting the response from the model
def get_response(request):
    st.session_state["Messages"].append(HumanMessage(content = request))
    respone = llm.invoke(st.session_state["Messages"])
    st.session_state["Messages"].append(AIMessage(content = respone.content))
    return respone.content

# Setting-up streamlit ui
st.set_page_config(page_title="Conversational Chatbot ❤️",
                   layout="wide",
                   page_icon=":star:")
st.title("Lets Chat!")
st.write("I can chat like a human.")

# User input field
user_input = st.text_input("Input: ", key="input")
response = get_response(user_input)

submit_btn = st.button("Generate Response")

# When the button is clicked
if submit_btn:
    st.subheader("Generated Result:")
    st.write(response)