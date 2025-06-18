# speedtest.py
# pip install speedtest-cli

import speedtest

spd = speedtest.Speedtest()

download_speed = spd.download() / 1_000_000  # Convert to Mbps
upload_speed = spd.upload() / 1_000_000  # Convert to Mbps
ping = spd.results.ping
server = spd.get_best_server()
server_info = f"{server['host']} ({server['name']}, {server['country']})"

print(f"Download Speed: \t{download_speed:.2f} Mbps")
print(f"Upload Speed: \t\t{upload_speed:.2f} Mbps")
print(f"Ping: \t\t\t{ping:.2f} ms")
print(f"Server: \t\t{server_info}")
