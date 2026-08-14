import os
def analyze_log(file_path):
    #count = {}
    Slow = 0
    Normal = 0
    info = 0
    log_length = 0
    slowest = 0
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if len(parts) > 1:
                if parts[1] == "INFO" and parts[3].startswith("Request") and parts[4].startswith("completed"):
                    info += 1
                    log_length = len(parts)
                    latency = parts[log_length-1].split('=')           
                    if int(latency[1][0:-2]) > 100:
                        Slow += 1
                        if slowest < int(latency[1][0:-2]):
                            slowest = int(latency[1][0:-2])
                    else:
                        Normal +=1
                                        
    return {
        "total_lines": info,
        "Slow" : Slow,
        "Normal" : Normal,
        "Longest" : slowest
    }
 
file_path = "C:\\Users\\Soumodeep\\Desktop\\Log_Analyzer\\sample_logs"  # Replace with the actual path to your log file
directory = os.listdir(file_path)
#analyzed_log = analyze_log(file_path)
total = {}
slowest = 0
for items in directory:
    full_path = os.path.join(file_path,items)
    result = analyze_log(full_path)
    if result["Longest"] > slowest:
        slowest = result["Longest"]
    for message,value in result.items():
        if message in total:
            total[message] += value
        else:
            total[message] = value

print("Slow Request Analysis")
print("=====================")
print("Total Lines:", total["total_lines"])
print("Slow Request:", total["Slow"])
print("Normal Request:", total["Normal"])

Slow_request_percentage = (total["Slow"]/ total["total_lines"]) * 100
print("Slow request rate:", Slow_request_percentage)
print(f"Slowest request: {slowest}ms" )
