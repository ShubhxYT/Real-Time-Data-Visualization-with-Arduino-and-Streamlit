# Real-Time Data Visualization with Arduino and Streamlit
> ![Python](https://img.shields.io/badge/Python-3.x-blue) | Live environmental sensor dashboard with gauge charts, time-series plots, and ultrasonic radar — dual Arduino + Streamlit

## What I Built It For
I genuinely don't remember exactly why I built this. It was late 2022 or early 2023 — four years ago. What I do remember: an Arduino reading sensors, Python parsing serial output, and Streamlit turning it all into live gauges on a web dashboard. This was my first time using Streamlit, and it felt like cheating — write Python, get a web dashboard. No HTML, no CSS, no JavaScript. The radar plot used matplotlib blitting for smooth real-time animation, which was genuinely clever for someone who'd never done real-time visualization before. I pushed it to GitHub nearly two years later in November 2024. Some projects don't need a reason.

## Features
- 4 live gauge charts (Plotly) for gas, humidity, temperature, and TDS water quality
- 4 time-series line plots (Matplotlib) with rolling 25-second windows
- Ultrasonic radar visualization — polar plot with sweeping line indicator and blit-based rendering for smooth animation
- Laser security system control panel — ON/OFF via second Arduino
- RFID gate access system with authorized/unauthorized status display
- Dual Arduino architecture — one for sensors, one for actuators

## Architecture
Four layers working together:

```
Arduino Firmware → Python Serial Bridge → Data Processing → Streamlit Dashboard
       ↑                                                    ↑
  Servo + ultrasonic sweep                          Plotly gauges + Matplotlib plots
  DHT11 + MQ gas + TDS                              Radar polar visualization
```

The Arduino sweeps a servo-mounted ultrasonic sensor from 5° to 165° while simultaneously reading DHT11 (temp/humidity), MQ gas sensor, and TDS water quality sensor. All readings stream over serial at 9600 baud as comma-separated key-value pairs. Python parses the stream, maintains rolling data windows, and feeds values to Streamlit. A second Arduino on a separate COM port handles laser and RFID gate commands.

## Tech Stack
| Component | Technology |
|-----------|-----------|
| Firmware | Arduino C++ (DHT library, Servo library) |
| Serial bridge | Python 3, PySerial |
| Dashboard | Streamlit |
| Gauges | Plotly (go.Indicator) |
| Line plots & radar | Matplotlib (blit-based polar projection) |
| Hardware | Arduino Uno/Nano, DHT11, MQ gas sensor, TDS sensor, HC-SR04 ultrasonic, servo |

## Setup & Usage
### Prerequisites
- Python 3.7+
- Arduino IDE (to upload firmware)
- Physical hardware: Arduino, DHT11, MQ gas sensor, TDS sensor, HC-SR04, servo motor

### Installation
```
git clone https://github.com/ShubhxYT/Real-Time-Data-Visualization-with-Arduino-and-Streamlit.git
cd Real-Time-Data-Visualization-with-Arduino-and-Streamlit
pip install streamlit plotly matplotlib pyserial
```

### Running
1. Upload `radar_dht_gas_water.ino` to your Arduino
2. Connect Arduino via USB (default: COM9 for sensors, COM10 for control)
3. Launch the dashboard:
```
streamlit run main.py
```
4. Open http://localhost:8501 in your browser
5. Use the sidebar to switch between Graphs view, Radar view, Laser controls, and Gate controls

## Project Structure
```
├── radar_dht_gas_water.ino   # Arduino firmware — sensor reading + servo sweep
├── arduino.py                # Python serial communication layer
├── radar.py                  # Real-time polar radar visualization (Matplotlib blit)
└── main.py                   # Streamlit dashboard — gauges, plots, controls
```
