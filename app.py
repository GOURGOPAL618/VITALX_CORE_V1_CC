# ============================================
# ASTROVITAL JCC V2.0 — With Login System (WORKING)
# Developer: Gouragopal Mohapatra
# ============================================

import streamlit as st
import base64
from datetime import datetime
from auth import show_login_ui

st.set_page_config(
    page_title="ASTROVITAL AI : VITALX CORE V1| Mission Control",
    page_icon="🛸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None

# ============================================
# SHOW LOGIN PAGE IF NOT LOGGED IN
# ============================================
if not st.session_state.logged_in:
    show_login_ui()
    st.stop()

# ============================================
# MAIN APP — ONLY SHOWS AFTER LOGIN
# ============================================

def load_css():
    st.markdown("""
        <style>
        * {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        .stApp {
            background: radial-gradient(ellipse at 20% 30%, #0a0c15, #05060a);
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, rgba(8, 10, 18, 0.98), rgba(3, 5, 10, 0.98));
            backdrop-filter: blur(12px);
            border-right: 1px solid rgba(0, 229, 255, 0.15);
        }
        .hero-logo {
            text-align: center;
            padding: 35px 20px 25px 20px;
            border-bottom: 2px solid rgba(0, 229, 255, 0.3);
            margin-bottom: 25px;
        }
        .hero-logo img {
            width: 140px;
            margin-bottom: 15px;
            filter: drop-shadow(0 0 20px rgba(0, 229, 255, 0.4));
        }
        .hero-title {
            font-size: 20px;
            font-weight: 800;
            background: linear-gradient(135deg, #FFFFFF, #00E5FF, #FFD700);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-sub {
            font-size: 9px;
            color: #5A6E8A;
            letter-spacing: 3px;
            margin-top: 5px;
        }
        .nav-head {
            font-size: 10px;
            font-weight: 700;
            color: #3A4A60;
            letter-spacing: 2px;
            padding: 0 16px;
            margin-bottom: 10px;
        }
        div[data-testid="stSelectbox"] {
            display: none;
        }
        .blockbuster-nav {
            display: block;
            width: 100%;
            text-align: left;
            padding: 10px 20px;
            margin: 4px 0;
            background: transparent;
            border: none;
            border-radius: 10px;
            color: #8E9AAC;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .blockbuster-nav:hover {
            background: rgba(0, 229, 255, 0.08);
            color: #00E5FF;
            transform: translateX(5px);
        }
        .nav-active {
            background: linear-gradient(90deg, rgba(0, 229, 255, 0.12), transparent);
            color: #00E5FF;
            border-left: 3px solid #00E5FF;
        }
        .status-panel {
            margin: 30px 16px 20px 16px;
            padding: 15px;
            background: linear-gradient(135deg, rgba(0, 0, 0, 0.4), rgba(0, 30, 40, 0.2));
            border-radius: 18px;
            border: 1px solid rgba(0, 229, 255, 0.2);
        }
        .status-row {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .status-row:last-child {
            border-bottom: none;
        }
        .status-label {
            font-size: 10px;
            color: #6A7A90;
        }
        .status-value {
            font-size: 10px;
            font-weight: 700;
        }
        .blink-led {
            display: inline-block;
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #00FF88;
            box-shadow: 0 0 8px #00FF88;
            animation: pulse 1.5s infinite;
            margin-right: 5px;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        .cinema-footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(3, 5, 10, 0.95);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(0, 229, 255, 0.2);
            padding: 8px 32px;
            z-index: 999;
        }
        .footer-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .footer-block {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .footer-text {
            font-size: 9px;
            color: #5A6E8A;
        }
        .footer-glow {
            color: #00E5FF;
            font-weight: 600;
        }
        .footer-divider {
            width: 1px;
            height: 14px;
            background: rgba(0, 229, 255, 0.2);
        }
        footer {
            display: none !important;
        }
        .main .block-container {
            padding-bottom: 65px;
        }
                /* Remove default Streamlit padding from main app */
.main > div {
    padding-top: 0rem !important;
}
.block-container {
    padding-top: 1rem !important;
}
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

def render_sidebar():
    logo_base64 = get_image_base64("assets/icons/astro_logo.jpeg")
    
    with st.sidebar:
        if logo_base64:
            st.markdown(f"""
                <div class="hero-logo">
                    <img src='data:image/jpeg;base64,{logo_base64}'/>
                    <div class="hero-title">ASTROVITAL</div>
                    <div class="hero-sub">JCC · MISSION CONTROL</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="hero-logo">
                    <div style="font-size: 52px;">🚀</div>
                    <div class="hero-title">ASTROVITAL AI : VITALX CORE V1</div>
                    <div class="hero-sub">CC · MISSION CONTROL</div>
                </div>
            """, unsafe_allow_html=True)
        
        # User welcome
        st.markdown(f"""
            <div style='padding: 0 16px; margin-bottom: 20px;'>
                <div style='background:rgba(0,200,255,0.1); border-radius:10px; padding:8px; text-align:center;'>
                    <span style='color:#FFD700; font-size:11px;'>👨‍🚀 WELCOME</span><br>
                    <span style='color:#00C8FF; font-weight:bold; font-size:12px;'>{st.session_state.current_user}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="nav-head">MISSION NAVIGATION</div>', unsafe_allow_html=True)
        
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "🎯 MISSION CONTROL"
        
        nav_options = [
            "🎯 MISSION CONTROL",
            "📡 LIVE VITALS",
            "🧠 AI DECISION",
            "💾 DATA RECORDS",
            "⚙️ SYSTEM HEALTH",
            "📖 USER MANUAL"
        ]
        
        for opt in nav_options:
            is_active = st.session_state.current_page == opt
            active_class = "nav-active" if is_active else ""
            st.markdown(f'<div class="blockbuster-nav {active_class}">{opt}</div>', unsafe_allow_html=True)
            
            if st.button(opt, key=f"nav_{opt}", use_container_width=True):
                st.session_state.current_page = opt
                st.rerun()
        
        page = st.session_state.current_page
        
        st.markdown("""
            <div class="status-panel">
                <div class="status-row">
                    <span class="status-label">EDGE MODE</span>
                    <span class="status-value"><span class="blink-led"></span>ACTIVE</span>
                </div>
                <div class="status-row">
                    <span class="status-label">CLOUD</span>
                    <span class="status-value" style="color:#FF4444;">🔴 NO CONNECTION</span>
                </div>
                <div class="status-row">
                    <span class="status-label">MISSION</span>
                    <span class="status-value" style="color:#00FF88;">NOMINAL</span>
                </div>
                <div class="status-row">
                    <span class="status-label">DEPLOYMENT</span>
                    <span class="status-value" style="color:#00E5FF;">EDGE-ONLY</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 LOGOUT", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.rerun()
        
        return page

def render_footer():
    current_time = datetime.now().strftime("%H:%M:%S")
    st.markdown(f"""
        <div class="cinema-footer">
            <div class="footer-container">
                <div class="footer-block">
                    <span class="blink-led"></span>
                    <span class="footer-text">SYSTEM <span class="footer-glow">NOMINAL</span></span>
                </div>
                <div class="footer-divider"></div>
                <div class="footer-block">
                    <span class="footer-text">🔴 NO CLOUD · EDGE-ONLY</span>
                </div>
                <div class="footer-divider"></div>
                <div class="footer-block">
                    <span class="footer-text">👨‍🚀 {st.session_state.current_user}</span>
                </div>
                <div class="footer-divider"></div>
                <div class="footer-block">
                    <span class="footer-text">🕐 <span class="footer-glow">{current_time}</span> UTC</span>
                </div>
                <div class="footer-divider"></div>
                <div class="footer-block">
                    <span class="footer-text">© 2026</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    selected_page = render_sidebar()
    
    if "MISSION CONTROL" in selected_page:
        from interface.home import render_home
        render_home()
    elif "LIVE VITALS" in selected_page:
        from interface.vitals import render_vitals
        render_vitals()
    elif "AI DECISION" in selected_page:
        from interface.ai_decision import render_ai_decision
        render_ai_decision()
    elif "DATA RECORDS" in selected_page:
        from interface.data_records import render_data_records
        render_data_records()
    elif "SYSTEM HEALTH" in selected_page:
        from interface.system_health import render_system_health
        render_system_health()
    elif "USER MANUAL" in selected_page:
        from interface.user_manual import render_user_manual
        render_user_manual()
    
    render_footer()

if __name__ == "__main__":
    main()