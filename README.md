# Computational-Physics
🌍☀️🪐 Orbital Simulation: What If Jupiter Were 100x Bigger?
🔭 Project Overview
This project simulates the orbits of Earth, Jupiter, and the Sun using Python and Newtonian mechanics. But with a twist...

👉 What happens if Jupiter is 10x or 100x more massive than its current size?

The simulation demonstrates how increasing Jupiter’s mass drastically affects Earth’s orbit and even makes the Sun move significantly from its usual position. This is a fun but insightful way to understand the importance of massive bodies in maintaining (or disrupting) the stability of planetary systems.

🎯 Features
Simulates the gravitational interactions between the Sun, Earth, and a supermassive Jupiter.

Visualizes how Earth's orbit becomes distorted due to Jupiter's amplified gravitational pull.

Shows how the Sun itself moves around the barycenter (center of mass) when affected by massive planets.

Highly customizable — change masses, distances, or add more bodies to experiment.

🚀 Getting Started
✅ Requirements
Python 3.x

Libraries:

numpy

matplotlib

🔧 Installation
Clone the repository:
git clone https://github.com/laiba32/Conputational-Physics.git

Navigate to the project folder:
cd Comput_phy_assign3_Q2

Install required packages (if not installed):
pip install numpy matplotlib

⚙️ How the Code Works
The code applies Newton's Law of Universal Gravitation to calculate the forces between the Sun, Earth, and Jupiter.

It updates their positions and velocities using a basic numerical integration (Euler method) over time steps.

You can adjust the following parameters:

Mass of Jupiter (Mj)

Mass of the Sun (Ms)

Mass of Earth (Me)

Distances between the bodies

Simulation time steps (dt) and duration (num_steps)

📌 Example Modification:
Change Mj = 100 * 1.898e27 to Mj = 1.898e27 to simulate real Jupiter instead of a supermassive one
