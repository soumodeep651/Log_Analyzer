import os
from datetime import datetime
def analyze_log(file_path):
    count = {}
    errors = 0
    total_lines = 0
    with open(file_path, "r") as file:
        for line in file:
            total_lines += 1
            parts = line.split()
            timestamp = datetime.strptime(parts[0],"%Y-%m-%dT%H:%M:%S")
            #print(timestamp.hour)
            #print(timestamp.minute)
            minute = (timestamp.minute//5)*5
            bucket = timestamp.replace(minute=minute, second= 0, microsecond= 0)
            
            if bucket not in count:
                count[bucket] = {
                    "total" : 0,
                    "errors" : 0
                }
            if parts[1] == "ERROR":
                count[bucket]["errors"] += 1

            count["total"] += 1

        print(count)



            
    return {
        "total_lines": total_lines,
        "errors": errors,
        "error_summary": count
    }

file_path = "C:\\Users\\Soumodeep\\Desktop\\Log_Analyzer\\sample_logs\\Error_Spikes"
directory = os.listdir(file_path)
for items in directory:
    full_path = os.path.join(file_path,items)
    result = analyze_log(full_path)