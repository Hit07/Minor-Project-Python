# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt",mode= "r+") as file:
    b = file.read()
    a = file.readline()
with open("./Input/Names/invited_names.txt",mode="r+") as new:
    c = new.readlines()
    for i in c:
        with open(f"./Output/ReadyToSend/letter_to_{i.strip()}.txt", mode="w") as file2:
            d = b.replace(f"[name]",f"{i.strip()}")
            file2.write(d)

















