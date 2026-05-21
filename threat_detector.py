# Detects malware in file

# Created by Ashraf Awaiz

def malware_file(filename):
    with open(filename) as file:
        for line in file:
            if "malware" in line:
                print (line)

malware_file("system.log")