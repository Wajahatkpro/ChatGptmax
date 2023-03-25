import openai
import streamlit as st

# Set OpenAI API key
openai.api_key = "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"

# Set Streamlit app title and background color
st.set_page_config(
    page_title="Turbo ChatGPT-3",
    page_icon=":speech_balloon:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(
    """
    <style>
    body {
        background-color: #1a1a1a;
        color: #fff;
    }
    .stButton button {
        background-color: #1da1f2;
        color: #fff;
    }
    .stTextInput input {
        background-color: #2b2b2b;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add app title
st.title("Turbo ChatGPT-3")

# Add input field for user's question
user_input = st.text_input("Enter your question:")

# Add output field for model's response
bot_response = st.empty()

# Add button to submit question and get response
if st.button("Get Response"):

    # Check if user input is empty
    if not user_input:
        st.warning("Please enter a question!")
    else:
        # Set OpenAI parameters
        model_engine = "text-davinci-002"
        max_tokens = 2048
        temperature = 0.7
        prompt = f"Q: {user_input}\nA:"

        # Call OpenAI API to generate response
        try:
            generated_text = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            # Print response to output field
            bot_response.text(generated_text.choices[0].text)
        except Exception as e:
            st.error(f"Error: {str(e)}")
