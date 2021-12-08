# Day 22
# Date : 06 Dec 2021
# Mail Merge Project 

PLACEHOLDER = "[name]"

with open("Day_22/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    

with open("Day_22\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        with open(f"Day_22\Output\ReadyToSend\letter_for_{stripped_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)

