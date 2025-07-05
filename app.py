import streamlit as st
from textblob import TextBlob
from transformers import pipeline

# Load the HuggingFace GPT-2 model
generator = pipeline("text-generation", model="gpt2")

st.set_page_config(page_title="Reflectify - Mental Health Reflection Journal", layout="centered")
st.title("🧘 Reflectify - Mental Health Reflection Journal")

user_input = st.text_area("📝 How are you feeling today?")

if st.button("Reflect"):
    if user_input.strip() == "":
        st.warning("Please enter something.")
    else:
        with st.spinner("Reflecting..."):
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            mood = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"

            # Generate response using GPT-2
            prompt = f"The user said: '{user_input}'. Respond supportively based on this feeling:"
            result = generator(prompt, max_length=60, num_return_sequences=1)
            reflection = result[0]['generated_text']

            st.subheader("🪞 AI's Reflection")
            st.write(reflection.strip())

            st.caption(f"Detected mood: **{mood}**")
