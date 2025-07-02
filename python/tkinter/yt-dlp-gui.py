import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import threading
import os


class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("#pip install yt-dlp")
        self.root.geometry("500x300")
        self.root.resizable(False, False)

        # Variables
        self.url_var = tk.StringVar()
        self.download_type = tk.StringVar(value="video")
        self.playlist_var = tk.BooleanVar(value=False)
        self.output_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))

        # Create UI
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Video URL:").pack()

        # URL Entry
        self.url_var = tk.StringVar()
        self.url_var.trace_add("write", self.validate_url_entry)
        url_entry = ttk.Entry(self.root, textvariable=self.url_var, width=40)
        url_entry.pack()

        # Clear Button (initially disabled)
        self.clear_btn = ttk.Button(
            self.root, text="Clear URL", command=self.clear_url, state="disabled"
        )
        self.clear_btn.pack()

        # Download Type
        type_frame = ttk.LabelFrame(self.root, text="Download Type")
        type_frame.pack(pady=10, fill="x", padx=10)

        ttk.Radiobutton(
            type_frame, text="Best Video", variable=self.download_type, value="video"
        ).pack(side="left", padx=10)
        ttk.Radiobutton(
            type_frame, text="Best Audio", variable=self.download_type, value="audio"
        ).pack(side="left", padx=10)

        # Options
        options_frame = ttk.Frame(self.root)
        options_frame.pack(pady=5, fill="x", padx=10)

        ttk.Checkbutton(
            options_frame, text="Download Playlist", variable=self.playlist_var
        ).pack(side="left")

        # Output Path
        path_frame = ttk.Frame(self.root)
        path_frame.pack(pady=5, fill="x", padx=10)

        ttk.Label(path_frame, text="Save to:").pack(side="left")
        ttk.Entry(path_frame, textvariable=self.output_path, width=30).pack(
            side="left", padx=5
        )
        ttk.Button(path_frame, text="Browse", command=self.select_directory).pack(
            side="left"
        )

        # Download Button
        ttk.Button(self.root, text="Download", command=self.start_download).pack(
            pady=20
        )

        # Progress/Status
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(self.root, textvariable=self.status_var).pack()

        self.progress = ttk.Progressbar(self.root, mode="indeterminate")

    def validate_url_entry(self, *args):
        if self.url_var.get().strip() == "":
            self.clear_btn.config(state="disabled")
        else:
            self.clear_btn.config(state="normal")

    def clear_url(self):
        self.url_var.set("")
        self.clear_btn.config(state="disabled")

    def select_directory(self):
        directory = filedialog.askdirectory(initialdir=self.output_path.get())
        if directory:
            self.output_path.set(directory)

    def start_download(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return

        # Start download in a separate thread
        threading.Thread(target=self.download_video, daemon=True).start()
        self.progress.pack(fill="x", padx=10)
        self.progress.start()
        self.status_var.set("Downloading...")

    def download_video(self):
        url = self.url_var.get()
        download_type = self.download_type.get()
        is_playlist = self.playlist_var.get()
        output_path = self.output_path.get()

        try:
            # Build yt-dlp command
            cmd = [
                "yt-dlp",
                "-P",
                output_path,
                "--no-playlist" if not is_playlist else "--yes-playlist",
            ]

            if download_type == "audio":
                cmd.extend(
                    [
                        "-x",  # Extract audio
                        "--audio-format",
                        "mp3",
                        "--audio-quality",
                        "0",  # Best quality
                        "--embed-thumbnail",
                        "--embed-metadata",
                        "-o '%(title)s.%(ext)s'"
                    ]
                )
            else:
                cmd.extend(
                    [
                        "-f",
                        "bestvideo+bestaudio",
                        "--merge-output-format",
                        "mp4",
                        "--embed-thumbnail",
                        "--embed-metadata",
                        "-o '%(title)s.%(ext)s'"
                    ]
                )

            cmd.append(url)

            # Run command
            process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )

            # Monitor progress
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    self.status_var.set(output.strip())

            # Check for errors
            if process.returncode != 0:
                error = process.stderr.read()
                messagebox.showerror("Error", f"Download failed:\n{error}")
            else:
                messagebox.showinfo("Success", "Download completed successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
        finally:
            self.progress.stop()
            self.progress.pack_forget()
            self.status_var.set("Ready")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    app.run()
