# ============================================
# DATA RECORDS — MISSION DATABASE
# AstroVital JCC V2.0 | Patient Records & History
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# ============================================
# GENERATE SAMPLE DATA (tu actual DB se replace kar sakta hai)
# ============================================
def generate_sample_data(n=50):
    """Generate realistic patient records"""
    patients = []
    crew_ids = [f"CREW-{i:03d}" for i in range(1, n+1)]
    
    statuses = ["🟢 NORMAL", "🟡 WARNING", "🔴 CRITICAL"]
    conditions = ["Stable", "Monitoring", "Follow-up", "Emergency", "Routine Check"]
    
    for i, crew_id in enumerate(crew_ids):
        record = {
            "Timestamp": (datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))).strftime("%Y-%m-%d %H:%M:%S"),
            "Crew ID": crew_id,
            "Heart Rate (BPM)": random.randint(55, 95),
            "SpO₂ (%)": random.randint(92, 100),
            "Resp Rate (/min)": random.randint(12, 20),
            "BP Systolic": random.randint(100, 140),
            "BP Diastolic": random.randint(60, 90),
            "Temperature (°C)": round(random.uniform(36.1, 37.5), 1),
            "Status": random.choices(statuses, weights=[0.7, 0.2, 0.1])[0],
            "Condition": random.choice(conditions),
            "AI Risk Score": round(random.uniform(0, 1), 3)
        }
        patients.append(record)
    
    return pd.DataFrame(patients)

# ============================================
# STATS CARDS
# ============================================
def show_stats_cards(df):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'>
                <p style='color:#A0AEC0;'>📊 TOTAL RECORDS</p>
                <h2 style='color:#00FFAA;'>{len(df)}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        normal_count = len(df[df['Status'] == "🟢 NORMAL"])
        st.markdown(f"""
            <div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'>
                <p style='color:#A0AEC0;'>🟢 NORMAL</p>
                <h2 style='color:#00FFAA;'>{normal_count}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        warning_count = len(df[df['Status'] == "🟡 WARNING"])
        st.markdown(f"""
            <div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'>
                <p style='color:#A0AEC0;'>🟡 WARNING</p>
                <h2 style='color:#FFD700;'>{warning_count}</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        critical_count = len(df[df['Status'] == "🔴 CRITICAL"])
        st.markdown(f"""
            <div style='text-align:center; background:rgba(0,200,255,0.1); border-radius:15px; padding:15px;'>
                <p style='color:#A0AEC0;'>🔴 CRITICAL</p>
                <h2 style='color:#FF4444;'>{critical_count}</h2>
            </div>
        """, unsafe_allow_html=True)

# ============================================
# COLOR STATUS FUNCTION (FIXED)
# ============================================
def color_status(val):
    """Return color for status text"""
    if "NORMAL" in str(val):
        return '#00FFAA'
    elif "WARNING" in str(val):
        return '#FFD700'
    elif "CRITICAL" in str(val):
        return '#FF4444'
    return '#A0AEC0'

# ============================================
# MAIN RENDER FUNCTION
# ============================================
def render_data_records():
    # Header
    st.markdown("""
        <div style='text-align:center; padding:20px; background: linear-gradient(135deg, rgba(0,200,255,0.1), rgba(0,0,0,0.3)); border-radius: 20px; margin-bottom: 30px;'>
            <h1 style='font-size:3rem;'>💾 DATA RECORDS</h1>
            <p style='color:#00C8FF; font-family:Share Tech Mono;'>
                PATIENT DATABASE • HISTORICAL DATA • EDGE STORAGE
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Load data (cached)
    @st.cache_data
    def load_data():
        return generate_sample_data(100)
    
    df = load_data()
    
    # Stats
    show_stats_cards(df)
    st.markdown("---")
    
    # ============================================
    # FILTERS SECTION
    # ============================================
    st.markdown("<h3>🔍 FILTER PATIENT DATA</h3>", unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    
    with col_f1:
        crew_filter = st.multiselect(
            "👨‍🚀 Crew ID",
            options=df['Crew ID'].unique(),
            default=[]
        )
    
    with col_f2:
        status_filter = st.multiselect(
            "🩺 Status",
            options=df['Status'].unique(),
            default=[]
        )
    
    with col_f3:
        hr_min, hr_max = st.slider(
            "❤️ Heart Rate Range",
            min_value=int(df['Heart Rate (BPM)'].min()),
            max_value=int(df['Heart Rate (BPM)'].max()),
            value=(60, 85)
        )
    
    with col_f4:
        spo2_min, spo2_max = st.slider(
            "🫁 SpO₂ Range",
            min_value=int(df['SpO₂ (%)'].min()),
            max_value=int(df['SpO₂ (%)'].max()),
            value=(94, 100)
        )
    
    # Apply filters
    filtered_df = df.copy()
    
    if crew_filter:
        filtered_df = filtered_df[filtered_df['Crew ID'].isin(crew_filter)]
    if status_filter:
        filtered_df = filtered_df[filtered_df['Status'].isin(status_filter)]
    
    filtered_df = filtered_df[
        (filtered_df['Heart Rate (BPM)'] >= hr_min) &
        (filtered_df['Heart Rate (BPM)'] <= hr_max) &
        (filtered_df['SpO₂ (%)'] >= spo2_min) &
        (filtered_df['SpO₂ (%)'] <= spo2_max)
    ]
    
    st.caption(f"📌 Showing {len(filtered_df)} of {len(df)} records")
    
    # ============================================
    # DATA TABLE (Styled with HTML)
    # ============================================
    st.markdown("---")
    st.markdown("<h3>📋 PATIENT RECORDS</h3>", unsafe_allow_html=True)
    
    # Display dataframe with custom formatting
    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400,
        column_config={
            "Timestamp": st.column_config.DatetimeColumn("Timestamp"),
            "Heart Rate (BPM)": st.column_config.NumberColumn("❤️ Heart Rate", format="%d BPM"),
            "SpO₂ (%)": st.column_config.NumberColumn("🫁 SpO₂", format="%d %%"),
            "Status": st.column_config.TextColumn("🩺 Status"),
            "AI Risk Score": st.column_config.ProgressColumn(
                "🤖 AI Risk", 
                format="%.2f", 
                min_value=0, 
                max_value=1,
                help="AI-predicted risk level (0=low, 1=high)"
            )
        }
    )
    
    # ============================================
    # EXPORT OPTIONS
    # ============================================
    st.markdown("---")
    col_e1, col_e2, col_e3 = st.columns([1, 1, 2])
    
    with col_e1:
        if st.button("📥 Export as CSV", use_container_width=True):
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name=f"astrovital_records_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    
    with col_e2:
        if st.button("🖨️ Print Report", use_container_width=True):
            st.info("📄 Report ready — use browser print (Ctrl+P)")
    
    # ============================================
    # DATA VISUALIZATION
    # ============================================
    st.markdown("---")
    st.markdown("<h3>📊 DATA INSIGHTS</h3>", unsafe_allow_html=True)
    
    col_v1, col_v2 = st.columns(2)
    
    with col_v1:
        # Status Distribution
        status_counts = filtered_df['Status'].value_counts()
        fig_pie = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Patient Status Distribution",
            color_discrete_map={
                "🟢 NORMAL": "#00FFAA",
                "🟡 WARNING": "#FFD700",
                "🔴 CRITICAL": "#FF4444"
            }
        )
        fig_pie.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#A0AEC0'),
            title_font=dict(color='#00C8FF')
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col_v2:
        # Heart Rate vs SpO2 Scatter
        fig_scatter = px.scatter(
            filtered_df,
            x='Heart Rate (BPM)',
            y='SpO₂ (%)',
            color='Status',
            title="Heart Rate vs SpO₂ Correlation",
            color_discrete_map={
                "🟢 NORMAL": "#00FFAA",
                "🟡 WARNING": "#FFD700",
                "🔴 CRITICAL": "#FF4444"
            }
        )
        fig_scatter.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#A0AEC0'),
            title_font=dict(color='#00C8FF')
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # ============================================
    # SEARCH FUNCTION
    # ============================================
    st.markdown("---")
    st.markdown("<h3>🔎 SEARCH PATIENT HISTORY</h3>", unsafe_allow_html=True)
    
    search_term = st.text_input("Search by Crew ID or Condition", placeholder="e.g., CREW-001 or Stable")
    
    if search_term:
        search_results = filtered_df[
            filtered_df['Crew ID'].str.contains(search_term, case=False) |
            filtered_df['Condition'].str.contains(search_term, case=False)
        ]
        st.success(f"🔍 Found {len(search_results)} matching records")
        st.dataframe(search_results, use_container_width=True)
    
    # ============================================
    # STORAGE INFO
    # ============================================
    st.markdown("---")
    st.markdown("""
        <div style='background:rgba(0,0,0,0.3); border-radius:10px; padding:15px; margin-top:20px;'>
            <div style='display:flex; justify-content:space-between;'>
                <span style='color:#A0AEC0;'>💾 EDGE STORAGE STATUS</span>
                <span style='color:#00FFAA;'>✅ ACTIVE</span>
            </div>
            <div style='background:rgba(255,255,255,0.1); border-radius:5px; height:8px; margin:10px 0;'>
                <div style='background:#00C8FF; width:42%; height:8px; border-radius:5px;'></div>
            </div>
            <div style='display:flex; justify-content:space-between;'>
                <span style='color:#A0AEC0;'>Used: 42.3 GB</span>
                <span style='color:#A0AEC0;'>Free: 57.7 GB</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div style='text-align:center; padding:20px; background:rgba(0,0,0,0.3); border-radius:10px; margin-top:30px;'>
            <p style='color:#A0AEC0; font-size:11px;'>
                📡 ALL DATA STORED LOCALLY • EDGE DATABASE ACTIVE • NO CLOUD SYNC
            </p>
        </div>
    """, unsafe_allow_html=True)