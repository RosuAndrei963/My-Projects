import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for index, row in alphabet_df.iterrows()}
print(alphabet_dict)

def gen_phonetic():
    input_word = input("Enter a word: ")
    try:
        output_list = [alphabet_dict[letter.upper()] for letter in input_word]
    except KeyError:
        print("Only letters accepted.")
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()
