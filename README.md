⏱️ Python Stopwatch Project

A simple and efficient stopwatch application built in Python. It supports start, stop, reset, lap recording, and automatic saving of lap times to a CSV file.
A separate script is provided to visualize lap times as a graph using Matplotlib.

📌 Features
🕒 Stopwatch

Start, Stop, Resume, Reset functions

Live running display

Lap recording

Auto-save lap timestamps to laps.csv

CSV automatically appends only new laps

📈 Graphing Script

Reads laps.csv

Plots Lap Number vs Time Taken

Auto-opens graph window

Clean, simple Matplotlib chart

📂 Project Structure
stopwatch/
│── stopwatch.py               # Main stopwatch application
│── graph_viewer.py           # Graph generation script
│── laps.csv                  # Auto-generated file (lap data)
│── README.md

🚀 How to Run
1. Install Required Package
pip install matplotlib

2. Run Stopwatch
python stopwatch.py

3. Generate Lap Graph
python graph_viewer.py

🖥️ Preview (Functionality Overview)
Stopwatch

Displays live time (HH:MM:SS.ms)

Records lap times

Saves to CSV without overwriting existing laps

Graph Viewer

Creates a graph of:

Lap Number ➜ X-axis  
Lap Time (seconds) ➜ Y-axis  

📜 Example Code Snippets
stopwatch.py

Contains:

Live display loop

CSV append logic

Keyboard control (start/stop/lap/reset)

graph_viewer.py

Reads laps.csv

Uses Matplotlib to draw graph

Opens window automatically

🌟 Future Improvements

GUI using Tkinter / PyQt

Export to PNG graph

Web dashboard using Flask

Real-time graph update

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.
