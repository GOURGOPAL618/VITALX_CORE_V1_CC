# ============================================
# MISSION CONTROL DASHBOARD — HOME
# AstroVital JCC V2.0 | NASA Grade
# ============================================

import streamlit as st
import pandas as pd
import random
from datetime import datetime

def render_home():
    # Mission Header
    st.markdown("""
        <div style='text-align:center; padding:20px; background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius: 20px; margin-bottom: 30px;'>
            <h1 style='font-size:3rem;'>🛸 MISSION CONTROL</h1>
            <p style='color:#00C8FF; font-family:Share Tech Mono;'>
                ACTIVE MISSION • REAL-TIME TELEMETRY • EDGE DEPLOYMENT
            </p>
            <p style='color:#FFD700; font-size:14px;'>
                🟢 SYSTEM NOMINAL | 🛰️ ALL SYSTEMS GO
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Mission Time Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🕐 MISSION ELAPSED",
            value=f"{random.randint(100, 500)} DAYS",
            delta="ACTIVE"
        )
    
    with col2:
        st.metric(
            label="📡 SIGNAL STRENGTH",
            value=f"{random.randint(85, 99)}%",
            delta="NOMINAL"
        )
    
    with col3:
        st.metric(
            label="⚡ POWER USAGE",
            value=f"{random.randint(40, 75)} kW",
            delta="-2%"
        )
    
    with col4:
        st.metric(
            label="💾 DATA STORAGE",
            value=f"{random.randint(45, 80)}%",
            delta="EDGE ONLY"
        )
    
    st.markdown("---")
    
    # Two Column Layout
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.markdown("""
            <div style='background: rgba(0,200,255,0.05); border-radius: 15px; padding: 20px;'>
                <h3>🎯 MISSION OBJECTIVES</h3>
                <ul style='color:#E0E0E0; font-family:Share Tech Mono;'>
                    <li>✅ Real-time health monitoring</li>
                    <li>✅ AI-powered anomaly detection</li>
                    <li>✅ Edge-only data processing</li>
                    <li>✅ Zero cloud dependency</li>
                    <li>✅ 99.9% system uptime</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        # System Health Cards
        st.markdown("### 🩺 SYSTEM HEALTH")
        
        health_metrics = {
            "CPU": random.randint(30, 70),
            "RAM": random.randint(40, 80),
            "STORAGE": random.randint(50, 85),
            "NETWORK": random.randint(70, 95)
        }
        
        for component, value in health_metrics.items():
            color = "#00FFAA" if value < 70 else "#FFD700" if value < 85 else "#FF4444"
            st.markdown(f"""
                <div style='margin:10px 0;'>
                    <span style='color:#A0AEC0'>{component}</span>
                    <div style='background:rgba(255,255,255,0.1); border-radius:10px; height:8px;'>
                        <div style='background:{color}; width:{value}%; height:8px; border-radius:10px;'></div>
                    </div>
                    <span style='color:{color}'>{value}%</span>
                </div>
            """, unsafe_allow_html=True)
    
    with right_col:
        st.markdown("""
            <div style='background: rgba(255,215,0,0.05); border-radius: 15px; padding: 20px;'>
                <h3>🚀 RECENT ACTIVITY</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # Recent Events
        events = [
            ("🟢", "System check completed", "Just now"),
            ("📡", "Telemetry data received", "2 min ago"),
            ("🧠", "AI decision executed", "5 min ago"),
            ("💾", "Data backup successful", "10 min ago"),
            ("⚙️", "Health monitor active", "15 min ago")
        ]
        
        for icon, event, time in events:
            st.markdown(f"""
                <div style='display:flex; justify-content:space-between; padding:10px; border-bottom:1px solid rgba(0,200,255,0.1);'>
                    <span>{icon} {event}</span>
                    <span style='color:#A0AEC0; font-size:12px;'>{time}</span>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Quick Stats
        st.markdown("### 📊 QUICK STATS")
        stats = {
            "Total Patients Monitored": random.randint(100, 500),
            "AI Predictions Made": random.randint(500, 2000),
            "Anomalies Detected": random.randint(5, 50),
            "System Health Score": f"{random.randint(92, 99)}%"
        }
        
        for label, value in stats.items():
            st.markdown(f"""
                <div style='display:flex; justify-content:space-between; padding:5px;'>
                    <span style='color:#A0AEC0'>{label}</span>
                    <span style='color:#00FFAA; font-weight:bold;'>{value}</span>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
        <div style='text-align:center; padding:20px; background:rgba(0,0,0,0.3); border-radius:10px;'>
            <p style='color:#A0AEC0; font-size:11px;'>
                🔴 NO CLOUD CONNECTION • ALL DATA PROCESSED LOCALLY • EDGE MODE ACTIVE
            </p>
            <p style='color:#FFD700; font-size:11px;'>
                "Because Every Heartbeat in Space Matters."
            </p>
        </div>
    """, unsafe_allow_html=True)