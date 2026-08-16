import os

def analyze_log(file_path):
    req_count = {}
    repeated_failure = 0
    unique_failure = 0
    errors = 0
    total_lines = 0
    length = 0
    with open(file_path, "r") as file:
        for line in file:
            total_lines += 1
            parts = line.split()
            if len(parts) > 1:
                if parts[1] == "ERROR":
                    errors += 1
                    message = " ".join(parts[3:])
                    words = message.split()
                    #print(words)
                    length = len(words)
                    req_id = words[length -1].split('=')
                    #print(req_id)
                    if req_id[1] in req_count:
                        req_count[req_id[1]] += 1
                    else:
                        req_count[req_id[1]] = 1
    repeated_failure_dic = {}
    unique_failure = len(req_count)
    for message,value in req_count.items():
        if req_count[message] >= 3:
            repeated_failure += 1
            repeated_failure_dic[message] = value
               
    return {
        "total_lines": total_lines,
        "errors": errors,
        "Unique_failure": unique_failure,
        "Repeated_failure_count": repeated_failure,
        "Repeated_failure": repeated_failure_dic
    }

directory = "C:\\Users\\Soumodeep\\Desktop\\Log_Analyzer\\sample_logs\\req_failure"

final_path = os.listdir(directory)

for items in final_path:
    if items.endswith(".log"):
        full_path = os.path.join(directory,items)
        result = analyze_log(full_path)
        print(result)
