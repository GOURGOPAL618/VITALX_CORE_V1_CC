# ============================================
# auth.py — Login System with Quiz (FIXED - No Blank Space)
# Edge-Only · Local Storage · No Cloud
# ============================================

import streamlit as st
import json
import os
import hashlib
import random
from datetime import datetime

# File to store user data
USER_DATA_FILE = "users.json"

# Space-related quiz questions
SPACE_QUIZ = [
    {
        "question": "🚀 What is the name of India's first mission to the Moon?",
        "options": ["Mangalyaan", "Chandrayaan-1", "Gaganyaan", "Aditya-L1"],
        "correct": "Chandrayaan-1"
    },
    {
        "question": "🛰️ Who was the first Indian to go into space?",
        "options": ["Kalpana Chawla", "Sunita Williams", "Rakesh Sharma", "Ravish Malhotra"],
        "correct": "Rakesh Sharma"
    },
    {
        "question": "🌍 What is the closest planet to the Sun?",
        "options": ["Venus", "Earth", "Mars", "Mercury"],
        "correct": "Mercury"
    },
    {
        "question": "🔭 Which galaxy is Earth located in?",
        "options": ["Andromeda", "Milky Way", "Triangulum", "Sombrero"],
        "correct": "Milky Way"
    },
    {
        "question": "👨‍🚀 Which space agency operates the International Space Station (ISS)?",
        "options": ["ISRO", "ESA", "NASA", "Roscosmos"],
        "correct": "NASA"
    },
    {
        "question": "🌙 Which is the largest planet in our solar system?",
        "options": ["Saturn", "Jupiter", "Neptune", "Uranus"],
        "correct": "Jupiter"
    },
    {
        "question": "🛸 Who was the first person to walk on the Moon?",
        "options": ["Buzz Aldrin", "Neil Armstrong", "Michael Collins", "Yuri Gagarin"],
        "correct": "Neil Armstrong"
    }
]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USER_DATA_FILE):
        try:
            with open(USER_DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def register_user(user_id, password):
    users = load_users()
    if user_id in users:
        return False, "User ID already exists!"
    
    users[user_id] = {
        "password": hash_password(password),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_login": None
    }
    save_users(users)
    return True, "Registration successful!"

def login_user(user_id, password):
    users = load_users()
    if user_id not in users:
        return False, "User ID not found!"
    if users[user_id]["password"] != hash_password(password):
        return False, "Incorrect password!"
    
    users[user_id]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_users(users)
    return True, "Login successful!"

def show_login_ui():
    """Main login/signup UI - NO BLANK SPACE"""
    
    # Custom CSS to remove all default padding/margin
    st.markdown("""
        <style>
        /* Remove default Streamlit padding */
        .main > div {
            padding-top: 0rem !important;
        }
        
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }
        
        /* Remove top margin from first element */
        .stApp > header {
            display: none;
        }
        
        .login-container {
            max-width: 500px;
            margin: 30px auto;
            padding: 35px;
            background: linear-gradient(135deg, rgba(10, 14, 23, 0.95), rgba(5, 7, 12, 0.98));
            border-radius: 25px;
            border: 1px solid rgba(0, 200, 255, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .login-title {
            text-align: center;
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #FFFFFF, #00C8FF, #FFD700);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 30px;
        }
        
        .quiz-card {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            padding: 20px;
            margin: 15px 0;
            border-left: 3px solid #00C8FF;
        }
        
        /* Hide default Streamlit top bar */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    # Mode toggle
    if 'auth_mode' not in st.session_state:
        st.session_state.auth_mode = "login"
    
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    
    # Mode Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 LOGIN", use_container_width=True):
            st.session_state.auth_mode = "login"
            st.rerun()
    with col2:
        if st.button("🌟 SIGN UP", use_container_width=True):
            st.session_state.auth_mode = "signup"
            # Reset quiz state when switching to signup
            if 'quiz_score' in st.session_state:
                del st.session_state.quiz_score
            if 'quiz_answers' in st.session_state:
                del st.session_state.quiz_answers
            st.rerun()
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    if st.session_state.auth_mode == "login":
        # LOGIN FORM
        st.markdown('<div class="login-title">🚀 MISSION LOGIN</div>', unsafe_allow_html=True)
        
        user_id = st.text_input("👨‍🚀 User ID", placeholder="Enter your User ID", key="login_user")
        password = st.text_input("🔐 Password", type="password", placeholder="Enter password", key="login_pass")
        
        if st.button("🔓 LOGIN", use_container_width=True):
            if user_id and password:
                success, message = login_user(user_id, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.current_user = user_id
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.warning("Please enter User ID and Password")
    
    else:
        # SIGNUP FORM
        st.markdown('<div class="login-title">🌟 BECOME A MEMBER</div>', unsafe_allow_html=True)
        
        user_id = st.text_input("👨‍🚀 Choose User ID", placeholder="Create your User ID", key="signup_user")
        password = st.text_input("🔐 Create Password", type="password", placeholder="Create a strong password", key="signup_pass")
        confirm_password = st.text_input("✓ Confirm Password", type="password", placeholder="Confirm password", key="signup_confirm")
        
        st.markdown("---")
        st.markdown("### 🌌 SPACE CERTIFICATION QUIZ")
        st.caption("Answer at least 2 questions correctly to register")
        
        # Initialize quiz in session state
        if 'quiz_questions' not in st.session_state:
            # Randomly select 3 questions
            st.session_state.quiz_questions = random.sample(SPACE_QUIZ, 3)
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
        
        # Display quiz
        for i, q in enumerate(st.session_state.quiz_questions):
            st.markdown(f"""
                <div class="quiz-card">
                    <b style='color:#FFD700;'>Question {i+1}</b>
                    <p>{q['question']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            answer = st.radio(
                "",
                q['options'],
                key=f"quiz_{i}",
                label_visibility="collapsed",
                index=None
            )
            
            if answer:
                st.session_state.quiz_answers[i] = answer
        
        # Calculate score
        if st.session_state.quiz_answers:
            correct_count = 0
            for i, q in enumerate(st.session_state.quiz_questions):
                if i in st.session_state.quiz_answers and st.session_state.quiz_answers[i] == q['correct']:
                    correct_count += 1
        else:
            correct_count = 0
        
        st.markdown(f"""
            <div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:12px; padding:10px; margin:15px 0;'>
                <span style='color:#FFD700;'>📊 SCORE: {correct_count}/3</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Refresh quiz button
        col_q1, col_q2 = st.columns(2)
        with col_q1:
            if st.button("🔄 NEW QUESTIONS", use_container_width=True):
                st.session_state.quiz_questions = random.sample(SPACE_QUIZ, 3)
                st.session_state.quiz_answers = {}
                st.rerun()
        
        st.markdown("---")
        
        # Register button
        if st.button("✅ COMPLETE REGISTRATION", use_container_width=True):
            if not user_id:
                st.warning("Please enter a User ID")
            elif not password:
                st.warning("Please create a password")
            elif password != confirm_password:
                st.warning("Passwords do not match!")
            elif correct_count < 2:
                st.error(f"❌ Quiz failed! Score: {correct_count}/3. Need at least 2 correct.")
                st.info("Click 'NEW QUESTIONS' to try again with different questions.")
            else:
                success, message = register_user(user_id, password)
                if success:
                    st.success(f"✅ {message}")
                    st.balloons()
                    st.info("🎉 You are now a certified Mission Member! Please login.")
                    st.session_state.auth_mode = "login"
                    # Clear quiz state
                    for key in ['quiz_questions', 'quiz_answers', 'quiz_submitted']:
                        if key in st.session_state:
                            del st.session_state[key]
                    st.rerun()
                else:
                    st.error(message)
    
    st.markdown('</div>', unsafe_allow_html=True)