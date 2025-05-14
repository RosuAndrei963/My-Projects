PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for n in names:
        stripped_name = n.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

