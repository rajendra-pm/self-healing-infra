# self-healing-infra
# Self-Healing NGINX Infrastructure

This project demonstrates a **self-healing infrastructure** using **Prometheus**, **Alertmanager**, **Flask**, and **Ansible**.  
When NGINX goes down, Prometheus triggers an alert, Alertmanager sends it to the Flask webhook listener, and Ansible automatically restarts the NGINX container.

---

## Features

- Monitors NGINX service uptime
- Automatically restarts NGINX if it goes down
- Uses a Flask webhook listener to receive alerts
- Ansible playbooks for automation
- Dockerized setup for Prometheus, Alertmanager, and NGINX

---

## Prerequisites

- Docker Compose
- Python 3
- Flask
- Ansible
- Linux/WSL environment

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/rajendra-pm/self-healing-infra.git
cd self-healing-infra
