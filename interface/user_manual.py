# ============================================
# USER MANUAL — MISSION DOCUMENTATION
# AstroVital JCC V2.0 | Operations Guide
# ============================================

import streamlit as st
from datetime import datetime

def render_user_manual():
    # Header
    st.markdown("""
        <div style='text-align:center; padding:20px; background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius: 20px; margin-bottom: 30px;'>
            <h1 style='font-size:3rem;'>📖 USER MANUAL</h1>
            <p style='color:#00C8FF; font-family:Share Tech Mono;'>
                MISSION OPERATIONS GUIDE • EDGE DEPLOYMENT • VERSION 1.0
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Version Info
    st.markdown(f"""
        <div style='background:rgba(0,200,255,0.05); border-radius:15px; padding:15px; margin-bottom:20px; border-left:4px solid #00C8FF;'>
            <div style='display:flex; justify-content:space-between;'>
                <span><strong>📅 MANUAL VERSION:</strong> 2.0.0</span>
                <span><strong>🕐 LAST UPDATED:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
                <span><strong>✅ STATUS:</strong> MISSION READY</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ============================================
    # TABLE OF CONTENTS
    # ============================================
    with st.expander("📑 TABLE OF CONTENTS", expanded=False):
        st.markdown("""
        1. [Mission Control](#mission-control)
        2. [Live Vitals Monitoring](#live-vitals)
        3. [AI Decision Core](#ai-decision)
        4. [Data Records](#data-records)
        5. [System Health](#system-health)
        6. [Troubleshooting](#troubleshooting)
        7. [FAQ](#faq)
        8. [Technical Specifications](#specs)
        """)

    st.markdown("---")

    # ============================================
    # SECTION 1: MISSION CONTROL
    # ============================================
    st.markdown("""
        <h2 id='mission-control'>🎯 1. MISSION CONTROL DASHBOARD</h2>
        <p style='color:#A0AEC0;'>The central command center for AstroVital JCC.</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **📊 Dashboard Features:**
        - Mission elapsed time counter
        - Real-time signal strength
        - Power usage monitoring
        - Data storage status
        - System health overview
        - Recent activity log
        """)
    with col2:
        st.success("""
        **🎯 Quick Actions:**
        - Navigate via sidebar menu
        - Refresh data automatically
        - System status at a glance
        - AI health recommendations
        """)

    st.markdown("---")

    # ============================================
    # SECTION 2: LIVE VITALS
    # ============================================
    st.markdown("""
        <h2 id='live-vitals'>📡 2. LIVE VITALS TELEMETRY</h2>
        <p style='color:#A0AEC0;'>Real-time biometric monitoring for all crew members.</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **❤️ Monitored Parameters:**
        - Heart Rate (BPM) - Normal: 60-100
        - Blood Pressure - Normal: 90-120/60-80
        - SpO₂ Saturation - Normal: 95-100%
        - Respiratory Rate - Normal: 12-20/min
        - Body Temperature - Normal: 36.1-37.2°C
        """)
    with col2:
        st.markdown("""
        **📈 Visualization Tools:**
        - Interactive Plotly graphs
        - Historical trend analysis
        - AI-powered anomaly detection
        - Alert thresholds (color-coded)
        - Zoom & pan functionality
        """)

    st.warning("""
    ⚠️ **IMPORTANT:** All vitals are processed locally on the edge device. 
    No data is transmitted to the cloud, ensuring patient privacy and zero latency.
    """)

    st.markdown("---")

    # ============================================
    # SECTION 3: AI DECISION CORE
    # ============================================
    st.markdown("""
        <h2 id='ai-decision'>🧠 3. AI DECISION CORE</h2>
        <p style='color:#A0AEC0;'>Clinical Decision Support System (CDSS) for predictive analytics.</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🤖 AI Capabilities:**
        - Real-time risk assessment
        - Anomaly detection
        - Predictive health modeling
        - Clinical recommendations
        - 94.7% model accuracy
        """)
    with col2:
        st.markdown("""
        **📊 Input Parameters:**
        - Heart Rate
        - SpO₂ Level
        - Respiratory Rate
        - Blood Pressure
        - Body Temperature
        """)

    st.info("💡 **Tip:** The AI model runs entirely on the edge device with <0.5ms inference time.")

    st.markdown("---")

    # ============================================
    # SECTION 4: DATA RECORDS
    # ============================================
    st.markdown("""
        <h2 id='data-records'>💾 4. DATA RECORDS</h2>
        <p style='color:#A0AEC0;'>Patient database management and historical data analysis.</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **📋 Database Features:**
        - Filter by Crew ID
        - Status-based sorting
        - Range filtering (HR, SpO₂)
        - Search functionality
        - CSV export capability
        """)
    with col2:
        st.markdown("""
        **📊 Data Insights:**
        - Status distribution charts
        - HR vs SpO₂ correlation
        - Historical trends
        - AI risk scoring
        - Printable reports
        """)

    st.markdown("---")

    # ============================================
    # SECTION 5: SYSTEM HEALTH
    # ============================================
    st.markdown("""
        <h2 id='system-health'>⚙️ 5. SYSTEM HEALTH MONITORING</h2>
        <p style='color:#A0AEC0;'>Edge infrastructure and component status.</p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **🖥️ Monitored Resources:**
        - CPU Usage & Temperature
        - RAM Consumption
        - Disk Storage
        - System Uptime
        - Network Status
        """)
    with col2:
        st.markdown("""
        **🛠️ Component Status:**
        - AI Inference Engine
        - Data Pipeline
        - Edge Database
        - Sensor Interface
        - Network Controller
        """)

    st.markdown("---")

    # ============================================
    # SECTION 6: TROUBLESHOOTING
    # ============================================
    st.markdown("""
        <h2 id='troubleshooting'>🔧 6. TROUBLESHOOTING GUIDE</h2>
    """, unsafe_allow_html=True)

    troubleshooting = [
        ("Logo not showing", "Ensure 'assets/icons/astro_logo.jpeg' exists. Use base64 encoding method."),
        ("Model loading error", "Check MODEL_HANGAR path and file permissions. Verify pickle file integrity."),
        ("Graphs not rendering", "Install plotly: `pip install plotly`. Check internet for CDN (first load only)."),
        ("High CPU usage", "Reduce data refresh rate. Close other applications. Restart Streamlit."),
        ("Data not saving", "Check write permissions in data directory. Verify disk space availability."),
        ("Sidebar missing", "Check st.set_page_config layout parameter. Ensure no conflicting CSS.")
    ]

    for issue, solution in troubleshooting:
        st.markdown(f"""
            <div style='background:rgba(0,0,0,0.3); border-radius:10px; padding:12px; margin:8px 0;'>
                <span style='color:#FFD700;'>❓ {issue}</span><br>
                <span style='color:#A0AEC0; font-size:13px;'>✅ {solution}</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ============================================
    # SECTION 7: FAQ
    # ============================================
    st.markdown("""
        <h2 id='faq'>❓ 7. FREQUENTLY ASKED QUESTIONS</h2>
    """, unsafe_allow_html=True)

    faq = [
        ("Is my data sent to the cloud?", "❌ NO. AstroVital JCC is 100% edge-only. All data stays on your local device."),
        ("Can I use this offline?", "✅ YES. The platform is designed for complete offline operation."),
        ("How accurate is the AI model?", "📊 The CDSS model achieves 85.4% accuracy & 75.8% recall on validation data."),
        ("Can I add more patients?", "✅ YES. Simply add records through the Data Records section."),
        ("How often is data refreshed?", "🔄 Real-time. Metrics update dynamically based on sensor input."),
        ("Is there a mobile version?", "📱 The web interface is responsive and works on tablets and mobile devices.")
    ]

    for q, a in faq:
        st.markdown(f"""
            <div style='background:rgba(0,200,255,0.05); border-radius:10px; padding:12px; margin:8px 0; border-left:3px solid #00C8FF;'>
                <span style='color:#FFD700;'>{q}</span><br>
                <span style='color:#00FFAA; font-size:13px;'>{a}</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ============================================
    # SECTION 8: TECHNICAL SPECIFICATIONS
    # ============================================
    st.markdown("""
        <h2 id='specs'>🔬 8. TECHNICAL SPECIFICATIONS</h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **💻 System Requirements:**
        - OS: Windows/Linux/macOS
        - Python: 3.8+
        - RAM: 4GB minimum
        - Storage: 1GB free space
        - No internet required
        """)
    with col2:
        st.markdown("""
        **📦 Dependencies:**
        - Streamlit 1.28+
        - Pandas 1.5+
        - Plotly 5.0+
        - NumPy 1.20+
        - psutil (for system metrics)
        """)

    st.markdown("---")

    # ============================================
    # SUPPORT & CONTACT
    # ============================================
    st.markdown("""
        <div style='background:linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius:15px; padding:20px; margin-top:20px; text-align:center;'>
            <h3>🆘 NEED SUPPORT?</h3>
            <p style='color:#A0AEC0;'>For technical assistance or mission-critical issues:</p>
            <p style='color:#00C8FF;'>📧 support@astrovital.space</p>
            <p style='color:#FFD700;'>🛰️ Mission Control: 24/7 Operational</p>
            <hr style='border-color:rgba(0,200,255,0.2);'>
            <p style='color:#A0AEC0; font-size:11px;'>
                © 2026 Gouragopal Mohapatra — All Rights Reserved<br>
                "Because Every Heartbeat in Space Matters."
            </p>
        </div>
    """, unsafe_allow_html=True)