from datetime import datetime

log_file_path = "application.log"

current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[{timestamp}] INFO: This is a log entry"

try:
    with open(log_file_path, "a", encoding="utf-8") as file:
        file.write(log_entry + "\n")
    print("Log entry added successfully")
except Exception as e:
    print(f"Failed to write log: {e}")
