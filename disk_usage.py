import os 

def disk_usage(file_path):
    with open(file_path,"r") as file:
        count = {}
        
        for line in file:
            parts = line.split()
            server_id = parts[2]
            usage = int(parts[4].split("=")[1].replace("%", ""))
            if server_id not in count:
                count[server_id] = {
                    "usage": usage,
                    "total": 1,
                    "max": usage,
                    "min": usage,
                    "Times Above 80": 1 if usage > 80 else 0
                }
            else:
                count[server_id]["usage"] += usage
                count[server_id]["total"] += 1
                if usage > count[server_id]["max"]:
                    count[server_id]["max"] = usage

                if usage < count[server_id]["min"]:
                    count[server_id]["min"] = usage

                if usage > 80:
                    count[server_id]["Times Above 80"] += 1

    return count

file_path = "C:\\Users\\Soumodeep\\Desktop\\Log_Analyzer\\sample_logs\\Disk_Usage"
directory = os.listdir(file_path)
final_result = {}
for items in directory:
    full_path = os.path.join(file_path,items)
    result = disk_usage(full_path)
    for key,value in result.items():
        if key in final_result:
            final_result[key]["usage"] += value["usage"]
            final_result[key]["total"] += value["total"]
            if value["max"]> final_result[key]["max"]:
                final_result[key]["max"] = value["max"]
            if value["min"] < final_result[key]["min"]:
                final_result[key]["min"] = value["min"]
        else:
            final_result[key] = value.copy()

for key,value in final_result.items():
    average = final_result[key]["usage"]/ final_result[key]["total"]
    if average < 70:
        final_result[key]["Status"] = "Healthy"
    elif average >= 70 and average < 80:
        final_result[key]["Status"] = "Warning"
    elif average >= 80:
        final_result[key]["Status"] = "Critical"

for key,value in final_result.items(): 
    print(key, value )
