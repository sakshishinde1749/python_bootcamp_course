student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

student = []
score = []
#Looping through dictionaries:
for (key, value) in student_dict.items():
    student.append(key)
    score.append(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

word_dict = {row.letter : row.code for (index, row) in data.iterrows()}
print(word_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("write any word: ").upper()
    try:
        output_list = [word_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet pls")
        generate_phonetic
    else:
        print(output_list)
    
generate_phonetic()