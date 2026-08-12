import os 

def analyze_log(file_path):
    count = {}
    errors = 0
    total_lines = 0
    with open(file_path, "r") as file:
        for line in file:
            total_lines += 1
            parts = line.split()
            if len(parts) > 1:
                if parts[1] == "ERROR":
                    errors += 1
                    message = " ".join(parts[3:])
                    words = message.split()
                    new_words = []
                    if "=" in message:
                        for word in words:
                            if "=" not in word:
                                new_words.append(word)
                        new_message = " ".join(new_words)
                    else:
                        new_message = message

                    if new_message in count:
                        count[new_message] += 1
                    else:
                        count[new_message] = 1

    return {
        "total_lines": total_lines,
        "errors": errors,
        "error_summary": count
    }

directory = "path"
content_list = os.listdir(directory)
result = {}
total_logs = 0
total_errors = 0
error_rate = 0

for items in content_list:
    if items.endswith(".log"):
        full_path = os.path.join(directory,items)
        analyze = analyze_log(full_path)
        total_logs += analyze["total_lines"]
        total_errors += analyze["errors"]
        
        for message, number in analyze["error_summary"].items():
            if message in result:
                result[message] += number
            else:
                result[message] = number    

error_rate = (total_errors/total_logs) * 100

print("Multi Log Health Report")
print("===============")            
print("Total lines:", total_logs)
print("Total errors:" , total_errors)
print("Error rate:", error_rate)

if error_rate < 5:
    print("Status: Healthy")
elif error_rate >= 5 and error_rate < 10:
    print("Status: Warning")
elif error_rate >= 10:
    print("Status: Critical")


print("Most Common Error:\n")
max_count = 0
max_message = ""
for message, value in result.items():

    if result[message] > max_count:
        max_count = result[message]
        max_message = message

print(f"{max_message}: {max_count}")