# 🚦 Traffic Light Controller – Logisim Evolution

A simple digital circuit project simulating a Traffic Light System using Logisim Evolution.
This project demonstrates how binary counters and logic gates control Red, Yellow, and Green lights in a sequence — an ideal beginner’s introduction to VLSI and chip design fundamentals.

# 🧠 Overview

The circuit uses a 2-bit counter connected to a clock to generate binary sequences (00, 01, 10, 11).
Using AND and NOT gates, these signals control the three lights representing real-world traffic signals.

# Sequence:
🟥 Red → 🟩 Green → 🟨 Yellow → repeat ♻️

⚙️ Components Used

# Clock (for timing)

2-bit Counter (from Memory section)

Logic Gates (AND, NOT)

Output Pins (as LEDs)

# Wires for connections

🔩 Working Logic
Light	Q1	Q0	Logic Expression
Red	0	0	NOT Q1 AND NOT Q0
Green	0	1	NOT Q1 AND Q0
Yellow	1	0	Q1 AND NOT Q0

The counter cycles through these binary states, automatically switching the lights in order.

# 💡 Learning Outcomes

Understanding binary counting and state transitions

Designing sequential circuits with clock and counter

Applying combinational logic to control real-world systems

Gaining hands-on experience with VLSI basics in Logisim

# 🧰 Tools & Software

Logisim Evolution v3.7.1 or above

Java 21 or newer (for running Logisim)

# 📁 How to Use

Open traffic_light_logisim.circ in Logisim Evolution.

Click Simulate → Tick Enable to start the circuit.

Set Tick Frequency to around 1 Hz for visible timing.

Watch the LEDs cycle through Red → Green → Yellow → Red.

# 🧩 Author

Pranay Anand

Aspiring Python Developer & VLSI Enthusiast
Passionate about bridging software intelligence with hardware design.
