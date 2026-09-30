import streamlit as st
import random
import time

# Set up cute pink page layout configuration for mobile phone screens
st.set_page_config(page_title="A Message For You! 💕", page_icon="✨", layout="centered")

# Custom Baby Pink Mobile Styling
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1, h2, h3 { color: #FF69B4 !important; font-family: 'Comic Sans MS', sans-serif; text-align: center; }
    div.stButton > button {
        background-color: #FF69B4; color: white; border-radius: 20px;
        border: none; padding: 10px 25px; font-family: 'Comic Sans MS', sans-serif;
        font-weight: bold; width: 100%; box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.3);
    }
    div.stButton > button:hover { background-color: #FFB6C1; color: white; }
    .cat-container { text-align: center; font-size: 80px; margin: 10px 0; }
    .arrow-text { color: #FFB6C1; font-family: monospace; text-align: center; font-weight: bold; margin-bottom: 5px; }
    .plea-text { color: #DB7093; font-family: 'Comic Sans MS', sans-serif; font-size: 18px; text-align: center; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Initialize interactive screen states
if "page" not in st.session_state:
    st.session_state.page = 1
if "no_count" not in st.session_state:
    st.session_state.no_count = 0

# --- PAGE 1: THE INVITATION ---
if st.session_state.page == 1:
    st.write("# Hey! Look over here! 💕")
    
    # Large cute cat emoji placeholder for clean phone screen sizing
    st.markdown('<div class="cat-container">🐱🌸</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="arrow-text">👇 CLICK HERE 👇</div>', unsafe_allow_html=True)
    if st.button("Will you be my best friend? 💖"):
        st.session_state.page = 2
        st.rerun()

# --- PAGE 2: THE LOYALTY QUESTION ---
elif st.session_state.page == 2:
    st.write("# Yay! Now for the next question... 🌸")
    
    st.markdown('<p class="plea-text">Will you always be a good friend to me? 👉👈</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES! 🥰"):
            st.session_state.page = "yes_screen"
            st.rerun()
            
    with col2:
        if st.button("No 🥺"):
            st.session_state.no_count += 1
            st.rerun()

    # Reactive changes depending on rejection count tracking
    if st.session_state.no_count == 1:
        st.markdown('<p class="plea-text" style="color:#FF1493; margin-top:20px;">Please?? 🥺 Pretty please? Say yes! 💕</p>', unsafe_allow_html=True)
    elif st.session_state.no_count >= 2:
        st.session_state.page = "angry_screen"
        st.rerun()

# --- SUCCESS PAGE ---
elif st.session_state.page == "yes_screen":
    st.write("# YAYYY! You're the best! 🎉💞")
    st.balloons() # Automatically triggers mobile balloon animation popups!
    st.markdown('<div class="cat-container">🥰🎈💖</div>', unsafe_allow_html=True)
    if st.button("Restart 🔄"):
        st.session_state.page = 1
        st.session_state.no_count = 0
        st.rerun()

# --- ANGRY PAGE ---
elif st.session_state.page == "angry_screen":
    st.write("# Hmph! 😤 BYE!")
    st.markdown('<div class="cat-container">😡💢👎</div>', unsafe_allow_html=True)
    if st.button("Try Again 🥺"):
        st.session_state.page = 1
        st.session_state.no_count = 0
        st.rerun(