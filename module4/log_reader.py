
# Create and write a log file
file = open("log.txt", "w")

file.write("Application started\n")
file.write("User logged in\n")
file.write("File opened successfully\n")
file.write("Application closed\n")

file.close()

# Read the log file
file = open("log.txt", "r")

print("Log File Contents:")

for line in file:
    print(line.strip())

file.close()
