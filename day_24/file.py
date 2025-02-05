# with python we can read, edit any file or create any new file

with open("file.csv") as file:          # here default mode is read so it cant make any changes into file for that we need to change the mode
    content = file.read()
    # print(content)

with open("file.csv", mode="a") as file:       #mode 'w' vanish all existing data and add new data
    file.write("new text")                     # mode "a" lets you add new data without vanishing old data
    print(file)



