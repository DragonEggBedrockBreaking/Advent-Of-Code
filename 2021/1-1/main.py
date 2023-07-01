with open('data.txt', 'r', encoding="utf-8") as f: data = f.read().splitlines()  # Gets input from data.txt
print(len([value > data[index - 1] for index, value in enumerate(data) if (index != 0) and (value > data[index - 1])]))  # Creates a list of increments and prints it
