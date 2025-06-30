# pip install speedtest-cli
import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
import threading

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")
        self.root.geometry("400x300")
        
        # Create widgets
        self.setup_ui()
        
        # Speedtest object
        self.st = speedtest.Speedtest()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Test button
        self.test_btn = ttk.Button(
            main_frame, 
            text="Run Speed Test", 
            command=self.start_test_thread
        )
        self.test_btn.pack(pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame, 
            orient=tk.HORIZONTAL,
            length=300, 
            mode='determinate'
        )
        self.progress.pack(pady=10)
        
        # Results labels
        self.ping_label = ttk.Label(main_frame, text="Ping: -- ms")
        self.ping_label.pack(pady=5)
        
        self.download_label = ttk.Label(main_frame, text="Download: -- Mbps")
        self.download_label.pack(pady=5)
        
        self.upload_label = ttk.Label(main_frame, text="Upload: -- Mbps")
        self.upload_label.pack(pady=5)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready")
        self.status_label.pack(pady=10)
        
    def start_test_thread(self):
        """Start the speed test in a separate thread"""
        self.test_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Preparing test...")
        threading.Thread(target=self.run_speedtest, daemon=True).start()
        
    def update_progress(self, value, message):
        """Update progress bar and status"""
        self.progress['value'] = value
        self.status_label.config(text=message)
        self.root.update_idletasks()
        
    def run_speedtest(self):
        try:
            # Get best server
            self.update_progress(10, "Finding best server...")
            self.st.get_best_server()
            
            # Ping test
            self.update_progress(30, "Testing ping...")
            ping = self.st.results.ping
            self.ping_label.config(text=f"Ping: {ping:.2f} ms")
            
            # Download test
            self.update_progress(50, "Testing download speed...")
            download_speed = self.st.download() / 1_000_000  # Convert to Mbps
            self.download_label.config(text=f"Download: {download_speed:.2f} Mbps")
            
            # Upload test
            self.update_progress(80, "Testing upload speed...")
            upload_speed = self.st.upload() / 1_000_000  # Convert to Mbps
            self.upload_label.config(text=f"Upload: {upload_speed:.2f} Mbps")
            
            # Complete
            self.update_progress(100, "Test complete!")
            self.test_btn.config(state=tk.NORMAL)
            
        except Exception as e:
            messagebox.showerror("Error", f"Speed test failed:\n{str(e)}")
            self.update_progress(0, "Test failed")
            self.test_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()