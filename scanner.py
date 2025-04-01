import socket

# Ziel-IP eingeben
target = input("Gib die Ziel-IP ein: ")

# Port-Bereich definieren
start_port = 20
end_port = 1024

print(f"Scanne {target} von Port {start_port} bis {end_port}...")

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} ist offen")
    s.close()

print("Scan abgeschlossen.")

