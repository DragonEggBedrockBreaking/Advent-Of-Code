from requests_html import HTMLSession
print(HTMLSession().get('https://adventofcode.com/2021/day/1/input').text)
data  = HTMLSession().get('https://adventofcode.com/2021/day/1/input').html.find('body', first=True).text.splitlines() # Gets all data from website
# with open('data.txt', 'r', encoding="utf-8") as f: data = f.read().splitlines()  # Gets input from data.txt
sums = [sum((int(value), int(data[index + 1]), int(data[index + 2]))) for index, value in enumerate(data) if index < len(data) - 2]  # Creates a list of sums
print(len([value > sums[index - 1] for index, value in enumerate(sums) if (index != 0) and (value > sums[index - 1])]))  # Creates a list of increments and prints it
