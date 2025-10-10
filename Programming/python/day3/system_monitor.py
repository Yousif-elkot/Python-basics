from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Tuple
from collections import deque
import subprocess
import json
import time
import argparse
        

@dataclass
class SystemMetrics:
    timestamp: datetime
    memory_total: int      # MB
    memory_used: int       # MB
    memory_free: int       # MB
    memory_percent: float  # %
    disk_total:float       # GB
    disk_used: float       # GB
    disk_free: float       # GB
    disk_percent: int      # %
    load_1m: float
    load_5m: float
    load_15m: float

    def __str__(self):
        # Expected output format:
        # 21:48:59 up 1 day, 11 min,  1 user,  load average: 0.37, 0.53, 0.50
        return (f"{self.timestamp.strftime('%H:%M:%S')} | "
                f"Mem: {self.memory_used}/{self.memory_total}MB ({self.memory_percent:.1f}%) | "
                f"Disk: {self.disk_used}/{self.disk_total}GB ({self.disk_percent}%) | "
                f"Load Avg: {self.load_1m:.2f}, {self.load_5m:.2f}, {self.load_15m:.2f}")
    
    def to_dict(self):
        return {
            "timestamp": self.timestamp.isoformat(),
            "memory_total": self.memory_total,
            "memory_used": self.memory_used,
            "memory_free": self.memory_free,
            "memory_percent": self.memory_percent,
            "disk_total": self.disk_total,
            "disk_used": self.disk_used,
            "disk_free": self.disk_free,
            "disk_percent": self.disk_percent,
            "load_1m": self.load_1m,
            "load_5m": self.load_5m,
            "load_15m": self.load_15m
        }
    
    
#parse function
def parse_memory() -> tuple[int, int, int, float]:
    """Parse memory usage using 'free -m' command."""
    result = subprocess.run(['free', '-m'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    # Expected output format:
    # Mem:           15605        8168        1639        1112        5552        7436
    #              [total]      [used]      [free]
    mem_line = next((line for line in lines if line.startswith('Mem:')), None)
    if mem_line:
        parts = mem_line.split()
        total = int(parts[1])
        used = int(parts[2])
        free = int(parts[3])
        percent = (used / total) * 100 if total > 0 else 0.0
        return total, used, free, percent
    raise RuntimeError("Failed to parse memory info")

def parse_disk() -> tuple[float, float, float, int]:
    """Parse disk usage using 'df -h /' command."""
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    # Expected output format:
    # /dev/nvme0n1p2  476G   20G  454G   5% /
    #               [size] [used] [avail] [use%]
    disk_line = next((line for line in lines if line.startswith('/')), None)
    if disk_line:
        parts = disk_line.split()
        total = float(parts[1][:-1])  # Remove 'G'
        used = float(parts[2][:-1])   # Remove 'G'
        free = float(parts[3][:-1])   # Remove 'G'
        percent = int(parts[4][:-1])  # Remove '%'
        return total, used, free, percent
    raise RuntimeError("Failed to parse disk info")

def parse_uptime() -> tuple[float, float, float]:
    """Parse system load averages using 'uptime' command."""
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    output = result.stdout.strip()
    # Expected output format:
    # 21:48:59 up 1 day, 11 min,  1 user,  load average: 0.37, 0.53, 0.50
    if "load average:" in output:
        load_part = output.split("load average:")[-1].strip()
        loads = load_part.split(", ")
        load_1m = float(loads[0])
        load_5m = float(loads[1])
        load_15m = float(loads[2])
        return load_1m, load_5m, load_15m
    raise RuntimeError("Failed to parse uptime info")

# Collector function
def collect_metrics() -> SystemMetrics:
    """Collect system metrics."""
    memory_total, memory_used, memory_free, memory_percent = parse_memory()
    disk_total, disk_used, disk_free, disk_percent = parse_disk()
    load_1m, load_5m, load_15m = parse_uptime()
    
    return SystemMetrics(
        timestamp=datetime.now(),
        memory_total=memory_total,
        memory_used=memory_used,
        memory_free=memory_free,
        memory_percent=memory_percent,
        disk_total=disk_total,
        disk_used=disk_used,
        disk_free=disk_free,
        disk_percent=disk_percent,
        load_1m=load_1m,
        load_5m=load_5m,
        load_15m=load_15m
    )

# Metric history and alerting
class MetricCollector:
    def __init__(self, max_history: int = 100):
        self.history: deque[SystemMetrics] = deque(maxlen=max_history)

    def collect(self) -> SystemMetrics:
        metrics = collect_metrics()
        self.history.append(metrics)
        return metrics
    
    def get_history(self, count: int = 10) -> List[SystemMetrics]:
        return list(self.history)[-count:]
    
    def check_alerts(self, metrics: SystemMetrics, 
                     mem_threshold: float = 80.0, 
                     disk_threshold: float = 90.0, 
                     load_threshold: float = 5.0) -> List[str]:
        alerts = []
        if metrics.memory_percent > mem_threshold:
            alerts.append(f"High Memory Usage: {metrics.memory_percent:.1f}%")
        if metrics.disk_percent > disk_threshold:
            alerts.append(f"High Disk Usage: {metrics.disk_percent}%")
        if metrics.load_1m > load_threshold:
            alerts.append(f"High Load Average (1m): {metrics.load_1m:.2f}")
        return alerts

def main():
    parser = argparse.ArgumentParser(
        description="System Monitor - Track memory, disk, and load metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # One-time snapshot
  python system_monitor.py snapshot
  
  # Monitor every 5 seconds
  python system_monitor.py monitor --interval 5
  
  # Show last 10 metrics
  python system_monitor.py history --count 10
  
  # Export history to JSON
  python system_monitor.py export --file metrics.json
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # snapshot command
    snapshot_parser = subparsers.add_parser('snapshot', help='Take a one-time snapshot of system metrics')
    
    # monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Continuously monitor system metrics')
    monitor_parser.add_argument('--interval', type=int, default=5, help='Collection interval in seconds (default: 5)')
    monitor_parser.add_argument('--max-history', type=int, default=100, help='Maximum history size (default: 100)')
    
    # history command
    history_parser = subparsers.add_parser('history', help='Show metrics history')
    history_parser.add_argument('--count', type=int, default=10, help='Number of metrics to show (default: 10)')
    
    # export command
    export_parser = subparsers.add_parser('export', help='Export metrics history to JSON')
    export_parser.add_argument('--file', type=str, default='metrics.json', help='Output file (default: metrics.json)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Implement command handlers here
    if args.command == 'snapshot':
        #collect metrics once
        collector = MetricCollector(max_history=1)

        #collect metrics once
        metrics = collector.collect()

        #Display metrics
        print("📊 System Snapshot")
        print("=" * 60)
        print(metrics)

        #Check for alerts
        alerts = collector.check_alerts(metrics)
        if alerts:
            print("\n⚠️ Alerts:")
            for alert in alerts:
                print(f" - {alert}")
        else:
            print("\n✅ System healthy - no alerts")
    
    elif args.command == 'monitor':
        collector = MetricCollector(max_history=args.max_history)
        print(f"🔍 Monitoring system every {args.interval} seconds...")
        print("Press Ctrl+C to stop")
        print("=" * 60)

        try:
            while True:
                metrics = collector.collect()
                print(f"\n{metrics}")

                alerts = collector.check_alerts(metrics)
                if alerts:
                    print("⚠️ Alerts:")
                    for alert in alerts:
                        print(f" - {alert}")

                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped")
            print(f"Collected {len(collector.history)} metrics")
    
    elif args.command == 'history':
        collector = MetricCollector(max_history=args.count)
        print(f"Collecting {args.count} metrics samples...")
        for i in range(args.count):
            collector.collect()
            if i < args.count - 1:
                time.sleep(1)  # Short delay to simulate time passing

        print(f"\n📜 Last {args.count} Metrics:")
        print("=" * 60)
        history = collector.get_history(count = args.count)

        for i, metric in enumerate(history, 1):
            print(f"{i}. {metric}")        


    
    elif args.command == 'export':
        # Create collector
        collector = MetricCollector(max_history=10)
        
        # Collect some metrics
        print(f"Collecting 10 metric samples for export...")
        for i in range(10):
            collector.collect()
            time.sleep(1)
        
        # Convert to JSON-serializable format
        history = collector.get_history(count=10)
        data = {
            "collected_at": datetime.now().isoformat(),
            "total_samples": len(history),
            "metrics": [m.to_dict() for m in history]  # Use to_dict() method
        }
        
        # Save to file
        with open(args.file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Exported {len(history)} metrics to {args.file}")
    

if __name__ == '__main__':
    main()