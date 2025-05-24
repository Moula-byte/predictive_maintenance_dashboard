# Predictive Maintenance Dashboard

This project implements a predictive maintenance dashboard for industrial machines (Injection, Welding, Laser, Assembly) using sensor data. It leverages machine learning (Scikit-learn, PyTorch, SciPy) to predict equipment failures and visualizes results in a dashboard. Data is exported for interactive Tableau visualizations.

## Features
- **ML Models**: Random Forest (Scikit-learn) and MLP (PyTorch) predict failure probabilities.
- **Feature Engineering**: Rolling statistics, FFT (SciPy), PCA for dimensionality reduction.
- **Dashboard**: Visualizes vibration, temperature, and failure probability with thresholds.
- **Tableau Export**: CSV output for interactive stakeholder dashboards.

## Setup
1. **Prerequisites**:
   - Python 3.12
   - Install dependencies:
     ```bash
     pip install numpy pandas matplotlib seaborn scikit-learn scipy torch
     ```
2. **Run the Code**:
   - Execute the script to generate the dashboard image and CSV:
     ```bash
     python sensor_data_ml_dashboard.py
     ```
   - Outputs:
     - `sensor_ml_dashboard.png`: Dashboard with vibration, temperature, and failure probability plots.
     - `sensor_data.csv`: Data for Tableau visualization.

## Dashboard
The dashboard (`sensor_ml_dashboard.png`) includes:
1. **Vibration Plot**: Vibration levels (g) for four machines with thresholds (1.5, 2.0, 1.0, 1.8).
2. **Temperature Plot**: Temperatures (°C) with thresholds (300, 200, 150, 80).
3. **Failure Probability Plot**: ML-predicted failure likelihood (0-1) with a 30% threshold.

## Tableau Instructions
1. **Load Data**:
   - Open Tableau (Public/Desktop) and connect to `sensor_data.csv` (Text File).
2. **Create Worksheets**:
   - **Vibration**:
     - Drag `Time` (Continuous) to Columns, `Inj_Vibration`, `Weld_Vibration`, `Laser_Vibration`, `Assy_Vibration` to Rows.
     - Add reference lines at 1.5, 2.0, 1.0, 1.8 (Dashed, Red, 50% Opacity).
     - Title: "Vibration Across Machines", y-axis: "Vibration (g)".
   - **Temperature**:
     - Drag `Time` to Columns, `Inj_Temperature`, `Weld_Temperature`, `Laser_Temperature`, `Assy_Temperature` to Rows.
     - Add reference lines at 300, 200, 150, 80 (Dashed, Red, labeled).
     - Title: "Temperature Across Machines", y-axis: "Temperature (°C)".
   - **Failure Probability**:
     - Drag `Time` to Columns, `Failure_Probability` to Rows.
     - Add reference line at 0.3 (Dashed, Red, "Threshold (30%)").
     - Title: "Predicted Failure Probability", y-axis: "Probability", x-axis: "Time".
3. **Create Dashboard**:
   - Drag worksheets into a new dashboard (1500x1200 pixels).
   - Arrange vertically, add a `Time` filter, and enable tooltips.
   - Title: "Predictive Maintenance Dashboard".
4. **Publish (Optional)**:
   - Save to Tableau Public or Server for sharing.

## Files
- `sensor_data_ml_dashboard.py`: Main script for ML and dashboard generation.
- `sensor_ml_dashboard.png`: Generated dashboard image.
- `sensor_data.csv`: Data for Tableau.
- `.gitignore`: Excludes unnecessary files.
- `README.md`: This file.

## Notes
- Tested on May 23, 2025, 11:03 PM IST.
- For advanced Tableau analytics, install TabPy (`pip install tabpy`) and connect via localhost:9004.