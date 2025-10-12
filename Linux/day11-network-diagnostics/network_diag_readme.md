# 🌐 Network Diagnostics Toolkit

A comprehensive Python-based network troubleshooting tool for Linux systems that automates common diagnostic tasks.

## 🎯 Purpose

This tool performs systematic network diagnostics to quickly identify connectivity issues. It's designed for:
- System administrators troubleshooting server connectivity
- DevOps engineers debugging deployment issues
- Anyone needing quick network health checks

## ✨ Features

The script performs four key diagnostic tests:

1. **Local Configuration Check**
   - Identifies your primary network interface
   - Displays your local IP address
   
2. **Gateway Connectivity Test**
   - Finds your default gateway
   - Tests connectivity with latency measurement

3. **External Connectivity Test**
   - Pings 8.8.8.8 (Google DNS) to verify internet access
   - Measures round-trip latency

4. **DNS Resolution Test**
   - Resolves google.com to verify DNS functionality
   - Tests connectivity to the resolved IP

---

## 📂 Project Structure

```
network-diagnostics/
├── README.md              # This file
├── network_diag_v1.py     # Initial implementation (functional with bugs)
└── network_diag_v2.py     # Refined version (production-ready)
```

### Version History

- **v1**: Initial implementation following the V.P.C.R. pseudocode
- **v2**: Production-ready version with bug fixes and UX improvements

---

## 🚀 Usage

### Basic Usage

```bash
# Run the refined version (recommended)
python3 network_diag_v2.py

# Run the original version (educational purposes)
python3 network_diag_v1.py
```

### Prerequisites

- Linux operating system (uses `ip` and `ping` commands)
- Python 3.6+
- Standard Linux utilities: `ip`, `ping`

### Sample Output (v2)

```
==================================================
    🌐 NETWORK DIAGNOSTICS TOOLKIT
==================================================

═══ Local Configuration ═══
✓ IP Address: 192.168.1.50 on interface eth0

═══ Gateway Connectivity ═══
Gateway: 192.168.1.1
Testing gateway connectivity... ✓ Gateway reachable (2.1ms)

═══ External Connectivity ═══
Testing connection to 8.8.8.8 (Google DNS)... ✓ Internet reachable (15.3ms)

═══ DNS Resolution ═══
Resolving google.com... ✓ Resolved to 142.250.185.46
Testing connection to resolved IP... ✓ Host reachable (14.8ms)

═══ Summary ═══

Network Status:
  Local IP:         192.168.1.50 (eth0)
  Gateway:          192.168.1.1
  Gateway Ping:     ✓ Pass
  External Ping:    ✓ Pass
  DNS Resolution:   ✓ Pass
  DNS Host Ping:    ✓ Pass

✓ All tests passed! Network is healthy.
```

---

## 🔄 Version Comparison: v1 vs v2

### Overview of Changes

| Aspect | v1 (Initial) | v2 (Refined) | Impact |
|--------|-------------|--------------|--------|
| **Functionality** | Works with bugs | Fully functional | High |
| **Line Parsing** | Splits by whitespace | Splits by newlines | Critical |
| **Latency Calculation** | Returns first ping | Returns actual average | High |
| **Result Tracking** | Variables overwritten | Results dictionary | Critical |
| **User Feedback** | Plain text only | Color-coded with symbols | Medium |
| **Error Messages** | Generic | Specific troubleshooting | High |
| **Timeout Handling** | None | 5-10 second timeouts | High |
| **Progress Indicators** | None | Real-time feedback | Low |
| **Exit Codes** | Inconsistent | Proper exit codes (0/1/130) | Medium |
| **Code Organization** | Good structure | Professional structure | Medium |

---

## 🐛 Critical Bug Fixes (v1 → v2)

### Bug #1: Line Parsing Logic Error in `get_local_ip()`

**The Problem:**
```python
# ❌ v1 - INCORRECT
words = output.split()      # Splits entire output by whitespace
for line in words:          # Now looping over individual WORDS, not lines!
    if line[0].isdigit() and ':' in line:
        # This will match random words like "2:" or "123:"
```

**Why It Fails:**
- `split()` with no arguments splits by ANY whitespace (spaces, tabs, newlines)
- Destroys the line structure completely
- You're now processing individual words, making pattern matching unreliable
- `line[0].isdigit()` on a single word can match unrelated tokens

**The Fix:**
```python
# ✅ v2 - CORRECT
lines = output.split('\n')  # Splits by newlines only, preserving line structure
for line in lines:          # Now looping over actual lines!
    # Match interface line: "2: eth0: <BROADCAST,MULTICAST,UP>"
    interface_match = re.match(r'^\d+:\s+([\w.-]+):', line)
```

**Impact:** 🔴 **Critical** - v1 may fail to detect network interfaces or detect wrong ones

---

### Bug #2: Incorrect Latency Calculation in `ping_host()`

**The Problem:**
```python
# ❌ v1 - Returns FIRST ping time, not average
words = output.split()
for line in words:
    if "time=" in line:
        match = re.search(r'time=([\d.]+) ms', line)
        if match:
            latency = float(match.group(1))
            return True, latency  # ⚠️ Returns immediately on first match!
```

**Example ping output:**
```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=118 time=15.2 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=118 time=14.8 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=118 time=15.1 ms
--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 14.8/15.033/15.2/0.173 ms
                          ^^^^^ THIS is what we want!
```

**Why It Fails:**
- Returns `15.2` (first ping) instead of `15.033` (actual average)
- Not representative of overall connectivity quality
- Ignores ping's built-in statistics

**The Fix:**
```python
# ✅ v2 - Parses the actual average from statistics line
match = re.search(r'rtt min/avg/max/[a-z]+ = [\d.]+/([\d.]+)/[\d.]+/[\d.]+ ms', output)
if match:
    avg_latency = float(match.group(1))  # Gets the avg value: 15.033
    return True, avg_latency
```

**Impact:** 🟡 **High** - Provides inaccurate latency measurements

---

### Bug #3: Variable Overwriting in Summary Section

**The Problem:**
```python
# ❌ v1 - Reuses 'success' variable, losing previous results
# After Test 2 (gateway)
success, latency = ping_host(gateway_ip)

# After Test 3 (external) - OVERWRITES gateway result!
success, latency = ping_host("8.8.8.8")

# After Test 4 (DNS ping) - OVERWRITES external result!
success, latency = ping_host(resolved_ip)

# Summary section uses WRONG values
print("Ping to Gateway: " + ("Success" if success else "Failed"))    # ❌ Wrong!
print("Ping to 8.8.8.8: " + ("Success" if success else "Failed"))    # ❌ Wrong!
```

**Why It Fails:**
- Each test overwrites the `success` variable
- Summary always shows the LAST test result for ALL tests
- If DNS ping fails, it reports that gateway and external pings also failed (even if they passed)

**Example of Wrong Output:**
```
# Actual results: Gateway ✓, External ✓, DNS ✗
# v1 reports: Gateway ✗, External ✗, DNS ✗  (ALL WRONG!)
```

**The Fix:**
```python
# ✅ v2 - Store all results in a dictionary
results = {
    'gateway_ping': False,
    'external_ping': False,
    'dns_resolution': False,
    'dns_ping': False
}

# Test 2
success, latency = ping_host(gateway_ip)
results['gateway_ping'] = success  # Store independently

# Test 3
success, latency = ping_host("8.8.8.8")
results['external_ping'] = success  # Store independently

# Summary uses correct values
print(f"Gateway Ping:     {'✓ Pass' if results['gateway_ping'] else '✗ Fail'}")
print(f"External Ping:    {'✓ Pass' if results['external_ping'] else '✗ Fail'}")
```

**Impact:** 🔴 **Critical** - Summary reports completely wrong diagnostics

---

### Bug #4: Regex Pattern Issues in `get_local_ip()`

**The Problem:**
```python
# ❌ v1 - Fragile pattern matching
if line[0].isdigit() and ':' in line:
    match = re.search(r'\d+:\s+([\w.-]+):', line)
    # Problem 1: line[0] check happens BEFORE we know it's a valid line
    # Problem 2: Searching instead of matching from start of line
```

**Why It Fails:**
- `line[0].isdigit()` can throw `IndexError` on empty lines
- Searching anywhere in line instead of matching line start
- Could match unrelated content that happens to have digit and colon

**The Fix:**
```python
# ✅ v2 - Robust pattern matching
interface_match = re.match(r'^\d+:\s+([\w.-]+):', line)
if interface_match:
    current_interface = interface_match.group(1)
    # ^ matches start of line, single operation, safe
```

**Impact:** 🟡 **Medium** - Can fail on edge cases or malformed output

---

## ✨ User Experience Improvements (v1 → v2)

### 1. Color-Coded Visual Feedback

**v1 Output:**
```
Local IP Address: 192.168.1.50 on Interface: eth0
Successfully pinged gateway 192.168.1.1 with average latency 2.1 ms
Successfully pinged 8.8.8.8 with average latency 15.3 ms
```

**v2 Output:**
```
✓ IP Address: 192.168.1.50 on interface eth0
✓ Gateway reachable (2.1ms)
✓ Internet reachable (15.3ms)
```

**Implementation:**
```python
# v2 - ANSI color codes
class Colors:
    GREEN = '\033[92m'   # Success
    RED = '\033[91m'     # Error
    YELLOW = '\033[93m'  # Warning
    BLUE = '\033[94m'    # Info
    RESET = '\033[0m'    # Reset to default

def print_success(message):
    print(f"{Colors.GREEN}✓{Colors.RESET} {message}")
```

**Benefits:**
- Instant visual recognition of pass/fail
- Professional appearance
- Easier to scan results

---

### 2. Progress Indicators

**v1:** Silent execution, no feedback during long operations

**v2:** Real-time progress
```python
print("Testing gateway connectivity...", end=" ")
sys.stdout.flush()  # Force immediate output
success, latency = ping_host(gateway_ip)  # Long operation
print_success(f"Gateway reachable ({latency:.1f}ms)")  # Complete on same line
```

**Benefits:**
- Users know the script is working
- Professional feel
- Reduces perceived wait time

---

### 3. Structured Output with Sections

**v2 Implementation:**
```python
def print_section(title):
    print(f"\n{Colors.BOLD}{Colors.BLUE}═══ {title} ═══{Colors.RESET}")

print_section("Local Configuration")
print_section("Gateway Connectivity")
print_section("DNS Resolution")
```

**Benefits:**
- Clear logical flow
- Easy to parse visually
- Professional formatting

---

### 4. Comprehensive Summary Table

**v1:** Scattered results throughout output

**v2:** Consolidated summary
```
Network Status:
  Local IP:         192.168.1.50 (eth0)
  Gateway:          192.168.1.1
  Gateway Ping:     ✓ Pass
  External Ping:    ✓ Pass
  DNS Resolution:   ✓ Pass
  DNS Host Ping:    ✓ Pass
```

**Benefits:**
- Quick at-a-glance status
- Easy to copy/paste for reports
- Clear pass/fail indicators

---

### 5. Intelligent Troubleshooting Suggestions

**v1:** Generic suggestions regardless of failure type

**v2:** Context-aware diagnostics
```python
if not results['gateway_ip']:
    print("  • No default gateway configured")
    print("    → Check your network configuration (DHCP or static IP)")
    print("    → Run: sudo dhclient (for DHCP) or configure manually\n")

if results['gateway_ping'] and not results['external_ping']:
    print("  • Local network OK, but no internet access")
    print("    → Gateway may not have internet connection")
    print("    → Check router/firewall settings")
```

**Benefits:**
- Actionable next steps
- Saves troubleshooting time
- Educational for junior engineers

---

## 🛡️ Robustness Improvements (v1 → v2)

### 1. Timeout Protection

**v1:** No timeouts - can hang indefinitely
```python
result = subprocess.run(command, capture_output=True, text=True)
# If command hangs, script hangs forever
```

**v2:** Timeouts on all subprocess calls
```python
result = subprocess.run(
    command,
    capture_output=True,
    text=True,
    timeout=5  # Fails gracefully after 5 seconds
)
```

**Impact:** Prevents script from hanging on network issues

---

### 2. Better Exception Handling

**v1:** Catches exceptions but returns `None` inconsistently

**v2:** Consistent return values and error propagation
```python
try:
    # ... operation ...
except FileNotFoundError:
    print_error("The 'ip' command is not found. Is this a Linux system?")
    return None, None  # Consistent tuple return
except subprocess.TimeoutExpired:
    print_error("Command timeout")
    return None, None
```

---

### 3. Proper Exit Codes

**v2:** Unix-standard exit codes
```python
return 0   # Success
return 1   # Failure
return 130 # Interrupted (Ctrl+C)
```

**Benefits:**
- Can be used in shell scripts: `network_diag.py && echo "Network OK"`
- Proper automation integration
- Professional script behavior

---

### 4. Keyboard Interrupt Handling

**v2:** Graceful handling of Ctrl+C
```python
try:
    exit_code = run_diagnostics()
    sys.exit(exit_code)
except KeyboardInterrupt:
    print(f"\n\n{Colors.YELLOW}Diagnostics interrupted by user{Colors.RESET}")
    sys.exit(130)
```

---

## 🔧 Technical Implementation Details

### Architecture

```
get_local_ip() → Parses 'ip addr show' output
     ↓
get_default_gateway() → Parses 'ip route show default'
     ↓
ping_host() → Executes ping and parses latency
     ↓
resolve_dns() → Uses socket.getaddrinfo() for DNS
     ↓
run_diagnostics() → Orchestrates all tests and generates report
```

### Key Technologies

- **subprocess**: Execute system commands securely
  - Used with lists (not strings) to prevent shell injection
  - Captures output with `capture_output=True`
  - Timeout protection on all calls

- **socket**: DNS resolution using Python's standard library
  - `socket.getaddrinfo()` for hostname resolution
  - More reliable than parsing `dig` output

- **regex**: Parse command outputs reliably
  - `re.match()` for line-start patterns (interfaces)
  - `re.search()` for patterns anywhere in text (latency)

- **ANSI colors**: Terminal-based visual feedback
  - `\033[92m` = Green
  - `\033[91m` = Red
  - Works on all modern terminals

### Design Patterns Used

1. **Results Dictionary Pattern**: Centralized state management
2. **Helper Functions**: `print_success()`, `print_error()`, `print_section()`
3. **Early Return**: Fail fast on critical errors
4. **Defensive Programming**: Check for None/empty before processing

---

## 📊 Performance Comparison

| Metric | v1 | v2 |
|--------|----|----|
| Execution Time | ~10-15 seconds | ~10-15 seconds (same) |
| Lines of Code | ~180 | ~280 |
| Functions | 6 | 9 (added helpers) |
| Error Handlers | Basic | Comprehensive |
| User Feedback | Minimal | Rich |

---

## 🎓 V.P.C.R. Method Applied

This project was built using the **V.P.C.R. (Visualize, Pseudocode, Code, Refine)** methodology:

### 1. **Visualize**
Drew the diagnostic flow:
```
[User] → [IP Check] → [Gateway Test] → [External Test] → [DNS Test] → [Report]
```

### 2. **Pseudocode**
Wrote logic in plain English:
```
FUNCTION get_default_gateway():
    RUN command "ip route show default"
    PARSE output to extract gateway IP
    RETURN gateway IP
```

### 3. **Code** (v1)
Translated pseudocode to Python - functional but with bugs

### 4. **Refine** (v2)
- Fixed critical parsing bugs
- Added visual feedback
- Improved error handling
- Enhanced user experience

---

## 🐛 Common Issues & Solutions

### "The 'ip' command is not found"
**Solution:** This is a Linux-only tool
```bash
# Ubuntu/Debian
sudo apt install iproute2

# Arch Linux (should already have it)
sudo pacman -S iproute2
```

### "No non-loopback IP address found"
**Solution:** Network interface is down
```bash
# Check interfaces
ip link show

# Bring interface up
sudo ip link set eth0 up

# Request DHCP
sudo dhclient eth0
```

### "No default gateway found"
**Solution:** Gateway not configured
```bash
# View routes
ip route show

# Add default gateway
sudo ip route add default via 192.168.1.1
```

---

## 📚 Learning Outcomes

### Networking Concepts
- ✅ TCP/IP model (4 layers)
- ✅ IP addressing and routing
- ✅ DNS resolution process
- ✅ ICMP (ping) protocol
- ✅ Default gateway role

### Python Skills
- ✅ Subprocess command execution
- ✅ Regex for parsing structured text
- ✅ Socket programming for DNS
- ✅ Dictionary-based state management
- ✅ ANSI escape codes for colors
- ✅ Exception handling patterns

### Software Engineering
- ✅ V.P.C.R. methodology
- ✅ Iterative refinement (v1 → v2)
- ✅ User experience design
- ✅ Error handling strategies
- ✅ Code documentation
- ✅ Version control practices

---

## 🎯 Part of 60-Day Cloud Engineer Roadmap

**Week 2, Day 11**: Networking Deep Dive

This project consolidates:
- `ip` command mastery (`ip addr`, `ip route`)
- DNS resolution with `dig` and socket programming
- Network troubleshooting methodology
- Automation of diagnostic procedures

---

## 🚀 Future Enhancements

Potential improvements for v3:
- [ ] Add IPv6 support
- [ ] Test multiple DNS servers (8.8.8.8, 1.1.1.1, 9.9.9.9)
- [ ] Check firewall rules (iptables)
- [ ] Export results to JSON/CSV
- [ ] Add traceroute functionality
- [ ] Measure packet loss percentage
- [ ] Test specific ports (SSH, HTTP, HTTPS)
- [ ] Web-based dashboard
- [ ] Historical logging and trending

---

## 📄 License

This is an educational project created as part of a cloud engineering learning path.

---

## 🤝 Acknowledgments

Built following the **60-Day Cloud Engineer Roadmap** with emphasis on:
- Professional code quality
- Real-world applicability
- Comprehensive documentation
- Learning through iteration

---

**Author**: Yousif-Elkot  
**Date**: October 2025  
**Week**: 2/8 Complete ✓  
**Day**: 11/60 Complete ✓