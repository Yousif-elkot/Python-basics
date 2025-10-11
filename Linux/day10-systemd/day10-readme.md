# Day 10: Process Management & systemd Service

## 🎯 Project Goal
Master process management and systemd by creating a production-ready Flask web application managed as a systemd service.

## 📚 What You'll Learn
- Process states and lifecycle
- Signal handling (SIGTERM vs SIGKILL)
- Job control (fg, bg, jobs)
- systemd service file structure
- Service management with systemctl
- Log analysis with journalctl

## 🏗️ Project Structure
```
day10-systemd/
├── flask_app.py          # Python Flask web application
├── flask-app.service     # systemd service unit file
├── setup.sh              # Installation and configuration script
├── test_service.sh       # Comprehensive test suite
└── README.md             # This file
```

## 🚀 Quick Start

### Prerequisites
```bash
# Install Flask
pip3 install flask --user

# Ensure you're in the project directory
cd ~/cloud-engineer-plan/linux/day10-systemd
```

### Installation
```bash
# Make scripts executable
chmod +x setup.sh test_service.sh

# Run setup (requires sudo)
sudo ./setup.sh
```

### Verification
```bash
# Run test suite
./test_service.sh

# Or test manually
curl http://localhost:5000
curl http://localhost:5000/health
```

## 🔧 Service Management Commands

### Basic Operations
```bash
# Check service status
sudo systemctl status flask-app

# Start the service
sudo systemctl start flask-app

# Stop the service
sudo systemctl stop flask-app

# Restart the service
sudo systemctl restart flask-app

# Reload configuration (without stopping)
sudo systemctl reload flask-app
```

### Boot Configuration
```bash
# Enable service to start on boot
sudo systemctl enable flask-app

# Disable service from starting on boot
sudo systemctl disable flask-app

# Check if enabled
systemctl is-enabled flask-app
```

### Log Management
```bash
# View all logs
journalctl -u flask-app

# View logs in real-time
journalctl -u flask-app -f

# View logs since last boot
journalctl -u flask-app -b

# View last 50 lines
journalctl -u flask-app -n 50

# View logs from specific time
journalctl -u flask-app --since "1 hour ago"
```

## 📊 Understanding the Service File

### [Unit] Section
```ini
[Unit]
Description=Flask Web Application Demo
After=network.target
```
- **Description**: Human-readable name
- **After**: Start only after network is available

### [Service] Section
```ini
[Service]
Type=simple
User=yourname
WorkingDirectory=/path/to/app
ExecStart=/usr/bin/python3 flask_app.py
Restart=on-failure
RestartSec=5
```
- **Type=simple**: Process runs in foreground
- **User**: Run as specific user (not root for security)
- **WorkingDirectory**: Where to run the app
- **ExecStart**: Command to start the service
- **Restart=on-failure**: Auto-restart if crashed
- **RestartSec=5**: Wait 5 seconds before restart

### [Install] Section
```ini
[Install]
WantedBy=multi-user.target
```
- **WantedBy**: When to start (multi-user.target = normal boot)

## 🧪 Testing Scenarios

### Test 1: Basic Functionality
```bash
# Service should be running
systemctl is-active flask-app

# Should return "active"
```

### Test 2: HTTP Endpoints
```bash
# Main endpoint
curl http://localhost:5000
# Should return JSON with status: "running"

# Health endpoint
curl http://localhost:5000/health
# Should return JSON with status: "healthy"
```

### Test 3: Auto-Restart on Failure
```bash
# Get current PID
systemctl show -p MainPID flask-app

# Kill the process
sudo kill -9 <PID>

# Wait 6 seconds, then check status
sleep 6
systemctl status flask-app
# Should show new PID and still be active
```

### Test 4: Graceful Shutdown
```bash
# Stop service
sudo systemctl stop flask-app

# Check logs
journalctl -u flask-app -n 5
# Should show "Shutting down gracefully..."
```

## 🔍 Troubleshooting

### Service Won't Start
```bash
# Check detailed status
systemctl status flask-app -l

# Check logs for errors
journalctl -u flask-app -n 50

# Verify service file syntax
systemd-analyze verify flask-app.service

# Common issues:
# 1. Wrong paths in service file
# 2. Permission issues
# 3. Flask not installed
# 4. Port 5000 already in use
```

### Port Already in Use
```bash
# Find what's using port 5000
sudo lsof -i :5000

# Kill the process
sudo kill <PID>

# Or use different port in flask_app.py
```

### Permission Denied
```bash
# Ensure proper ownership
sudo chown -R $USER:$USER ~/cloud-engineer-plan/linux/day10-systemd

# Verify service file permissions
ls -l /etc/systemd/system/flask-app.service
# Should be: -rw-r--r-- root root
```

## 📈 Key Concepts Demonstrated

### 1. Process Lifecycle
- Created → Running → Sleeping → Stopped → Zombie → Dead
- Our app handles SIGTERM and SIGINT for graceful shutdown

### 2. Signal Handling
```python
signal.signal(signal.SIGTERM, graceful_shutdown)
signal.signal(signal.SIGINT, graceful_shutdown)
```

### 3. Service Supervision
- systemd monitors PID
- Automatically restarts on failure
- Manages dependencies (network.target)

### 4. Logging Best Practices
- All output goes to systemd journal
- Centralized log management
- Easy filtering and searching

## 🎓 Learning Outcomes

After completing this project, you should understand:
- ✅ How processes work in Linux
- ✅ The difference between SIGTERM and SIGKILL
- ✅ How to write systemd service files
- ✅ Service management with systemctl
- ✅ Log analysis with journalctl
- ✅ Auto-restart and failure recovery
- ✅ Boot-time service configuration

## 🔗 Additional Resources
- [systemd service documentation](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
- [Flask documentation](https://flask.palletsprojects.com/)
- [journalctl manual](https://www.freedesktop.org/software/systemd/man/journalctl.html)

## 📝 Notes
- Always test service files before enabling on boot
- Use `systemctl daemon-reload` after editing service files
- Monitor logs during development with `journalctl -f`
- Consider using `systemctl edit flask-app` for overrides

---

**Day 10 Complete!** 🎉
Next: Day 11 - Networking Deep Dive
