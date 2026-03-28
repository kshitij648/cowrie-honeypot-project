# cowrie-honeypot-project
SSH Honeypot using cowrie with log analysis

# 🛡️ Cowrie Honeypot Project

## 📌 Description
This project uses the Cowrie SSH honeypot to monitor attacker activities.
It captures login attempts, commands, and IP addresses.

## ⚙️ Features
- SSH honeypot simulation
- Attack logging
- Python analyzer script
- Extracts IPs, commands, login attempts

## 🚀 How to Run

```bash
cd ~/cowrie
bin/cowrie start
Log Analysis
The project includes a Python-based log analyzer that processes Cowrie logs to extract meaningful insights.
🔍 Extracted Data:
Attacker IP addresses
Login attempts (username/password)
Commands executed by attackers
Session activity
🛠️ Usage:
Bash
python analyzer.py cowrie.log
📁 Project Structure

cowrie-honeypot-project/
│── cowrie/               # Cowrie honeypot installation
│── logs/                 # Captured logs
│── analyzer.py           # Python log analysis script
│── README.md             # Project documentation
⚙️ Requirements
Make sure you have the following installed:
Python 3.x
Cowrie SSH Honeypot
Linux environment (Kali Linux / Ubuntu recommended)
🚀 Installation Guide
1️⃣ Clone the Repository
Bash
git clone https://github.com/your-username/cowrie-honeypot-project.git
cd cowrie-honeypot-project
2️⃣ Install Dependencies
Bash
sudo apt update
sudo apt install python3 python3-pip -y
3️⃣ Setup Cowrie
Bash
git clone https://github.com/cowrie/cowrie.git
cd cowrie
bin/cowrie start
🧪 How It Works
Cowrie simulates an SSH server
Attackers attempt to login
All activities are logged
Python script analyzes logs
Insights are generated for security research
Author
Kshitij Pandey
Cybersecurity Enthusiast 🚀
