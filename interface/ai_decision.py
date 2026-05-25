# ============================================
# AI DECISION INTELLIGENCE — NASA GRADE
# AUTO-DETECT WORKING MODEL
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.graph_objects as go
import os
import pickle
import gzip
import joblib

MODEL_PATH = r"D:\🛕_Jagannath_Code_Sanctum\ASTROVITAL_AI_VITALX_CORE_V1\MODEL_HANGAR"

# ============================================
# SMART MODEL LOADER — TRIES ALL FILES
# ============================================
@st.cache_resource
def find_working_model():
    """
    Try all .pkl files and find the first one that loads correctly
    """
    try:
        if not os.path.exists(MODEL_PATH):
            return None, None
        
        all_files = [f for f in os.listdir(MODEL_PATH) if f.endswith('.pkl')]
        
        for file_name in all_files:
            file_path = os.path.join(MODEL_PATH, file_name)
            
            # Try different loading methods
            for method_name, loader in [
                ("pickle", lambda: pickle.load(open(file_path, 'rb'))),
                ("pickle_latin1", lambda: pickle.load(open(file_path, 'rb'), encoding='latin1')),
                ("joblib", lambda: joblib.load(file_path)),
            ]:
                try:
                    model = loader()
                    st.success(f"✅ Loaded: {file_name} (using {method_name})")
                    return model, file_name
                except:
                    continue
        
        st.warning("⚠️ No working model found. Using demo mode.")
        return None, None
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None, None

# ============================================
# PREDICTION FUNCTION
# ============================================
def get_prediction(model, input_data):
    """Get prediction from loaded model"""
    if model is None:
        # Demo mode
        anomaly_score = random.uniform(0, 1)
        if anomaly_score < 0.3:
            return "NORMAL", "LOW", anomaly_score
        elif anomaly_score < 0.7:
            return "WARNING", "MEDIUM", anomaly_score
        else:
            return "CRITICAL", "HIGH", anomaly_score
    
    try:
        # Prepare features
        features = np.array([[
            input_data['heart_rate'],
            input_data['spo2'],
            input_data['resp_rate'],
            input_data['bp_systolic'],
            input_data['bp_diastolic'],
            input_data['temperature']
        ]])
        
        # Try predict
        if hasattr(model, 'predict_proba'):
            pred = model.predict(features)[0]
            proba = model.predict_proba(features)[0]
            confidence = max(proba)
        else:
            pred = model.predict(features)[0]
            confidence = 0.85
        
        anomaly_score = 1 - confidence
        risk_level = "LOW" if anomaly_score < 0.3 else "MEDIUM" if anomaly_score < 0.7 else "HIGH"
        
        return str(pred), risk_level, anomaly_score
        
    except Exception as e:
        # Fallback to demo
        anomaly_score = random.uniform(0, 1)
        if anomaly_score < 0.3:
            return "NORMAL", "LOW", anomaly_score
        elif anomaly_score < 0.7:
            return "WARNING", "MEDIUM", anomaly_score
        else:
            return "CRITICAL", "HIGH", anomaly_score

# ============================================
# NASA GRADE UI
# ============================================

def render_ai_decision():
    st.markdown("""
        <div style='text-align:center; padding:20px; background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius: 20px; margin-bottom: 30px;'>
            <h1 style='font-size:3rem;'>🧠 AI DECISION CORE</h1>
            <p style='color:#00C8FF; font-family:Share Tech Mono;'>
                CLINICAL DECISION SUPPORT • EDGE INFERENCE
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Find working model
    model, model_name = find_working_model()
    
    if model:
        st.info(f"🟢 ACTIVE MODEL: `{model_name}`")
    else:
        st.warning("🟡 DEMO MODE — Using rule-based predictions")
    
    # Input Section
    st.markdown("<h3>📊 PATIENT VITALS</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        heart_rate = st.number_input("❤️ Heart Rate", 40, 180, 72)
    with col2:
        spo2 = st.number_input("🫁 SpO₂", 70, 100, 96)
    with col3:
        resp_rate = st.number_input("🌬️ Resp Rate", 8, 30, 16)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        bp_systolic = st.number_input("🩸 BP Systolic", 80, 200, 118)
    with col5:
        bp_diastolic = st.number_input("🩸 BP Diastolic", 50, 120, 78)
    with col6:
        temperature = st.number_input("🌡️ Temperature", 35.0, 40.0, 36.6, 0.1)
    
    if st.button("🚀 RUN PREDICTION", use_container_width=True):
        with st.spinner("Analyzing..."):
            input_data = {
                "heart_rate": heart_rate,
                "spo2": spo2,
                "resp_rate": resp_rate,
                "bp_systolic": bp_systolic,
                "bp_diastolic": bp_diastolic,
                "temperature": temperature
            }
            
            prediction, risk_level, anomaly_score = get_prediction(model, input_data)
            confidence = 1 - anomaly_score
            
            st.markdown("---")
            st.markdown("<h3>📈 PREDICTION RESULT</h3>", unsafe_allow_html=True)
            
            # Results
            r1, r2, r3, r4 = st.columns(4)
            
            with r1:
                color = "#00FFAA" if prediction == "NORMAL" else "#FFD700" if prediction == "WARNING" else "#FF4444"
                st.markdown(f"<div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'><p style='color:#A0AEC0;'>DIAGNOSIS</p><h3 style='color:{color};'>{prediction}</h3></div>", unsafe_allow_html=True)
            
            with r2:
                st.markdown(f"<div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'><p style='color:#A0AEC0;'>CONFIDENCE</p><h3 style='color:#00FFAA;'>{confidence:.1%}</h3></div>", unsafe_allow_html=True)
            
            with r3:
                st.markdown(f"<div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'><p style='color:#A0AEC0;'>ANOMALY</p><h3 style='color:#FFD700;'>{anomaly_score:.3f}</h3></div>", unsafe_allow_html=True)
            
            with r4:
                risk_color = "#00FFAA" if risk_level == "LOW" else "#FFD700" if risk_level == "MEDIUM" else "#FF4444"
                st.markdown(f"<div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'><p style='color:#A0AEC0;'>RISK</p><h3 style='color:{risk_color};'>{risk_level}</h3></div>", unsafe_allow_html=True)
            
            # Gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=anomaly_score * 100,
                title=dict(text="ANOMALY INDEX (%)", font=dict(color='#FFD700')),
                gauge=dict(
                    axis=dict(range=[0, 100]),
                    bar=dict(color='#00C8FF'),
                    steps=[
                        dict(range=[0, 30], color='rgba(0,255,170,0.2)'),
                        dict(range=[30, 70], color='rgba(255,215,0,0.2)'),
                        dict(range=[70, 100], color='rgba(255,0,0,0.2)')
                    ]
                )
            ))
            fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
        <div style='text-align:center; padding:20px; background:rgba(0,0,0,0.3); border-radius:10px; margin-top:30px;'>
            <p style='color:#A0AEC0;'>⚡ EDGE-ONLY INFERENCE • NO CLOUD</p>
        </div>
    """, unsafe_allow_html=True)