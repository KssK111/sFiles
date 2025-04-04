import os

current_path = "."

while True:
    elements = os.listdir(current_path)
    folders = ['..']
    files = []
    commands = [
        {'q': ['os.system(f"start cmd /K \\"cd {current_path}\\"")', 'quit()']}
    ]

    for i in range(len(elements)):
        if os.path.isdir(os.path.join(current_path, elements[i])):
            folders.append(elements[i])
        else:
            files.append(elements[i])

    elements = folders + files
    for i in range(len(elements)):
        print(f"{len(elements) - i} - {elements[-1 - i]}")
    print("q - quit with path")

    while True:
        selected_element = input("Select a directory or a file: ")
        for command in commands:
            if selected_element == list(command.keys())[0]:
                for execution in list(command[selected_element]):
                    exec(execution)
                break

        try:
            selected_element = (int)(selected_element)
            if (1 <= selected_element <= len(elements)):
                if elements[selected_element - 1] in folders:
                    current_path = os.path.join(current_path, elements[selected_element - 1])
                    break
                else:
                    os.system(f'start cmd /K "start {os.path.join(current_path, elements[selected_element - 1])} && exit"')
                    quit()
            else:
                print("Entered value is invalid")
        except ValueError:
            print("Entered value is invalid")