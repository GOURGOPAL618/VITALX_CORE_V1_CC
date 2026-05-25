# ============================================
# LIVE VITALS MONITORING — NASA GRADE
# AstroVital JCC V2.0 | Real-time Telemetry
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

def render_vitals():
    # Header
    st.markdown("""
        <div style='text-align:center; padding:20px; background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius: 20px; margin-bottom: 30px;'>
            <h1 style='font-size:3rem;'>📡 LIVE VITALS TELEMETRY</h1>
            <p style='color:#00C8FF; font-family:Share Tech Mono;'>
                REAL-TIME BIOMETRIC DATA • EDGE PROCESSING • AI-ENHANCED
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Patient Selection
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        patient_id = st.selectbox(
            "👨‍🚀 SELECT ASTRONAUT / PATIENT",
            [f"CREW-{i:03d}" for i in range(1, 11)],
            format_func=lambda x: f"🛸 {x}"
        )
    with col2:
        time_range = st.selectbox("⏱️ TIME RANGE", ["Last 1 Hour", "Last 6 Hours", "Last 24 Hours", "Last 7 Days"])
    with col3:
        refresh = st.button("🔄 REFRESH DATA", use_container_width=True)

    # Generate random vitals data
    def generate_vital_signs():
        return {
            "Heart Rate": random.randint(55, 95),
            "BP Systolic": random.randint(100, 140),
            "BP Diastolic": random.randint(60, 90),
            "SpO2": random.randint(92, 100),
            "Respiratory Rate": random.randint(12, 20),
            "Temperature": round(random.uniform(36.1, 37.5), 1)
        }

    # ============================================
    # METRIC CARDS (Top Row)
    # ============================================
    vitals = generate_vital_signs()
    
    m1, m2, m3, m4, m5, m6 = st.columns(6)
    
    with m1:
        st.metric("❤️ HEART RATE", f"{vitals['Heart Rate']} BPM", delta=f"{random.randint(-5,5)}")
    with m2:
        st.metric("🩸 BP", f"{vitals['BP Systolic']}/{vitals['BP Diastolic']}", delta="NOMINAL")
    with m3:
        color = "🟢" if vitals['SpO2'] >= 95 else "🟡" if vitals['SpO2'] >= 90 else "🔴"
        st.metric(f"{color} SpO₂", f"{vitals['SpO2']}%")
    with m4:
        st.metric("🌡️ TEMP", f"{vitals['Temperature']}°C")
    with m5:
        st.metric("🫁 RESP RATE", f"{vitals['Respiratory Rate']} /min")
    with m6:
        st.metric("📊 VITAL SCORE", f"{random.randint(85, 100)}%", delta="STABLE")

    st.markdown("---")

    # ============================================
    # GRAPH 1: HEART RATE TREND (Plotly)
    # ============================================
    st.markdown("<h3>❤️ HEART RATE TREND</h3>", unsafe_allow_html=True)
    
    # Generate time series data
    hours = list(range(24))
    hr_data = [random.randint(55, 95) for _ in range(24)]
    # Add some spikes for realism
    hr_data[10] = random.randint(100, 120)
    hr_data[14] = random.randint(100, 115)
    
    fig_hr = go.Figure()
    fig_hr.add_trace(go.Scatter(
        x=hours,
        y=hr_data,
        mode='lines+markers',
        line=dict(color='#00FFAA', width=2),
        marker=dict(size=6, color='#00FFAA', symbol='circle'),
        fill='tozeroy',
        fillcolor='rgba(0, 255, 170, 0.1)'
    ))
    
    fig_hr.update_layout(
        title=dict(text="HEART RATE VARIABILITY (HRV)", font=dict(color='#00C8FF', family='Orbitron')),
        xaxis=dict(title="Time (Hours)", gridcolor='rgba(255,255,255,0.1)', color='#A0AEC0'),
        yaxis=dict(title="Beats Per Minute (BPM)", gridcolor='rgba(255,255,255,0.1)', color='#A0AEC0'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        height=400
    )
    
    fig_hr.add_hline(y=85, line_dash="dash", line_color="#FFD700", annotation_text="Alert Threshold")
    fig_hr.add_hline(y=60, line_dash="dash", line_color="#FFD700")
    
    st.plotly_chart(fig_hr, use_container_width=True)

    # ============================================
    # TWO COLUMN GRAPHS (FIXED VERSION)
    # ============================================
    left, right = st.columns(2)
    
    with left:
        st.markdown("<h3>🫁 SpO₂ & RESPIRATION</h3>", unsafe_allow_html=True)
        
        # Dual axis graph
        time_points = list(range(24))
        spo2_data = [random.randint(92, 100) for _ in range(24)]
        resp_data = [random.randint(12, 20) for _ in range(24)]
        
        fig_dual = go.Figure()
        fig_dual.add_trace(go.Scatter(
            x=time_points, y=spo2_data, name="SpO₂ (%)",
            line=dict(color='#00C8FF', width=2), yaxis="y1"
        ))
        fig_dual.add_trace(go.Scatter(
            x=time_points, y=resp_data, name="Respiratory Rate (/min)",
            line=dict(color='#FFD700', width=2, dash='dot'), yaxis="y2"
        ))
        
        # FIXED: Removed 'titlefont', using proper nested dict
        fig_dual.update_layout(
            yaxis=dict(
                title=dict(text="SpO₂ (%)", font=dict(color='#00C8FF')),
                tickfont=dict(color='#00C8FF')
            ),
            yaxis2=dict(
                title=dict(text="Resp Rate", font=dict(color='#FFD700')),
                tickfont=dict(color='#FFD700'),
                overlaying='y',
                side='right'
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            height=350,
            legend=dict(font=dict(color='#A0AEC0'))
        )
        
        st.plotly_chart(fig_dual, use_container_width=True)
    
    with right:
        st.markdown("<h3>🩸 BLOOD PRESSURE TREND</h3>", unsafe_allow_html=True)
        
        # BP Gauge Chart
        systolic = vitals['BP Systolic']
        diastolic = vitals['BP Diastolic']
        
        fig_bp = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=systolic,
            title=dict(text="SYSTOLIC BP (mmHg)", font=dict(color='#FFD700', size=14)),
            delta=dict(reference=120, increasing=dict(color="red"), decreasing=dict(color="green")),
            gauge=dict(
                axis=dict(range=[80, 180], tickcolor='#00C8FF'),
                bar=dict(color='#00FFAA'),
                bgcolor='rgba(0,0,0,0.5)',
                borderwidth=1,
                bordercolor='#00C8FF',
                steps=[
                    dict(range=[80, 120], color='rgba(0,255,170,0.2)'),
                    dict(range=[120, 140], color='rgba(255,215,0,0.2)'),
                    dict(range=[140, 180], color='rgba(255,0,0,0.2)')
                ],
                threshold=dict(
                    line=dict(color="red", width=4),
                    thickness=0.75,
                    value=140
                )
            )
        ))
        
        fig_bp.update_layout(
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#00C8FF')
        )
        
        st.plotly_chart(fig_bp, use_container_width=True)

    st.markdown("---")

    # ============================================
    # AI INSIGHTS PANEL
    # ============================================
    st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius: 15px; padding: 20px; margin-top: 20px;'>
            <h3>🧠 AI MEDICAL INSIGHTS</h3>
        </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    
    insights = [
        ("✅", "Heart Rate Stable", "Normal sinus rhythm detected"),
        ("⚠️", "SpO₂ Alert", "Slight desaturation observed at 14:00"),
        ("📈", "BP Trend", "Systolic trending upward +5%")
    ]
    
    for i, (icon, title, desc) in enumerate(insights):
        with [col_a, col_b, col_c][i]:
            st.markdown(f"""
                <div style='background:rgba(0,0,0,0.5); border-radius:10px; padding:15px; margin:5px; border-left:3px solid #00C8FF;'>
                    <span style='font-size:24px'>{icon}</span>
                    <span style='color:#FFD700; font-weight:bold;'>{title}</span>
                    <p style='color:#A0AEC0; font-size:12px;'>{desc}</p>
                </div>
            """, unsafe_allow_html=True)
    
    # ============================================
    # WARNING SECTION (if any)
    # ============================================
    if vitals['SpO2'] < 94 or vitals['Heart Rate'] > 100:
        st.warning("""
        🚨 **MEDICAL ALERT** 🚨  
        - Abnormal vitals detected. Recommended immediate attention.
        - AI suggests additional monitoring.
        """)

    # Footer
    st.markdown("""
        <div style='text-align:center; padding:20px; background:rgba(0,0,0,0.3); border-radius:10px; margin-top:30px;'>
            <p style='color:#A0AEC0; font-size:11px;'>
                📡 DATA UPDATED IN REAL-TIME • EDGE PROCESSING ACTIVE • NO CLOUD STORAGE
            </p>
        </div>
    """, unsafe_allow_html=True)