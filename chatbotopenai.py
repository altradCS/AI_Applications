import streamlit as st
from openai import OpenAI

# Function to interact with the OpenAI API
def query_openai_chat(user_input):
    
    openai.api_key = "..............."
    openai.base_model = "............."
    MODEL_DI = "...............f"
    
    chat_completion = openai.chat.completion.create(
        model=MODEL_DI,
        messages=[{"role": "user", "content": user_inaput}],
        stream=False,  # Set to False for simpler handling
        max_tokens=1000,
    )

    # Assuming no streaming, we directly access the first (and only) choice's message content
    response_content = chat_completion.choices[0].message["content"] if chat_completion.choices else "No response."
    return response_content

# Streamlit UI
st.title("AI Chatbot")
user_query = st.text_input("Enter your question:", "")

if st.button("Ask"):
    if user_query:
        with st.spinner("Talking to AI Chatbot..."):
            response_content = query_openai_chat(user_query)
            st.write(response_content)  # Display the formatted response
    else:
        st.write("Please enter a question to ask the AI.")
