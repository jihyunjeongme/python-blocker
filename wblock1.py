# Import libraries
import time
from datetime import datetime as dt

# Path to the host file, redirect to local host, list of websits to block
host_path = "/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.netflix.com", "www.facebook.com"]

# Condition
while True:
    # Check for the current time
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Rihanna")
    else:
        print("Drake")
    time.sleep(5)
