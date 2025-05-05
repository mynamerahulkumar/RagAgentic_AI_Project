import streamlit as st

import json 

from src.agenticailanggraph.frontend.streamlitui.loadfronend import LoadStreamLitFrontend


#Main function start

def load_rag_lanaggraph_agentic_app():
     """
        Loads and runs the LangGraph AgenticAI application with Streamlit UI.
        This function initializes the UI, handles user input, configures the LLM model,
        sets up the graph based on the selected use case, and displays the output while 
        implementing exception handling for robustness.
     """
   
     #Load UI
   
     frontend=LoadStreamLitFrontend()
     user_input=frontend.load_streamlit_frontend()
     
     if not user_input:
         st.error("Error: Failed to Load user input from the frontend")
         return
     
     #Text input for user message
     if st.session_state.IsFetchButtonClicked:
         user_message=st.session_state.timeframe
     else:
         user_message=st.chat_input("Enter your message")
     