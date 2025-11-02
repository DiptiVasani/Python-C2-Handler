# Mini Lab — C2 Workflow (Sanitized)  
> **DO NOT PUBLISH REAL PAYLOADS OR C2 CODE.**  
>  **Important:** This repository contains a **sanitized, harmless demo** only. It does **not** include real payloads, reverse shells, or any code that enables remote compromise. This is for educational purposes only and was tested in an isolated lab environment.
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

1. **Prepare environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # macOS / Linux
   # venv\Scripts\activate      # Windows PowerShell
