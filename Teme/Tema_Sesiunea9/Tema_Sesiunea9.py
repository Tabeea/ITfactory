# 1. Sa se scrie o functie care citeste date dintr-un fisier csv si le scrie intr-un fisier json.
# Functia primeste numele fisierelor ca parametri.
import csv
import json


def read_csv_to_write_json(readcsv, writejson):
    data = {}
    with open(readcsv, encoding='utf-8') as f:
        csvReader = csv.DictReader(f)
        for rows in csvReader:
            key = rows['Nbcrt']
            data[key] = rows
    with open(writejson, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4))


readcsv = r'Data.csv'
writejson = r'Data.json'
read_csv_to_write_json(readcsv, writejson)

# 2. Sa se scrie o functie care citeste date dintr-un fisier json si le imparte in alte doua fisiere
# astfel incat prima jumatate a datelor va fi in fisierul prima_jumatate.json, iar a doua in a_doua_jumatate.json.
import json

def json_split_to_half(file_name):
    with open(file_name, 'r') as f:
        lines = json.load(f)
        first_half = lines[:(len(lines)//2)]
        second_half = lines[(len(lines)//2):]

    with open('first_half.json', 'w') as f:
            json.dump(first_half, f, indent=4)
    with open('second_half.json', 'w') as f:

        json.dump(second_half, f, indent=4)

json_split_to_half('Data1.json')


# 3. Sa se scrie o functie care citeste date dintr-un fisier csv si le elimina
# pe cele care in oricare coloana contin litera ‘a’. Dupa aceea va actualiza fisierul cu datele ce raman.


def remove_element(file_name, char_a):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    with open('sesiunea9ex3_solved.csv', 'w', newline ='') as f:
        new_data = []
        for line in data:
            current_list = []
            for element in line:
                if char_a not in element:
                    current_list.append(element)
            new_data.append(current_list)
        writer = csv.writer(f)
        writer.writerows(new_data)

remove_element("sesiunea9ex3.csv", "a")
