import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from neurocat_sim.simulate_neurocat import simulate_neurocat

st.set_page_config(page_title="NeuroCat Simulator", layout="wide", page_icon="🐱")

st.markdown("""
# 🧠 NeuroCat: Cerebellar Hypoplasia Research Simulator  
Model motor coordination deficits in CH-affected cats using a simplified neural simulation.

This simulation is modeled after **real neurological principles** and CH research in animals.  
It allows users to explore how **brain signal disruption** and **neuroplastic adaptation** affect motor outcomes.
""")

# Sidebar – Parameters
with st.sidebar:
    st.header("🎛️ Simulation Settings")
    st.markdown("Adjust the sliders to match an observed CH severity and neural adaptation level.")
    condition = st.selectbox("Condition", ["CH"], index=0)
    severity = st.slider("CH Severity", 0.0, 1.0, 0.5)
    adaptation = st.slider("Adaptation (Neuroplasticity)", 0.0, 1.0, 0.3)
    signal_attempts = st.slider("Signal Attempts", 100, 2000, 1000)
    run_sim = st.button("🧪 Run Simulation")

# Simulation Output
if run_sim:
    result = simulate_neurocat(
        condition=condition,
        runs=signal_attempts,
        nodes=10,
        severity=severity,
        adaptation=adaptation
    )

    st.success("Simulation complete.")
    st.subheader("📊 Simulation Summary")
    st.json(result)

    with st.expander("🧬 Explanation of Metrics", expanded=True):
        st.markdown("""
- **Total Attempts**: Number of brain signals sent for movement.
- **Successful Signals**: Signals that successfully transmitted.
- **Accuracy**: Percentage of successful movement control.
- **Jitter Events**: Failed signals due to cerebellar disruption.
- **Average Node Failures**: Average number of 'broken' neurons per signal.
- **Severity**: How damaged the motor system is (closer to 1 = more severe).
- **Adaptation**: Brain’s learning flexibility to bypass broken nodes.
        """)

    # Graph
    df = pd.DataFrame({
        "Metric": ["Accuracy (%)", "Avg Node Failures"],
        "Value": [result["accuracy"] * 100, result["avg_node_failures"]],
    })

    fig, ax = plt.subplots()
    bars = ax.bar(df["Metric"], df["Value"], color=["#57D4FF", "#FF6A6A"])
    ax.set_ylabel("Value")
    ax.set_title("📉 Signal Coordination Metrics")
    ax.bar_label(bars, fmt="%.2f")
    st.pyplot(fig)

    # Personal Mapping
    st.markdown("### 🐾 Match Parameters to *Your* Cat")

    st.markdown("""
| **Parameter** | **Real-World Observation** | **How to Use It in Simulation** |
|---------------|----------------------------|----------------------------------|
| **CH Severity** | Mild to severe wobbliness, tremors, uncoordinated steps | 0.2–0.4 → Mild, 0.5–0.7 → Moderate, 0.8–1.0 → Severe |
| **Neuroplasticity** | Does your cat learn to jump or walk better over time? | If yes, increase adaptation (e.g. 0.6–0.9). If not, keep it low. |
| **Signal Attempts** | Simulate a task like walking or playing | 1000–2000 = more robust results |

This lets you **visualize how movement errors emerge** and what helps reduce them.
""", unsafe_allow_html=True)
