#Ask for user input
full_name = input("Enter your full name (First, Middle, Last): ")


parts = [part.strip() for part in full_name.split(',')]

first = parts[0].capitalize()
middle = parts[1].capitalize()
last = ' '.join([word.capitalize() for word in parts[2].split()])
middle_initial = middle[0] + "."
formatted_name = f"{last}, {first} {middle_initial}"
print("Formatted Name:", formatted_name)
