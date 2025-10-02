# 🖥️ System Monitor - Usage Guide

A production-ready system monitoring CLI tool that tracks memory, disk, and load metrics using Python + Bash integration.

## 📋 Features

- ✅ **Real-time Monitoring** - Continuous metric collection with customizable intervals
- ✅ **System Metrics** - Memory usage, disk space, and load averages
- ✅ **Alert System** - Configurable thresholds for resource warnings
- ✅ **Time-Series Data** - Queue-based history storage with automatic size management
- ✅ **JSON Export** - Save metrics for analysis or dashboarding
- ✅ **Professional CLI** - Argparse-based interface with subcommands

## 🚀 Quick Start

```bash
# Take a one-time snapshot
python system_monitor.py snapshot

# Monitor continuously every 5 seconds
python system_monitor.py monitor --interval 5

# Show last 10 metrics
python system_monitor.py history --count 10

# Export metrics to JSON
python system_monitor.py export --file metrics.json
```

## 📖 Commands

### `snapshot` - One-Time Metrics Check

Collect and display current system metrics with alert detection.

```bash
python system_monitor.py snapshot
```

**Example Output:**
```
📊 System Snapshot
============================================================
23:05:46 | Mem: 8650/15605MB (55.4%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.56, 0.99, 0.84

✅ System healthy - no alerts
```

### `monitor` - Continuous Monitoring

Monitor system metrics at regular intervals. Press `Ctrl+C` to stop.

```bash
python system_monitor.py monitor [--interval SECONDS] [--max-history SIZE]
```

**Options:**
- `--interval`: Collection interval in seconds (default: 5)
- `--max-history`: Maximum metrics to store in memory (default: 100)

**Example:**
```bash
# Monitor every 3 seconds, keep last 50 metrics
python system_monitor.py monitor --interval 3 --max-history 50
```

**Example Output:**
```
🔍 Monitoring system every 5 seconds...
Press Ctrl+C to stop
============================================================

23:06:00 | Mem: 8734/15605MB (56.0%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.44, 0.94, 0.83

23:06:05 | Mem: 8740/15605MB (56.0%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.41, 0.92, 0.82
⚠️ Alerts:
 - High Memory Usage: 85.2%

^C
🛑 Monitoring stopped
Collected 12 metrics
```

### `history` - Show Metrics History

Collect multiple metric samples and display them as a numbered list.

```bash
python system_monitor.py history [--count NUMBER]
```

**Options:**
- `--count`: Number of metrics to collect and show (default: 10)

**Example:**
```bash
python system_monitor.py history --count 5
```

**Example Output:**
```
Collecting 5 metrics samples...

📜 Last 5 Metrics:
============================================================
1. 23:06:00 | Mem: 8731/15605MB (56.0%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.44, 0.94, 0.83
2. 23:06:01 | Mem: 8734/15605MB (56.0%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.44, 0.94, 0.83
3. 23:06:02 | Mem: 8724/15605MB (55.9%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.44, 0.94, 0.83
4. 23:06:03 | Mem: 8730/15605MB (55.9%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.40, 0.93, 0.82
5. 23:06:04 | Mem: 8728/15605MB (55.9%) | Disk: 20.0/476.0GB (5%) | Load Avg: 0.40, 0.93, 0.82
```

### `export` - Export to JSON

Collect metrics and save them to a JSON file for analysis or integration with other tools.

```bash
python system_monitor.py export [--file FILENAME]
```

**Options:**
- `--file`: Output filename (default: metrics.json)

**Example:**
```bash
python system_monitor.py export --file system_metrics.json
```

**Example Output:**
```
Collecting 10 metric samples for export...
✅ Exported 10 metrics to system_metrics.json
```

**JSON Format:**
```json
{
  "collected_at": "2025-10-02T23:06:13.624345",
  "total_samples": 10,
  "metrics": [
    {
      "timestamp": "2025-10-02T23:06:03.581254",
      "memory_total": 15605,
      "memory_used": 8723,
      "memory_free": 1053,
      "memory_percent": 55.89,
      "disk_total": 476.0,
      "disk_used": 20.0,
      "disk_free": 454.0,
      "disk_percent": 5,
      "load_1m": 0.44,
      "load_5m": 0.94,
      "load_15m": 0.83
    }
  ]
}
```

## ⚙️ Configuration

### Alert Thresholds

Default thresholds (can be customized in code):
- **Memory**: 80% usage
- **Disk**: 90% usage
- **Load Average (1m)**: 5.0

### Metric Collection

The tool uses these Linux commands:
- `free -m` - Memory usage in MB
- `df -h /` - Disk usage for root partition
- `uptime` - Load averages (1, 5, 15 minutes)

## 🔧 Technical Details

### Architecture

```
system_monitor.py
├── SystemMetrics (dataclass)
│   └── Stores: timestamp, memory, disk, load averages
├── parse_memory() → Parse 'free -m' output
├── parse_disk() → Parse 'df -h /' output  
├── parse_uptime() → Parse 'uptime' output
├── collect_metrics() → Coordinator function
├── MetricCollector (class)
│   ├── __init__(max_history) → Initialize deque
│   ├── collect() → Gather metrics, add to history
│   ├── get_history(count) → Retrieve last N metrics
│   └── check_alerts(metrics) → Threshold detection
└── main() → CLI interface with argparse
```

### Data Structures

- **deque** (from collections): Time-series storage with automatic size management
- **dataclass**: Clean data model with type hints
- **subprocess**: Execute bash commands from Python

### Key Concepts

1. **Subprocess Integration**: Execute system commands and parse output
2. **Queue Management**: `deque(maxlen=N)` automatically removes oldest items
3. **Time-Series Data**: Store metrics over time for trend analysis
4. **Alert Logic**: Threshold-based monitoring for proactive warnings
5. **JSON Serialization**: Export data for external tools

## 🎯 Use Cases

1. **Quick System Check**
   ```bash
   python system_monitor.py snapshot
   ```

2. **Monitor During Load Testing**
   ```bash
   python system_monitor.py monitor --interval 1 > load_test.log
   ```

3. **Collect Baseline Metrics**
   ```bash
   python system_monitor.py history --count 60 && \
   python system_monitor.py export --file baseline.json
   ```

4. **Alert on High Usage**
   ```bash
   python system_monitor.py monitor --interval 10
   # Watch for ⚠️ Alerts in output
   ```

## 📚 Learning Resources

See [`learn_subprocess.py`](learn_subprocess.py) for interactive lessons on:
- Basic subprocess command execution
- Parsing command output
- Error handling
- Practical examples

Run the learning script:
```bash
python learn_subprocess.py
```

## 🔗 Related Projects

- **[Command History Manager](COMMAND_HISTORY_USAGE.md)** - Stack-based command tracking
- **[Task Queue Simulator](TASK_QUEUE_USAGE.md)** - Queue and priority queue implementation

## 💡 Future Enhancements

- [ ] Add CPU usage percentage tracking
- [ ] Network I/O monitoring
- [ ] Process-level metrics
- [ ] Configurable thresholds via CLI flags
- [ ] Dashboard web interface
- [ ] Integration with cloud monitoring (CloudWatch, Datadog)
- [ ] Systemd service for continuous monitoring

## ☁️ Cloud Engineering Connection

This project demonstrates concepts used in:
- **CloudWatch Metrics**: Time-series monitoring data
- **CloudWatch Alarms**: Threshold-based alerting
- **EC2 Monitoring**: Instance health tracking
- **Auto Scaling**: Metric-based scaling decisions
- **Lambda**: Serverless monitoring functions
- **Infrastructure Monitoring**: Server health tracking

---

**Built with Python 3** | Part of the 30-Day Coding Journey
