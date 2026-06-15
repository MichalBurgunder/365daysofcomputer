# FIRST DRAFT: MISTRAL GENERATED
# FINALIZATION: ME
def check_if_num(string):
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in string:
        if num not in nums:
            print(num)
            print(f'string not a number: {string}')
            exit()

def check_of_parts_empty(parts):
    if not len(parts[0]):
        print(f"empty string name. number: {parts[1]}")
        exit()
    if not len(parts[1]):
        print(f"empty string number: {parts[0]}")
        exit()

def read_data(file_path):
    result = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            
            if len(parts) == 2:
                text = parts[0].strip()
                number = parts[1].strip()

                check_of_parts_empty([text, parts[1]])
                check_if_num(number)

                result.append([text, int(number)])
    return result

def write_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            line = f"{item[0]}, {item[1]}\n"
            file.write(line)

root = "/Users/michal/Documents/365daysofcomputer/365daysofcomputer-code"
dictionary_path = f'{root}/dictionary.txt'
output_path = f'{root}/sorted_dictionary.txt'

data = read_data(dictionary_path)
data.sort(key=lambda x: x[0])

write_data(output_path, data)