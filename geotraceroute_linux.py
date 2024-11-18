#!/usr/bin/env python3
import sys, subprocess

def traceroute_with_city():
    try:
        hostname = sys.argv[1]
        print(f"traceroute to {hostname}")
    except:
        print("traceroute: missing host operand")
        exit()
    command = ["traceroute", hostname]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True).stdout
    for line in process:
        if line.startswith("  ") and (line.count("*") != 3) and (ip := line.split()[1]):
                url = f"http://ip-api.com/csv/{ip}"
                data = subprocess.run(["curl", "-s", url], capture_output=True, text=True).stdout.split(",")
                try:
                    print(f"{line.strip()} {data[5]}, {data[3]}, {data[2]}")
                except:
                    print(f"{line.strip()}")

if __name__ == "__main__":
    try:
        traceroute_with_city()
    except KeyboardInterrupt:
        exit()
