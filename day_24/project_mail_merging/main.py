#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

name_file = open("Input/Names/invited_names.txt", "r")
name_list = name_file.readlines()


letter_file = open("Input/Letters/starting_letter.txt", "r")
letter_message = letter_file.read()


for name in name_list:
    name = name.strip()
    final_text = letter_message.replace(PLACEHOLDER, name)
    with open(f"Output/ReadyToSend/{name}_letter_file.txt", "w") as letter:
        letter.write(final_text)
    

