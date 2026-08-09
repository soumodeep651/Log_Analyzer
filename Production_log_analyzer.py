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


file_path = "production.log"  # Replace with the actual path to your log file
result = analyze_log(file_path)
print("Total lines:", result["total_lines"])
print("Errors:", result["errors"])
print("Error summary:")

for message, count in result["error_summary"].items():
    print(f"  {message}: {count}")