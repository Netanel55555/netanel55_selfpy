def actions_on_file():
    file_path = input("Enter a file path: ")
    action = input("Enter a task: ")

    inout_file = open(file_path, "rt")

    if action == "sort":
        words = []
        for line in inout_file:
            words.extend(line.split())

        words.sort()
        print(words)

    elif action == "rev":
        for line in inout_file:
            print(line.strip()[::-1])

    elif action == "last":
        n = int(input("Enter a number: "))
        lines = inout_file.readlines()

        for line in reversed(lines):
            if n == 0:
                break
            n -= 1
            print(line.strip())

    inout_file.close()

# This will run your function
actions_on_file()
