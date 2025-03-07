import os, tempfile, zipfile
from datetime import datetime

def write_log(message):
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, 'app.log')
    with open(log_file, 'a') as file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{timestamp} - {message}\n")
    print(f"Log written: {message}")
    
def read_log(offset, length):
    log_file = 'logs/app.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            file.seek(offset)
            data = file.read(length)
            print(f"Read data: {data}")
    else:
        print("Log file does not exists")
        
def search_in_log(pattern):
    log_file = "logs/app.log"
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            for line in file:
                if pattern in line:
                    print(f"Found pattern: {line.strip()}")
    else:
        print("Log file does not exists")

def process_with_temp_file(data: str):
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(data.encode())
        temp_file.seek(0)
        processed_data = temp_file.read().decode()
        print(f"Processed data: {processed_data}")
                


# 예제 실행
write_log("Application started")
write_log("An error occurred")


read_log(0, 50)

search_in_log("error")

process_with_temp_file("Temporary data processing")