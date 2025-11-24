import time
import csv
from datetime import datetime
import os

LOG_FILE = "time_log.csv"

# ----------------------------------------------------
#  Create CSV Log File
# ----------------------------------------------------
def create_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Start Time", "Stop Time", "Elapsed (seconds)"])  # header


# ----------------------------------------------------
#  Save Data Into CSV
# ----------------------------------------------------
def log_time(start, end, elapsed):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([start, end, f"{elapsed:.2f}"])


# ----------------------------------------------------
#  BASIC STOPWATCH (Your Original Feature)
# ----------------------------------------------------
def stopwatch():
    create_log_file()

    print("\n===== STOPWATCH WITH DATASET =====")
    print("Press ENTER to start")
    print("Press ENTER again to stop")
    print("Type 'exit' to quit\n")

    while True:
        cmd = input("Start/Stop > ")

        if cmd.lower() == "exit":
            print("Exiting stopwatch...")
            break

        # Record start time
        start_time = datetime.now()
        start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")

        input("Stop > ")

        # Record stop time
        end_time = datetime.now()
        end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")

        # Calculate elapsed time
        elapsed = (end_time - start_time).total_seconds()
        print(f"⏱ Time elapsed: {elapsed:.2f} seconds")

        # Save to CSV dataset
        log_time(start_time_str, end_time_str, elapsed)

        print("✔ Logged to time_log.csv\n")


# ----------------------------------------------------
#  LIVE WORKING STOPWATCH (New Feature)
# ----------------------------------------------------
def live_stopwatch():
    print("\n===== LIVE STOPWATCH =====")
    print("Press Ctrl + C to stop...\n")

    start = time.time()

    try:
        while True:
            elapsed = time.time() - start

            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            hundredths = int((elapsed - int(elapsed)) * 100)

            os.system("cls" if os.name == "nt" else "clear")
            print(f"⏱  {minutes:02d}:{seconds:02d}.{hundredths:02d}")
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopped.")
        print(f"Final Time: {elapsed:.2f} seconds")


# ----------------------------------------------------
#  Choose Mode
# ----------------------------------------------------
if __name__ == "__main__":
    print("Choose Mode:")
    print("1 - Basic Stopwatch (Start/Stop & CSV logging)")
    print("2 - Live Stopwatch (Live timer display)")
    mode = input("Enter 1 or 2: ")

    if mode == "1":
        stopwatch()
    elif mode == "2":
        live_stopwatch()
    else:
        print("Invalid choice.")
