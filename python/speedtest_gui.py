# speedtest_gui.py

import tkinter as tk
from tkinter import ttk
import speedtest
import threading


def run_speed_test():
    # Disable button during test
    test_button.config(state="disabled")
    result_label.config(text="Running speed test... Please wait.")

    def test():
        try:
            spd = speedtest.Speedtest()
            spd.get_best_server()
            download_speed = spd.download() / 1_000_000  # Convert to Mbps
            upload_speed = spd.upload() / 1_000_000  # Convert to Mbps
            ping = spd.results.ping
            server = spd.get_best_server()
            server_info = f"{server['host']} ({server['name']}, {server['country']})"

            result = (
                f"Download Speed: {download_speed:.2f} Mbps\n"
                f"Upload Speed:   {upload_speed:.2f} Mbps\n"
                f"Ping:           {ping:.2f} ms\n"
                f"Server:         {server_info}"
            )
        except Exception as e:
            result = f"Error: {e}"

        result_label.config(text=result)
        test_button.config(state="normal")

    # Run the test in a separate thread to avoid freezing the GUI
    threading.Thread(target=test).start()


# Create GUI window
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("650x250")

# Button to run test
test_button = ttk.Button(root, text="Run Speed Test", command=run_speed_test)
test_button.pack(pady=20)

# Label to display results
result_label = tk.Label(
    root,
    text="Press the button to test internet speed.",
    justify="left",
    font=("Courier", 10),
)
result_label.pack(padx=10, pady=10)

# Run the application
root.mainloop()
