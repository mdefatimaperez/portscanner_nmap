# portscanner_nmap
This repository contains a port scanner made in Python.

# Nmap Port Scanner

This Python script scans ports of a given target using the `nmap3` library.

## Dependencies

*   Python 3.x
*   `nmap3` library: Install with `pip install nmap3`

## Usage Examples

* bash
python portscammer_nmap.py <target> [-p <ports>] [-o <output_file>]

# Scan top ports of a domain:
python portscammer_nmap.py scanme.nmap.org

# Scan ports 80 and 443 of an IP address:
python portscammer_nmap.py 192.168.1.1 -p 80,443

# Scan top ports and save the output to my_scan.txt:
python portscammer_nmap.py www.example.com -o my_scan.txt

# Scan specific ports of a domain and save results to a JSON file:
python portscammer_nmap.py www.example.com -p 22,80,443 -o output.json

##Options:

<target>: IP address or domain to scan.

-p <ports> or --puertos <ports>: Ports to scan (top or comma-separated list).

-o <output_file> or --output <output_file>: File to save results (default: resultados.txt).
