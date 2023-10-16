import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(value[2])

    pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# print(student_data_frame.iterrows())
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(row.student)
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
# #--------------------------------------------------------------------------------
# # TODO 1. Create a dictionary in this format:
alphabets = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {
    row.letter: row.code for (index, row) in alphabets.iterrows()
}


print(new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def func():
    input_1 = input("Enter the name?:").upper()
    try:
        new_list = [new_dict[value] for value in input_1]
        # print(new_list)
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        func()
    else:
        print(new_list)


func()
