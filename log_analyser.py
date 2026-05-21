# Analyses log files 

# Written by Ashraf Awaiz
# 21-05-2026

def open_log_file(filename): 
    with open(filename) as file: 
        for line in file:
            if "failed" in line:
                print (line)

open_log_file("auth.log")
