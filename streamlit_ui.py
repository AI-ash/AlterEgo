from datetime import datetime
import streamlit as st
from main import ai_talk  

st.set_page_config(page_title="AlterEgo", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    .stSidebar {
        background-color: #1a1d23 !important;
        padding: 20px;
        border-right: 1px solid #333;
    }
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4 {
        color: #f5f5f5 !important;
    }
    .stTextInput > div > div > input, 
    .stTextArea > div > textarea, 
    .stNumberInput input {
        background-color: #2a2f3b !important;
        color: #ffffff !important;
        border: 1px solid #444;
        border-radius: 10px;
    }
    .stRadio > div {
        background-color: #2a2f3b;
        padding: 10px;
        border-radius: 10px;
    }
    .stButton > button {
        border-radius: 12px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 8px 16px;
        font-weight: bold;
        transition: all 0.2s ease-in-out;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #764ba2, #667eea);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AlterEgo – Your Custom AI Friend")

with st.sidebar.form(key="persona_form"):
    st.header("📝 Define Your Ego")
    name = st.text_input("👤 Name", placeholder="What should your AI be called?")
    gender = st.radio("⚧️ Gender", ["Male", "Female"])
    age = st.number_input("🎂 Age", min_value=5, max_value=100, value=20)
    hobbies = st.text_input("🎨 Hobbies", placeholder="e.g. reading, gaming, music")
    personality = st.text_area("💭 Personality", placeholder="e.g. Friendly, curious, and supportive")
    style = st.text_area("🎙️ Speaking Style", placeholder="e.g. Casual and humorous")
    st.caption("✨ Tip: Be creative – your choices shape how your AlterEgo will act.")
    st.markdown("---")
    submit_button = st.form_submit_button("✨ Create AlterEgo")

    
    if submit_button:
        if not all([name.strip(), gender.strip(), str(age).strip(), hobbies.strip(), personality.strip(), style.strip()]):
            st.error("⚠️ Please fill in all the fields before submitting.")
        else:
            st.session_state.profile = f"""
You are {name}, a {age}-year-old {gender} a personal AI assistant.
Your hobbies are: {hobbies}.
Your personality is: {personality}.
You should respond in a {style} way.
Always stay in character as {name}Keep the conversation natural and engaging. Remember to stay in character as {name}.
"""
            st.success(f"✅ AlterEgo '{name}' created successfully!")


st.subheader(f"💬 Chat with {name if name else 'your friend'}")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if "profile" not in st.session_state:
    st.warning("⚠️ Please create your AlterEgo first in the sidebar.")
else:
    prompt = st.chat_input(f"Say something to {name if name else 'your friend'}...")
    if prompt == None:
        prompt = "Introduce yourself"
        st.session_state.messages.append({"role": "user", "content": prompt})
    
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

    with st.chat_message("assistant"):
        response = ai_talk(st.session_state.profile, prompt) 
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    reset = st.button("Clear chat window.")
    if reset:
        st.session_state.messages.clear()
        st.rerun()