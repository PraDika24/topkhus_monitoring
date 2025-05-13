from flask import Flask, render_template
import datetime

app = Flask(__name__)

def read_log():
    log_file = "logs/server_monitor.log"
    timestamps, cpu, ram, swap, disk = [], [], [], [], []

    try:
        with open(log_file, "r") as f:
            lines = f.readlines()
            for line in lines[-20:]:  # Tampilkan 20 data terakhir
                parts = line.strip().split(", ")
                if len(parts) != 5:
                    continue
                time = parts[0]
                cpu_usage = parts[1].split(": ")[1].replace("%", "")
                ram_usage = parts[2].split(": ")[1].replace("%", "")
                swap_usage = parts[3].split(": ")[1].replace("%", "")
                disk_usage = parts[4].split(": ")[1].replace("%", "")

                timestamps.append(time)
                cpu.append(float(cpu_usage) if cpu_usage else 0.0)
                ram.append(float(ram_usage) if ram_usage else 0.0)
                swap.append(float(swap_usage) if swap_usage else 0.0)
                disk.append(float(disk_usage) if disk_usage else 0.0)
    except Exception as e:
        print("Error reading log:", e)

    return timestamps, cpu, ram, swap, disk

@app.route("/")
def dashboard():
    timestamps, cpu, ram, swap, disk = read_log()
    if not timestamps or not cpu or not ram or not swap or not disk:
        timestamps, cpu, ram, swap, disk = [], [], [], [], []
    return render_template("dashboard.html", timestamps=timestamps, cpu=cpu, ram=ram, swap=swap, disk=disk)

if __name__ == "__main__":
    app.run(debug=True)