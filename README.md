# Satellite Orbit Visualizer 🌍🛰️

A physics-consistent, real-time satellite orbit visualization system built using live Two-Line Element (TLE) data.  
This project simulates and animates the orbital motion of Earth-orbiting satellites around a realistically rendered Earth using a professional scientific computing workflow in Python.

The system demonstrates how real satellite tracking pipelines combine orbital mechanics, time-based propagation, and scientific visualization — following principles used in space research, Earth observation, and mission analysis.


## 🚀 Project Motivation

Satellites are fundamental to modern science and society, enabling:
- Earth observation and climate monitoring  
- Space situational awareness  
- Navigation and communication systems  

However, satellite orbits are often treated as abstract data rather than dynamic physical systems.  
This project was built to **bridge raw orbital data with intuitive, physics-aware visualization**, allowing users to see and understand satellite motion in a realistic Earth-centered reference frame.


## 🛰️ Key Features

- **Real satellite orbit propagation** using official Two-Line Element (TLE) data  
- **Live TLE fetching** from authoritative public sources  
- **Time-accurate orbital simulation**  
- **3D Earth rendering** with correct planetary scale  
- **Smooth animated satellite motion**  
- **Dark-space scientific visualization style**  
- **Clean VS Code–based development workflow (no notebooks)**  

## 🌍 Data Source

- **CelesTrak** — Publicly available Two-Line Element (TLE) sets  
  - Used globally by space agencies, observatories, and satellite tracking systems  
  - Provides continuously updated orbital parameters  

Live TLE retrieval ensures that each execution reflects the satellite’s most recent orbital state.

## 🧠 Technical Overview

The system follows a realistic satellite analysis pipeline:

1. **Retrieve live TLE data** for the target satellite  
2. **Propagate the orbit** using precise time-based calculations  
3. **Compute Earth-centered inertial coordinates**  
4. **Render Earth as a 3D sphere** at correct physical scale  
5. **Animate the satellite trajectory** to reflect continuous orbital motion  

While simplified for clarity, this workflow mirrors the core logic used in professional satellite mission analysis tools.

## 🛠️ Tech Stack

- **Python**  
- **Skyfield** — orbital mechanics and ephemeris calculations  
- **NumPy** — numerical computation  
- **Matplotlib** — 3D visualization and animation  
- **Requests** — live data retrieval  

The project intentionally avoids notebook-based workflows to reflect production-style development practices.

## 📁 Project Structure
satellite-orbit-visualizer/
├── main.py
├── requirements.txt
├── README.md
├── assets/
│ └── demo.gif
└── .gitignore

