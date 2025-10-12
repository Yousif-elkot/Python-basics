#!/usr/bin/env python3
"""
Network Diagnostics Toolkit
A comprehensive network troubleshooting tool that checks:
- Local IP configuration
- Gateway connectivity
- External connectivity
- DNS resolution
"""

import subprocess
import socket
import re
import sys

# ANSI color codes for better output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_success(message):
    """Print success message with checkmark"""
    print(f"{Colors.GREEN}✓{Colors.RESET} {message}")

def print_error(message):
    """Print error message with X mark"""
    print(f"{Colors.RED}✗{Colors.RESET} {message}")

def print_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠{Colors.RESET} {message}")

def print_section(title):
    """Print section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}═══ {title} ═══{Colors.RESET}")


def get_default_gateway():
    """
    Get the default gateway IP address.
    
    Returns:
        str: Gateway IP address or None if not found
    """
    try:
        command = ["ip", "route", "show", "default"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        output = result.stdout.strip()

        if not output:
            return None
        
        # Parse: "default via 192.168.1.1 dev eth0"
        match = re.search(r'default via ([\d.]+)', output)
        if match:
            return match.group(1)
        
        return None
        
    except FileNotFoundError:
        print_error("The 'ip' command is not found. Is this a Linux system?")
        return None
    except subprocess.CalledProcessError:
        return None
    except subprocess.TimeoutExpired:
        print_error("Command timeout while getting default gateway")
        return None
    except Exception as e:
        print_error(f"Unexpected error getting gateway: {e}")
        return None


def get_local_ip():
    """
    Get the first non-loopback IP address and its interface.
    
    Returns:
        tuple: (ip_address, interface_name) or (None, None) if not found
    """
    try:
        command = ["ip", "addr", "show"]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=5
        )
        output = result.stdout
        
        if not output:
            return None, None
        
        # Split by lines and process
        lines = output.split('\n')
        current_interface = None
        
        for line in lines:
            # Match interface name: "2: eth0: <BROADCAST,MULTICAST,UP>"
            interface_match = re.match(r'^\d+:\s+([\w.-]+):', line)
            if interface_match:
                current_interface = interface_match.group(1)
                continue
            
            # Match IP address: "    inet 192.168.1.50/24"
            if 'inet ' in line and current_interface and current_interface != "lo":
                ip_match = re.search(r'inet ([\d.]+)/\d+', line)
                if ip_match:
                    return ip_match.group(1), current_interface
        
        return None, None
        
    except FileNotFoundError:
        print_error("The 'ip' command is not found. Is this a Linux system?")
        return None, None
    except subprocess.CalledProcessError:
        return None, None
    except subprocess.TimeoutExpired:
        print_error("Command timeout while getting local IP")
        return None, None
    except Exception as e:
        print_error(f"Unexpected error getting local IP: {e}")
        return None, None


def ping_host(host, count=3):
    """
    Ping a host and return success status with average latency.
    
    Args:
        host (str): Hostname or IP address to ping
        count (int): Number of pings to send
    
    Returns:
        tuple: (success: bool, avg_latency: float or None)
    """
    try:
        command = ["ping", "-c", str(count), "-W", "2", host]
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Check if ping succeeded
        if result.returncode != 0:
            return False, None
        
        output = result.stdout
        
        # Parse average latency from: "rtt min/avg/max/mdev = 10.2/15.5/20.1/4.2 ms"
        match = re.search(r'rtt min/avg/max/[a-z]+ = [\d.]+/([\d.]+)/[\d.]+/[\d.]+ ms', output)
        if match:
            avg_latency = float(match.group(1))
            return True, avg_latency
        
        # If we can't parse latency but ping succeeded
        return True, None
        
    except FileNotFoundError:
        print_error("The 'ping' command is not found")
        return False, None
    except subprocess.TimeoutExpired:
        return False, None
    except Exception as e:
        print_error(f"Unexpected error during ping: {e}")
        return False, None


def resolve_dns(hostname):
    """
    Resolve a hostname to an IP address using DNS.
    
    Args:
        hostname (str): Hostname to resolve
    
    Returns:
        str: Resolved IP address or None if resolution failed
    """
    try:
        addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET)
        if addr_info:
            return addr_info[0][4][0]
        return None
        
    except socket.gaierror:
        return None
    except Exception as e:
        print_error(f"Unexpected error during DNS resolution: {e}")
        return None


def run_diagnostics():
    """
    Run comprehensive network diagnostics and display results.
    """
    print(f"\n{Colors.BOLD}{'='*50}")
    print("    🌐 NETWORK DIAGNOSTICS TOOLKIT")
    print(f"{'='*50}{Colors.RESET}\n")
    
    # Store all test results
    results = {
        'local_ip': None,
        'interface': None,
        'gateway_ip': None,
        'gateway_ping': False,
        'external_ping': False,
        'dns_resolution': False,
        'dns_ip': None,
        'dns_ping': False
    }
    
    # ═══════════════════════════════════════════════
    # Test 1: Local Configuration
    # ═══════════════════════════════════════════════
    print_section("Local Configuration")
    
    ip, interface = get_local_ip()
    if not ip or not interface:
        print_error("No non-loopback IP address found")
        print_warning("Cannot proceed without network interface")
        sys.exit(1)
    
    results['local_ip'] = ip
    results['interface'] = interface
    print_success(f"IP Address: {Colors.BOLD}{ip}{Colors.RESET} on interface {Colors.BOLD}{interface}{Colors.RESET}")
    
    # ═══════════════════════════════════════════════
    # Test 2: Gateway Connectivity
    # ═══════════════════════════════════════════════
    print_section("Gateway Connectivity")
    
    gateway_ip = get_default_gateway()
    if not gateway_ip:
        print_error("No default gateway found")
        print_warning("You may not be able to reach external networks")
        results['gateway_ip'] = None
    else:
        results['gateway_ip'] = gateway_ip
        print(f"Gateway: {gateway_ip}")
        print("Testing gateway connectivity...", end=" ")
        sys.stdout.flush()
        
        success, latency = ping_host(gateway_ip)
        results['gateway_ping'] = success
        
        if success:
            latency_str = f"{latency:.1f}ms" if latency else "unknown latency"
            print_success(f"Gateway reachable ({latency_str})")
        else:
            print_error("Cannot reach gateway")
    
    # ═══════════════════════════════════════════════
    # Test 3: External Connectivity
    # ═══════════════════════════════════════════════
    print_section("External Connectivity")
    
    print("Testing connection to 8.8.8.8 (Google DNS)...", end=" ")
    sys.stdout.flush()
    
    success, latency = ping_host("8.8.8.8")
    results['external_ping'] = success
    
    if success:
        latency_str = f"{latency:.1f}ms" if latency else "unknown latency"
        print_success(f"Internet reachable ({latency_str})")
    else:
        print_error("Cannot reach external network")
    
    # ═══════════════════════════════════════════════
    # Test 4: DNS Resolution
    # ═══════════════════════════════════════════════
    print_section("DNS Resolution")
    
    print("Resolving google.com...", end=" ")
    sys.stdout.flush()
    
    resolved_ip = resolve_dns("google.com")
    if not resolved_ip:
        print_error("DNS resolution failed")
        results['dns_resolution'] = False
    else:
        results['dns_resolution'] = True
        results['dns_ip'] = resolved_ip
        print_success(f"Resolved to {resolved_ip}")
        
        print("Testing connection to resolved IP...", end=" ")
        sys.stdout.flush()
        
        success, latency = ping_host(resolved_ip)
        results['dns_ping'] = success
        
        if success:
            latency_str = f"{latency:.1f}ms" if latency else "unknown latency"
            print_success(f"Host reachable ({latency_str})")
        else:
            print_error("Resolved IP not reachable")
    
    # ═══════════════════════════════════════════════
    # Summary & Diagnostics
    # ═══════════════════════════════════════════════
    print_section("Summary")
    
    print(f"\n{Colors.BOLD}Network Status:{Colors.RESET}")
    print(f"  Local IP:         {results['local_ip']} ({results['interface']})")
    print(f"  Gateway:          {results['gateway_ip'] or 'Not found'}")
    print(f"  Gateway Ping:     {'✓ Pass' if results['gateway_ping'] else '✗ Fail'}")
    print(f"  External Ping:    {'✓ Pass' if results['external_ping'] else '✗ Fail'}")
    print(f"  DNS Resolution:   {'✓ Pass' if results['dns_resolution'] else '✗ Fail'}")
    print(f"  DNS Host Ping:    {'✓ Pass' if results['dns_ping'] else '✗ Fail'}")
    
    # Determine overall health
    all_passed = (results['gateway_ping'] and results['external_ping'] and 
                  results['dns_resolution'] and results['dns_ping'])
    
    if all_passed:
        print(f"\n{Colors.GREEN}{Colors.BOLD}✓ All tests passed! Network is healthy.{Colors.RESET}\n")
        return 0
    
    # Provide troubleshooting suggestions
    print(f"\n{Colors.YELLOW}{Colors.BOLD}⚠ Issues detected. Troubleshooting suggestions:{Colors.RESET}\n")
    
    if not results['gateway_ip']:
        print("  • No default gateway configured")
        print("    → Check your network configuration (DHCP or static IP)")
        print("    → Run: sudo dhclient (for DHCP) or configure manually\n")
    
    if results['gateway_ip'] and not results['gateway_ping']:
        print("  • Gateway not reachable")
        print("    → Check physical connection (cable/WiFi)")
        print("    → Verify gateway IP is correct")
        print(f"    → Try: ip route show\n")
    
    if results['gateway_ping'] and not results['external_ping']:
        print("  • Local network OK, but no internet access")
        print("    → Gateway may not have internet connection")
        print("    → Check router/firewall settings")
        print("    → Verify NAT is configured on gateway\n")
    
    if not results['dns_resolution']:
        print("  • DNS resolution failing")
        print("    → Check /etc/resolv.conf for valid nameservers")
        print("    → Try: cat /etc/resolv.conf")
        print("    → Consider using 8.8.8.8 or 1.1.1.1 as DNS\n")
    
    if results['dns_resolution'] and not results['dns_ping']:
        print("  • DNS works but resolved IP not reachable")
        print("    → May be a routing or firewall issue")
        print("    → Check firewall rules: sudo iptables -L\n")
    
    return 1


def main():
    """Main entry point"""
    try:
        exit_code = run_diagnostics()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Diagnostics interrupted by user{Colors.RESET}")
        sys.exit(130)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()