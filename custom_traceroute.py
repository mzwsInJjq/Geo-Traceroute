import os
import subprocess

def get_city_name(ip):
    url = f"http://ip-api.com/csv/{ip}"
    stream = os.popen(f"curl -s {url}")
    print(stream.read())
    data = stream.read().split(',')
    return f"{data[5]}, {data[3]}, {data[2]}"

def traceroute_with_city():
    hostname = input("traceroute to: ")
    #command = ['traceroute', '-w', '1000', '-n', hostname] if not subprocess._mswindows else ['tracert', '-w', '1000', '-d', hostname]
    command = ['tracert', '-w', '1000', '-d', hostname]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
    for line in process.stdout:
        if line.startswith(' ') and (ip := line.split()[-1]) != "out.":               
            print(f"{line.strip()} {get_city_name(ip)}")

if __name__ == '__main__':
    traceroute_with_city()