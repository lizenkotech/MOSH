# command = ""
# while command != "quit"

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
