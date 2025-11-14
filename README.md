# COMRADE-WEB-IP

COMRADE-WEB-IP is a simple command-line tool to find the public and private IPv4 and IPv6 addresses of a website. It displays the results in a visually appealing way using ASCII art and colored output.

---

## Features

- Fetch IPv4 and IPv6 addresses of a website
- Detect private IPv4 addresses
- Clean and colorful CLI interface with ASCII art

---

## Installation

You can install COMRADE-WEB-IP directly from GitHub:

```bash
# Clone the repository
git clone https://github.com/Comrade-P/COMRADE-WEB-IP.git
cd COMRADE-WEB-IP

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install the package
pip install -e .

#RUN THE COMMAND
comrade_web_ip --u example.com
