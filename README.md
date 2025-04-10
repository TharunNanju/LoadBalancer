# Load Balancer using Tailscale VPN

A fault-tolerant, scalable, and real-time load balancing system built using Docker, Nginx, Tailscale, Grafana, Prometheus, and Twilio.

This project simulates a production-grade system with multiple backends running across different networks, connected securely through Tailscale VPN and balanced using Nginx.

---

## Tech Stack

- Docker – Containerized backends and services  
- Nginx – Load balancing across backend containers  
- Tailscale – Secure VPN tunneling between distributed devices  
- Prometheus – Metrics scraping from Nginx  
- Grafana – Dashboards for real-time metrics  
- Twilio – WhatsApp alerts on backend failure and recovery  
- Apache Benchmark (ab) – Load testing tool

---

## Features

- Round-robin load balancing across multiple backends
- Cross-network backend connectivity using Tailscale
- Twilio alert bot to notify backend crashes and recovery
- Grafana dashboard for live metrics
- Prometheus for scraping and storing request data
- Easily scalable: add or remove backends as needed

---

## How It Works

1. Nginx distributes incoming traffic to Flask-based backend containers using round-robin.
2. Each backend can be on a different physical machine connected over Tailscale VPN.
3. Prometheus periodically scrapes request metrics from Nginx.
4. Grafana displays these metrics in an interactive dashboard.
5. A Python bot (`alert_bot.py`) checks backend health:
   - Sends a WhatsApp alert via Twilio if a backend goes down.
   - Sends another alert when it comes back online.

---

## Tailscale Setup

- Download and install Tailscale on all devices (backend machines and load balancer).
- Sign up or log in using a single Tailscale account.
- All devices that are to be part of the system must be logged in with the **same Tailscale account**.
- Once connected, Tailscale assigns a unique internal IP to each device.
- These IPs must be updated in:
  - `nginx.conf` (under the list of backend servers)
  - `prometheus.yml` (Prometheus is scraping metrics from Tailscale-connected devices)

---

## Running the Project

### Server with Load Balancer
### Step 1: Clone the repo and enter the directory

```bash
cd project-directory
```

### Step 2: Build and start containers

Run either of the 2 commands

To run with CLI logs (more informative):
```bash
docker-compose up --build 
```
To run in detached mode, without CLI logs (for a cleaner look):
```bash
docker-compose up --build -d 
```

### Step 3: Start the Twilio alert bot

```bash
python alert_bot.py
```
Make sure your `.env` file is set up with Twilio credentials.

### Step  4: Run load test (optional)

```bash
ab -n 1000 -c 100 http://localhost:8080/
```
This sends 1000 requests with concurrency level 100 to test load balancing.

### Server with only Backends
> Note: cd into `backend` folder
### Step 1: Create backend image

```bash
docker build -t backend-clone .  
```

### Step 2: Start containers

```bash
docker run -d -p 5005:5000 backend-clone
```
> **Note**: In the command below, replace `5005` (the port on the **left-hand side**) with any available port on your system.

This maps the container's internal port `5000` (used by the Flask server) to a host machine port.
The left-hand port (`5005`) determines how you access the service from your browser or tools like Apache Benchmark. Make sure to use a unique and free port to avoid conflicts with other running containers or services.


---

## Monitoring & Dashboards

### Access Services Locally

- **Grafana Dashboard**: [http://localhost:3001](http://localhost:3001)  
- **Prometheus Interface**: [http://localhost:9091](http://localhost:9091)

> Note: Prometheus scrapes metrics from Nginx at regular intervals and exposes them on port `9090` inside Docker.

### Configure Prometheus Data Source in Grafana

1. Open Grafana
2. Go to **Settings → Data Sources**
3. Add a new Prometheus data source
4. Use this URL as the data source: http://prometheus:9090/

### Import Dashboard for Visualizations

To display real-time metrics:

1. Open Grafana
2. Go to **Dashboards → Import**
3. Upload the provided `.json` file (we created this file beforehand)
4. Click **Import**

### Visuals Included in the Dashboard

- Request load distributed across all active backends
- Total number of requests handled
- Uptime status of each backend
- Time-series plots for request spikes and dips

---

## Future Prospects

This project has strong potential for expansion and integration into more advanced, real-world systems. Some possible future directions include:

### 1. **Dynamic Backend Registration**
- Automate backend discovery and registration using a service like Consul or custom health check agents.
- No need to manually modify `nginx.conf` when a new server is added or removed.

### 2. **Self-Healing Architecture**
- Implement automatic backend restart or replacement on failure.
- Integrate with orchestration tools like Kubernetes or Docker Swarm for auto-recovery.

### 3. **Machine Learning-Based Load Prediction**
- Analyze traffic patterns to predict high-load periods.
- Pre-scale the number of backends based on predicted demand.

### 4. **Deployment to Cloud**
- Extend the current local + VPN model to use cloud VMs as backends.
- Use Terraform or Ansible for infrastructure automation.

### 5. **Custom Load Balancing Algorithms**
- Explore algorithms beyond round-robin like least connections or response-time-based routing.
- Implement logic in Nginx or build a custom reverse proxy.

### 6. **Security Enhancements**
- Add OAuth2/JWT authentication for dashboard access.
- Encrypt inter-container traffic with mTLS over VPN.

---
