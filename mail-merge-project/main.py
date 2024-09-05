"""merge mail"""

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", encoding="utf-8") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", encoding="utf8") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w", \
                  encoding="utf8") as completed_letter:
            completed_letter.write(new_letter)
