import os

for i in range(1, 255):
    host = "172.20.0." + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
    if response == 0:
        print(host + " is up")
    else:
        print(host + " is down")