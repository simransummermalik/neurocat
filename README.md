#  NeuroCat: A Simulation of Motor Coordination Disruption from Cerebellar Hypoplasia in Felines

**By SUMMER MALIK**  
Student @University of North Carolina at Charlotte  
Department of Biological Sciences × Computer Science
Created for my Animal Physiology Course

---

## Overview

**NeuroCat** is a probabilistic neural modeling tool that simulates motor coordination failure in cats affected by **Cerebellar Hypoplasia (CH)** — a congenital neurological disorder impairing cerebellar development and fine motor control. The tool leverages **Monte Carlo simulation**, **Bernoulli trial modeling**, and core concepts from **neurophysiology** and **fault-tolerant system theory** to visualize how disrupted neural pathways translate into observable motor dysfunction.

NeuroCat enables interactive manipulation of biological parameters like **damage severity** and **neuroplastic adaptation** to explore the fragile balance between breakdown and compensation in real-world motor systems.

---

## The Purpose

This project is designed to:

- Demonstrate how cerebellar underdevelopment disrupts motor reliability  
- Illustrate the compensatory role of **neuroplasticity** in signal routing  
- Provide a quantitative simulation inspired by real neurological architecture  
- Bridge neuroscience and computational modeling for educational and research purposes  

It serves as a visual and analytical tool for understanding CH through the lens of **probabilistic failure modeling**.

---

## Biological Background

Cerebellar Hypoplasia is a congenital condition in which the **cerebellum** ;a key structure involved in posture, balance, and voluntary movement precision ; is underdeveloped or malformed. While sensory perception and cognition remain largely unaffected, cerebellar dysfunction results in:

- **Ataxia** (wobbly or uncoordinated gait)  
- **Tremors**, especially during intentional movement  
- **Hypermetria**, **jerky limb motion**, and impaired balance  
- Difficulty in postural stabilization and motor targeting  

CH is often linked to prenatal infections (e.g. *feline panleukopenia virus*) that disrupt neurogenesis in the rapidly developing cerebellum. Although non-progressive and painless, its symptoms are lifelong.

---

## Simulation Design

The simulation represents the motor signal pathway as a linear sequence of **neural nodes** — abstracted synapses, axon bundles, or integration units — that a brain-generated command must traverse to reach muscles.

Each node has a **probability of failure** computed as:

\[
P_{\text{fail}} = \text{Severity} \times (1 - \text{Adaptation})
\]

- **Severity** reflects the extent of cerebellar damage.  
- **Adaptation** reflects the brain’s capacity for **neuroplastic rerouting** — compensating for damaged paths.

A single motor command is successful only if **all nodes succeed**. If any node fails, the result is a **jitter event** — an uncoordinated motor output. The simulation executes this process over many trials (default: 1000–2000), collecting statistical results on coordination reliability.

---

## Output Metrics

| Metric | Description |
|--------|-------------|
| `accuracy` | Ratio of successful motor signals (clean coordination) |
| `jitter_events` | Total trials where at least one node failed |
| `avg_node_failures` | Mean number of failed nodes per motor attempt |
| `severity` | Input severity level (0–1) |
| `adaptation` | Input plasticity level (0–1) |

These are visualized in bar graphs to help intuitively compare outcomes across different neurological states.

---

## The Math Behind It

This simulation uses **Bernoulli trials** to model each neural node’s pass/fail state across a signal path.

### Model:
Let:

- \( n \) = number of nodes (e.g. 10)  
- \( r \) = number of signal attempts (e.g. 1000)  
- \( p = \text{severity} \times (1 - \text{adaptation}) \)

Then each node \( X_i \sim \text{Bernoulli}(p) \), and a signal attempt is only successful if:

\[
\sum_{i=1}^{n} X_i = 0
\]

This simulates **complete signal transmission**, and all other outcomes are categorized as **failures or jitter**.

---

## Technologies Used

- **Python 3.11**  
- **Streamlit** – interactive UI for simulation control  
- **Matplotlib** – dynamic plotting of signal metrics  
- **Random module** – probabilistic trial generation  

---

## Research Context

This tool reflects foundational themes in:

| Field | Concept Modeled |
|-------|------------------|
| **Neuroscience** | Synaptic disruption, motor pathway failure |
| **Neuroplasticity** | Adaptive rerouting of neural signals |
| **Reliability Theory** | Node failure and redundancy |
| **Biomedical Computing** | Signal simulation under stochastic constraints |
| **Animal Physiology** | Realistic modeling of coordination pathology |

It also parallels broader work in:

- Feline neurodevelopment research  
- Pediatric cerebellar disorder modeling  
- Computational tools for behavioral neuroscience  
- Sensorimotor impairment in post-spaceflight rehabilitation (NASA studies)

---

## Career Tie-In

As a student of **Computer Science** with a strong focus on **bioinformatics**, **biomedical modeling**, and **aerospace physiology**, this project represents a convergence of scientific communication, neuroscience, and systems thinking.

I plan to expand this style of research-simulation integration toward future work in **NASA's Human Research Program**, **cognitive resilience modeling**, or **adaptive control systems** in both human and animal studies.

---

---

## 🧪 To Run the Simulation
install the dependences in requirements.txt and then-

```bash
streamlit run neurocat_app.py
