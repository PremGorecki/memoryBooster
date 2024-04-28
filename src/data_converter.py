import json

with open("E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\data_esp_short.txt", 'r') as file:

    lines = file.readlines()
    # for line in lines:
    #     print(line)

    numberOfUnits = int(lines[0])
    #print(numberOfUnits)

class Unit:
        def __init__(self, id, isTaught, isVerbIrregular, question, answer):
            self.id = id
            self.isTaught = isTaught
            self.isVerbIrregular = isVerbIrregular
            self.question = question
            self.answer = answer

units = [
    Unit(1, True, False, 'jeden', 'one'),
    Unit(2, True, False, 'dwa', 'two'),
    Unit(3, True, False, 'trzy', 'three')
]



#Konwersja obiektu do słownika
units_dict = []

for unit in units:
    units_dict.append({
    "id": unit.id,
    "isTaught": unit.isTaught,
    "isVerbIrregular": unit.isVerbIrregular,
    "question": unit.question,
    "answer": unit.answer
    })

#Ustawienie indent=4 spowoduje wcięcie o cztery spacje dla każdego zagnieżdżenia,
#co sprawi, że plik JSON będzie sformatowany i czytelny.

# Zapis do pliku JSON za pomocą json.dump()
with open("E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\data_esp_short.json", "w") as json_file:
    json.dump(units_dict, json_file,  indent=4)

# Lub zapis do stringa JSON za pomocą json.dumps()
json_string = json.dumps(units_dict,  indent=4)
print(json_string)