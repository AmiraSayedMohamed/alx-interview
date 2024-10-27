#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

 """Generates a single log entry as a string."""  
 ip = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"  
 timestamp = time.strftime("%d/%b/%Y %H:%M:%S", time.localtime())  
 request = f"GET /{random.choice(['index.html', 'about.html', 'contact.html'])} HTTP/1.1"  
 status_code = random.choice(['200', '301', '400', '401', '403', '404', '405', '500'])  
 file_size = random.randint(100,10000)  
 return f"{ip} - [{timestamp}] \"{request}\" {status_code} {file_size}"  

def main():  
 """Main function to continuously generate log entries."""  
 try:  
 while True:  
 print(generate_log_entry())  
 time.sleep(0.5) # Adjust the sleep time as needed except KeyboardInterrupt:  
 sys.exit(0)  

if __name__ == "__main__":  
 main()
