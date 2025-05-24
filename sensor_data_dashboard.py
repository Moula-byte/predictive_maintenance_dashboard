import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Simulate time series data (1 hour at 1-second intervals)
n_samples = 3600
time_index = [datetime.now() + timedelta(seconds=i) for i in range(n_samples)]

# 1. Injection Molding Machine Sensors
# Vibration (Accelerometer, RMS in g)
vibration_inj = np.random.normal(0.5, 0.1, n_samples)  # Normal: ~0.5g
vibration_inj[2000:2100] = np.random.normal(2.0, 0.3, 100)  # Anomaly: Spike to 2g
# Temperature (Thermocouple, °C)
temp_inj = np.random.normal(250, 10, n_samples)  # Normal: ~250°C
temp_inj[1500:1600] = np.random.normal(350, 15, 100)  # Overheating: >300°C
# Oil Level (Capacitive Sensor, %)
oil_inj = np.linspace(100, 95, n_samples) + np.random.normal(0, 0.5, n_samples)  # Gradual leak
# Pneumatic Pressure (Pressure Sensor, bar)
pressure_inj = np.random.normal(5, 0.2, n_samples)  # Normal: ~5 bar
pressure_inj[2500:2600] = np.random.normal(3, 0.2, 100)  # Failure: <4 bar
# Part Quality (Vision Sensor, defect rate %)
quality_inj = np.random.normal(2, 0.5, n_samples)  # Normal: ~2% defects
quality_inj[3000:3100] = np.random.normal(10, 1, 100)  # Spike: 10% defects

# 2. Vibration Welding Machine Sensors
vibration_weld = np.random.normal(0.8, 0.15, n_samples)  # Normal: ~0.8g
vibration_weld[1800:1900] = np.random.normal(3.0, 0.4, 100)  # Anomaly: Spike to 3g
temp_weld = np.random.normal(150, 5, n_samples)  # Normal: ~150°C
temp_weld[2200:2300] = np.random.normal(50, 5, 100)  # Temperature drop
oil_weld = np.linspace(100, 98, n_samples) + np.random.normal(0, 0.3, n_samples)  # Leak
pressure_weld = np.random.normal(6, 0.2, n_samples)  # Normal: ~6 bar
pressure_weld[2700:2800] = np.random.normal(4, 0.2, 100)  # Failure: <5 bar
quality_weld = np.random.normal(1.5, 0.4, n_samples)  # Normal: ~1.5% defects
quality_weld[3200:3300] = np.random.normal(8, 1, 100)  # Spike: 8% defects

# 3. Laser Weakening System Sensors
vibration_laser = np.random.normal(0.3, 0.05, n_samples)  # Normal: ~0.3g
vibration_laser[1900:2000] = np.random.normal(1.5, 0.2, 100)  # Anomaly: Spike to 1.5g
temp_laser = np.random.normal(100, 5, n_samples)  # Normal: ~100°C
temp_laser[2300:2400] = np.random.normal(200, 10, 100)  # Overheating: >150°C
oil_laser = np.linspace(100, 99, n_samples) + np.random.normal(0, 0.2, n_samples)  # Leak
pressure_laser = np.random.normal(4, 0.1, n_samples)  # Normal: ~4 bar
pressure_laser[2600:2700] = np.random.normal(2, 0.1, 100)  # Failure: <3 bar
quality_laser = np.random.normal(0.5, 0.1, n_samples)  # Normal: ~0.5% defects
quality_laser[3100:3200] = np.random.normal(5, 0.5, 100)  # Spike: 5% defects

# 4. Assembly Line Sensors
vibration_assy = np.random.normal(0.6, 0.1, n_samples)  # Normal: ~0.6g
vibration_assy[2100:2200] = np.random.normal(2.5, 0.3, 100)  # Anomaly: Spike to 2.5g
temp_assy = np.random.normal(60, 5, n_samples)  # Normal: ~60°C
temp_assy[2400:2500] = np.random.normal(100, 5, 100)  # Overheating: >80°C
oil_assy = np.linspace(100, 96, n_samples) + np.random.normal(0, 0.4, n_samples)  # Leak
pressure_assy = np.random.normal(7, 0.2, n_samples)  # Normal: ~7 bar
pressure_assy[2800:2900] = np.random.normal(4, 0.2, 100)  # Failure: <5 bar
quality_assy = np.random.normal(1, 0.3, n_samples)  # Normal: ~1% defects
quality_assy[3300:3400] = np.random.normal(7, 0.7, 100)  # Spike: 7% defects

# Create DataFrame
data = pd.DataFrame({
    'Time': time_index,
    'Inj_Vibration': vibration_inj, 'Inj_Temperature': temp_inj, 'Inj_Oil': oil_inj,
    'Inj_Pressure': pressure_inj, 'Inj_Quality': quality_inj,
    'Weld_Vibration': vibration_weld, 'Weld_Temperature': temp_weld, 'Weld_Oil': oil_weld,
    'Weld_Pressure': pressure_weld, 'Weld_Quality': quality_weld,
    'Laser_Vibration': vibration_laser, 'Laser_Temperature': temp_laser, 'Laser_Oil': oil_laser,
    'Laser_Pressure': pressure_laser, 'Laser_Quality': quality_laser,
    'Assy_Vibration': vibration_assy, 'Assy_Temperature': temp_assy, 'Assy_Oil': oil_assy,
    'Assy_Pressure': pressure_assy, 'Assy_Quality': quality_assy
})

# Create a multi-panel dashboard
plt.figure(figsize=(15, 20))
sns.set_style("whitegrid")

# Plot 1: Vibration
plt.subplot(5, 1, 1)
for col in ['Inj_Vibration', 'Weld_Vibration', 'Laser_Vibration', 'Assy_Vibration']:
    plt.plot(data['Time'], data[col], label=col)
plt.axhline(y=1.5, color='r', linestyle='--', label='Vibration Threshold (1.5g)')
plt.title('Vibration Across Machines')
plt.ylabel('Vibration (g)')
plt.legend()
plt.xticks(rotation=45)

# Plot 2: Temperature
plt.subplot(5, 1, 2)
for col in ['Inj_Temperature', 'Weld_Temperature', 'Laser_Temperature', 'Assy_Temperature']:
    plt.plot(data['Time'], data[col], label=col)
plt.axhline(y=300, color='r', linestyle='--', label='Overheating Threshold (300°C)')
plt.title('Temperature Across Machines')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.xticks(rotation=45)

# Plot 3: Oil Level
plt.subplot(5, 1, 3)
for col in ['Inj_Oil', 'Weld_Oil', 'Laser_Oil', 'Assy_Oil']:
    plt.plot(data['Time'], data[col], label=col)
plt.axhline(y=95, color='r', linestyle='--', label='Low Oil Threshold (95%)')
plt.title('Oil Level Across Machines')
plt.ylabel('Oil Level (%)')
plt.legend()
plt.xticks(rotation=45)

# Plot 4: Pneumatic Pressure
plt.subplot(5, 1, 4)
for col in ['Inj_Pressure', 'Weld_Pressure', 'Laser_Pressure', 'Assy_Pressure']:
    plt.plot(data['Time'], data[col], label=col)
plt.axhline(y=4, color='r', linestyle='--', label='Low Pressure Threshold (4 bar)')
plt.title('Pneumatic Pressure Across Machines')
plt.ylabel('Pressure (bar)')
plt.legend()
plt.xticks(rotation=45)

# Plot 5: Part Quality
plt.subplot(5, 1, 5)
for col in ['Inj_Quality', 'Weld_Quality', 'Laser_Quality', 'Assy_Quality']:
    plt.plot(data['Time'], data[col], label=col)
plt.axhline(y=5, color='r', linestyle='--', label='Defect Threshold (5%)')
plt.title('Part Quality (Defect Rate) Across Machines')
plt.ylabel('Defect Rate (%)')
plt.xlabel('Time')
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('sensor_dashboard.png')