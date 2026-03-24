import streamlit as st
from physics import simulate_photon_stream, get_system_health
from protocol import encode_packet
from brain import AetherBrain
from charts import get_3d_vector_chart, get_channel_chart

def aether_login_system():
    """Initializes the secure gateway for Aether-Net."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.markdown("<h1 style='text-align: center;'>AETHER-NET MISSION CONTROL</h1>", unsafe_allow_html=True)
        st.warning("Hardware Status: Locked. Please authenticate to access 512GB SSD Telemetry.")
        
        # Security Credentials
        user_input = st.text_input("User ID", placeholder="Enter ID")
        pass_input = st.text_input("Security Key", type="password", placeholder="Enter Passcode")
        
        if st.button("Initialize Kernel"):
            # Credentials matching your requirement
            if user_input == "nerd" and pass_input == "arise":
                st.session_state["authenticated"] = True
                st.success("Access Granted. Synchronizing with DSN Node...")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Credentials. Access Denied.")
        return False
    return True

# --- GLOBAL SECURITY TRIGGER ---
if not aether_login_system():
    st.stop()



st.set_page_config(page_title="Aether-Net Dashboard", layout="wide", page_icon="🛰️")

if 'brain' not in st.session_state:
    st.session_state.brain = AetherBrain()

# Sidebar
st.sidebar.title("📡 Mission Control")
station = st.sidebar.selectbox("Active Ground Station", st.session_state.brain.stations)
weather = st.sidebar.radio("Atmospheric Condition", ["Clear", "Cloudy", "Stormy"])
dist = st.sidebar.slider("Distance (AU)", 0.1, 5.0, 1.2)
jitter = st.sidebar.slider("Pointing Jitter (µrad)", 0.0, 1.5, 0.3)

# Core Logic
data = simulate_photon_stream(dist, 250, weather)
health = get_system_health(data)
packet = encode_packet(data)
handover_needed, target_station = st.session_state.brain.check_handover_requirement(health, station)
ai_correction = st.session_state.brain.predict_correction(jitter, weather)

# UI Display
st.title("Aether-Net: AI-Adaptive Optical Protocol")
st.caption(f"System Mode: Professional Academic Presentation | DSN Node: {station}")

if handover_needed:
    st.error(f"🚨 SIGNAL CRITICAL: AI Initiating Handover to {target_station}")

# Metrics Row
m1, m2, m3, m4 = st.columns(4)
m1.metric("System Health", health)
m2.metric("Primary Channel", packet["primary_ch"])
m3.metric("Throughput", f"{packet['throughput_mhz']} MHz")
m4.metric("AI Correction", f"{ai_correction:.3f} µrad")

st.markdown("---")
cl, cr = st.columns([1, 1])

with cl:
    st.subheader("🛰️ 3D Beam Path Analysis")
    st.plotly_chart(get_3d_vector_chart(jitter + ai_correction), use_container_width=True)

with cr:
    st.subheader("📟 64-Channel Telemetry")
    st.plotly_chart(get_channel_chart(data), use_container_width=True)
