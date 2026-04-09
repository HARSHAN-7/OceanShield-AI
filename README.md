# OceanShield-AI
AI-powered maritime surveillance system that detects illegal fishing, smuggling, and suspicious vessel behavior using AIS data, anomaly detection, and real-time geospatial analytics.

# Project Overview

OceanShield AI is a maritime surveillance project aimed at detecting illegal, unreported, and unregulated (IUU) activities in ocean regions using vessel tracking data. The project focuses on:

Detecting anomalous vessel behavior
Identifying dark activity (ships turning off AIS signals)
Visualizing movement patterns using interactive maps

This solution leverages AI for anomaly detection, combined with data visualization for real-time actionable insights.

Hackathon Goal: Build a working prototype in 24 hours that processes AIS data, detects suspicious activity, and demonstrates it through a clear, interactive dashboard.

# Problem Statement

Illegal fishing, smuggling, and other unregulated maritime activities threaten economic stability, marine life, and national security. Traditional monitoring methods rely heavily on manual inspection or satellite imagery, which is slow and resource-intensive.

Project Objective:

Analyze AIS vessel tracking data to establish “normal” maritime behavior
Automatically flag vessels showing unusual patterns
Highlight dark activity and suspicious rendezvous points

# Dataset Details

We are using AIS data from the Kattegat Strait (Jan 1 – Mar 10, 2022).

Static Information (Ship Details)
IMO number, MMSI number, Call Sign, Name
Ship type, Width, Length, Draft
GPS device type, GPS offsets (bow/stern/port/starboard)
Dynamic Information (Movement Data)
Timestamp, Latitude, Longitude
Navigational status (Fishing, Anchored, etc.)
Speed Over Ground (SOG), Course Over Ground (COG), Heading
Rate of Turn (ROT), Port of Destination, ETA

✅ Why this dataset works:

Provides enough data for pattern recognition and anomaly detection
Includes time-stamped positional info to detect dark activity and unusual behavior

# Technical Workflow
Step 1 — Data Processing
Load AIS CSV into Pandas
Clean missing values
Convert timestamps to datetime
Sort by vessel_id and time
Step 2 — Suspicious Activity Detection
Use Isolation Forest (unsupervised ML) to detect anomalies in movement
Features: latitude, longitude, speed
Output: anomaly column → -1 = suspicious, 1 = normal
Step 3 — Dark Activity Detection
Compute time difference between consecutive messages per vessel
Flag vessels missing for > 2 hours
Output: dark_activity column → True = suspicious
Step 4 — Visualization
Use Folium to create an interactive map
Red markers = suspicious/dark vessels
Blue markers = normal vessels
Optionally, show vessel paths and clustering
Step 5 — Output
Tables: suspicious vessels, dark activity vessels
HTML Map: interactive visualization ready for demo

# Project Structure
OceanShield-AI/
├── data/
│   └── ais_data.csv             # AIS dataset
├── notebooks/
│   └── OceanShield_AI_Hackathon.ipynb  # Colab notebook
├── src/
│   ├── data_processing.py
│   ├── anomaly_detection.py
│   ├── dark_activity.py
│   └── map_visualization.py
├── README.md                    # Full project description & instructions
└── requirements.txt             # Required Python libraries

# Expected Outcomes
Detect suspicious vessels — any vessel behaving outside normal patterns
Detect dark activity — vessels turning off AIS signals
Visualize movements — interactive map to highlight patterns
Generate reports — tables of anomalies and dark activity for actionable insights

Hackathon Impact: Judges can instantly see AI detecting illegal or suspicious behavior with interactive visuals — very demo-friendly.

# Tech Stack
Python 3.10+
Data Analysis: Pandas, Numpy
Machine Learning: Scikit-Learn (Isolation Forest)
Visualization: Folium, Matplotlib, Seaborn
Notebook Platform: Google Colab (fast setup, free GPU)

# Future Enhancements
Integrate SAR imagery to detect missing/dark vessels
Expand to full EEZ coverage for real-world applicability
Add risk scoring for vessels to prioritize monitoring
Deploy Streamlit dashboard or web app for live demonstration
Include real-time alerts for anomalies

# How to Run (For Judges & GitHub Users)
Open notebooks/OceanShield_AI_Hackathon.ipynb in Google Colab
Upload ais_data.csv to Colab
Run cells step-by-step:
Data cleaning
Suspicious vessel detection
Dark activity detection
Map generation
Output:
Tables: suspicious vessels and dark activity vessels
Map: OceanShield_Map.html

# Why This Project Wins
Tackles a real-world, high-impact problem
Combines AI, data analysis, and visualization in one working demo
Interactive, actionable outputs for judges
Well-structured, modular code → professional presentation
