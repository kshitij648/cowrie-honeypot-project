log_file = "cowrie.log"

ips = set()
commands = []
logins = []

with open(log_file, "r") as f:
    for line in f:
        if "HoneyPotSSHTransport" in line:
            parts = line.split(',')
            if len(parts) > 2:
                ips.add(parts[2].strip())

        if "CMD:" in line:
            commands.append(line.split("CMD:")[1].strip())

        if "login attempt" in line:
            logins.append(line.strip())

print("\n🔹 Unique IPs:")
for ip in ips:
    print(ip)

print("\n🔹 Commands Used:")
for cmd in commands:
    print(cmd)

print("\n🔹 Login Attempts:")
for l in logins:
    print(l)
