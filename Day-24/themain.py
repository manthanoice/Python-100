from os import name
with open(r"Day-24\Input\Names\invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Day-24\Input\Letters\starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        with open("Day-24\Output\ReadyToSend\letter_for_{}.docx".format(stripped_name), mode="w") as completed_file:
            completed_file.write(new_letter)