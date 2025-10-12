import subprocess
import socket
import re
import sys
"""FUNCTION get_default_gateway():
    RUN command "ip route show default"
    PARSE output to extract gateway IP
    RETURN gateway IP"""

def get_default_gateway():
    try:
        command = ["ip", "route", "show", "default"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.strip()

        if not output:
            print("No default route found.")
            return None
        
        words = output.split()
        via_index = words.index("via")
        gateway_ip = words[via_index + 1]
        return gateway_ip
    except FileNotFoundError:
        print("The 'ip' command is not found. Please ensure it is installed and available in your PATH.")
        return None
    except subprocess.CalledProcessError:
        print("Error: No default route found or command failed.")
        return None
    except (ValueError, IndexError):
        print("Error: Could not parse the output of 'ip route'. The format may be unexpected.")
        return None
    
"""
FUNCTION get_local_ip():
    RUN command "ip addr show"
    PARSE output to find first non-loopback IP
    RETURN IP address and interface name
"""
def get_local_ip():
    try:
        command = ["ip" , "addr", "show"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.strip()
        if not output:
            print("No network interfaces found.")
            return None, None
        current_interface = None
        words = output.split()
        for line in words:
            if line[0].isdigit() and ':' in line:
                match = re.search(r'\d+:\s+([\w.-]+):', line)
                if match:
                    current_interface = match.group(1)
                continue
            line_stripped = line.strip()
            if line_stripped.startswith("inet ") and current_interface != "lo":
                ip_addr = line_stripped.split()[1].split('/')[0]
                return ip_addr, current_interface
        print("No non-loopback IP address found.")
        print("Warning: No non-loopback IP address found.")
        return None, None
    except FileNotFoundError:
        print("The 'ip' command is not found. Please ensure it is installed and available in your PATH.")
        return None
    except subprocess.CalledProcessError:
        print("Error: the command 'ip addr show' failed.")
        return None
    except (ValueError, IndexError):
        print("Error: Could not parse the output of 'ip addr show'. The format may be unexpected.")
        return None

"""
FUNCTION ping_host(host, count=3):
    RUN command "ping -c {count} -W 2 {host}"
    CHECK if ping was successful
    RETURN True/False and average latency
"""
def ping_host(host, count=3):
    try:
        command = ["ping", "-c", str(count), "-W", "2", host]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        output = result.stdout.strip()
        if result.returncode != 0:
            return False, None
        
        words = output.split()
        for line in words:
            if "time=" in line:
                match = re.search(r'time=([\d.]+) ms', line)
                if match:
                    latency = float(match.group(1))
                    return True, latency

    except FileNotFoundError:
        print("The 'ping' command is not found. Please ensure it is installed and available in your PATH.")
        return None
    except subprocess.CalledProcessError:
        print("Error: the command 'ping -c {count} -W 2 {host}' failed.")
        return None
    except (ValueError, IndexError):
        print("Error: Could not parse the output of 'ping -c {count} -W 2 {host}'. The format may be unexpected.")
        return None
    
"""
FUNCTION resolve_dns(hostname):
    TRY to resolve hostname using socket.getaddrinfo()
    RETURN resolved IP or None
"""

def resolve_dns(hostname):
    try:
        addr_info = socket.getaddrinfo(hostname, None)
        if addr_info:
            return addr_info[0][4][0]
        else:
            print(f"DNS resolution failed for {hostname}.")
            return None
    except socket.gaierror:
        print(f"DNS resolution failed for {hostname}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during DNS resolution: {e}")
        return None

"""
FUNCTION run_diagnostics():
    PRINT "Starting Network Diagnostics..."
"""
def run_diagnostics():
    print("Starting Network Diagnostics...")
    """
    # Test 1: Local Configuration
    GET local IP and interface
    IF no IP found:
        REPORT error and EXIT
    ELSE:
        REPORT success with IP details
    """
    ip, interface = get_local_ip()
    if not ip:
        print("Error: No non-loopback IP address found. Please check your network configuration.")
        sys.exit(1)
    else:
        print(f"Local IP Address: {ip} on Interface: {interface}")

    """
    # Test 2: Gateway Connectivity
    GET default gateway
    IF no gateway found:
        REPORT error
    ELSE:
        PING gateway
        REPORT results
    """
    gateway_ip = get_default_gateway()
    if not gateway_ip:
        print("Error: No default gateway found. Please check your network configuration.")
    else:
        print(f"Default Gateway IP: {gateway_ip}")
        success, latency = ping_host(gateway_ip)
        if success:
            print(f"Successfully pinged gateway {gateway_ip} with average latency {latency} ms")
        else:
            print(f"Failed to ping gateway {gateway_ip}")

    """
    # Test 3: External Connectivity
    PING 8.8.8.8
    REPORT results
    """
    success, latency = ping_host("8.8.8.8")
    if success:
        print(f"Successfully pinged 8.8.8.8 with average latency {latency} ms")
    else:
        print("Failed to ping 8.8.8.8")

    """
    # Test 4: DNS Resolution
    RESOLVE google.com
    IF resolution fails:
        REPORT DNS error
    ELSE:
        PING resolved IP
        REPORT results
    """
    resolved_ip = resolve_dns("google.com")
    if not resolved_ip:
        print("DNS resolution failed for google.com")
    else:
        print(f"google.com resolved to {resolved_ip}")
        success, latency = ping_host(resolved_ip)
        if success:
            print(f"Successfully pinged google.com ({resolved_ip}) with average latency {latency} ms")
        else:
            print(f"Failed to ping google.com ({resolved_ip})")
    
    """
    # Generate Summary
    DISPLAY summary of all tests
    IF any test failed:
        PROVIDE troubleshooting suggestions
    """
    print("Network Diagnostics Completed.")
    print("Summary:")
    print(f"Local IP Address: {ip} on Interface: {interface}")
    if gateway_ip:
        print(f"Default Gateway IP: {gateway_ip}")
    else:
        print("Default Gateway: Not Found")
    print("Ping to Gateway: " + ("Success" if success else "Failed"))
    print("Ping to 8.8.8.8: " + ("Success" if success else "Failed"))
    print("DNS Resolution for google.com: " + ("Success" if resolved_ip else "Failed"))
    if not success:
       print("Troubleshooting Suggestions:")
       print("- Check your internet connection.")
       print("- Ensure that the target host is reachable.")
       print("- Verify DNS settings.")


"""
MAIN:
    RUN run_diagnostics()
"""
if __name__ == "__main__":
    run_diagnostics()