import csv
import random
from datetime import datetime, timedelta

# Configuración básica
output_file = "simulated_logs.csv"
num_entries = 200

# Usuarios e IPs simuladas
users = ["admin", "operator", "j.guagnelli", "service_account", "guest"]
ips_internal = ["192.168.1." + str(i) for i in range(10, 20)]
ips_external = ["45.67.89." + str(i) for i in range(100, 110)]

# Eventos posibles
events = [
    "login_success",
    "login_failed",
    "file_access",
    "config_change",
    "network_scan_detected",
    "multiple_failed_logins"
]

# Generar timestamp base
base_time = datetime.now() - timedelta(days=1)

log_entries = []

for i in range(num_entries):
    timestamp = base_time + timedelta(seconds=random.randint(0, 86400))
    user = random.choice(users)
    ip = random.choice(ips_internal + ips_external)
    event = random.choices(
        events,
        weights=[50, 70, 30, 10, 5, 10],
        k=1
    )[0]

    message = f"{event.replace('_', ' ').title()} for user {user} from IP {ip}"

    log_entries.append({
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "ip_address": ip,
        "event": event,
        "message": message
    })

# Guardar como CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=log_entries[0].keys())
    writer.writeheader()
    writer.writerows(log_entries)

print(f"[✓] Log simulation completed: {output_file}")
