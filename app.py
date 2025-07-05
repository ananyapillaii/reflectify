import streamlit as st
import openai
from textblob import TextBlob
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Reflectify - AI Journal", layout="centered")
st.title("🧘 Reflectify - Mental Health Reflection Journal")

user_input = st.text_area("📝 How are you feeling today?")

if st.button("Reflect"):
    if user_input.strip() == "":
        st.warning("Please enter something.")
    else:
        with st.spinner("Thinking..."):
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            mood = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"

            prompt = f"You are a kind and thoughtful journal companion. The user says: '{user_input}'\nRespond supportively based on their emotional tone ({mood})."

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                reflection = response['choices'][0]['message']['content']
                st.subheader("🪞 AI's Reflection")
                st.write(reflection)

                st.caption(f"Detected mood: **{mood}**")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
