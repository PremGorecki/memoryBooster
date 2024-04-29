import json
import pandas as pd

def RemoveNewLineCharacter(input):
    output = input.replace("\n", "")
    return output

with (open("E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\data_esp.txt", 'r', encoding='utf-8')
      as file):
    lines = file.readlines()

class Unit:
        def __init__(self, id, isTaught, isVerbIrregular, question, question1, question2, answer,
                     answer1, answer2, answer3, answer4, answer5, answer6,
                     interval, repetitionDate, easinessFactor, numberOfCorrectRepetitions, numberOfIncorrectRepetitions):
            self.id = id
            self.isTaught = isTaught
            self.isVerbIrregular = isVerbIrregular
            self.question = question
            # print('qq='+question)
            # print('qqq=' + self.question)
            self.question1 = question1
            self.question2 = question2
            self.answer = answer
            self.answer1 = answer1
            self.answer2 = answer2
            self.answer3 = answer3
            self.answer4 = answer4
            self.answer5 = answer5
            self.answer6 = answer6
            self.interval = interval
            self.repetitionDate = repetitionDate
            self.easinessFactor = easinessFactor
            self.numberOfCorrectRepetitions = numberOfCorrectRepetitions
            self.numberOfIncorrectRepetitions = numberOfIncorrectRepetitions

# units = [
#     Unit(1, True, False, 'jeden', 'one'),
#     Unit(2, True, False, 'dwa', 'two'),
#     Unit(3, True, False, 'trzy', 'three')
# ]

units = [ ]

numberOfUnits = int(lines[0])

for i in range(numberOfUnits):
    id = int(lines[(i)*19+2])
    if (RemoveNewLineCharacter(lines[(i)*19+3])=='true'):
        isTaught = True
    else:
        isTaught = False
    if (RemoveNewLineCharacter(lines[(i)*19+4])=='true'):
        isVerbIrregular = True
    else:
        isVerbIrregular = False

    question = RemoveNewLineCharacter(lines[(i)*19+5])
    question1 = RemoveNewLineCharacter(lines[(i)*19+6])
    question2 = RemoveNewLineCharacter(lines[(i)*19+7])
    answer = RemoveNewLineCharacter(lines[(i)*19+8])
    answer1 = RemoveNewLineCharacter(lines[(i)*19+9])
    answer2 = RemoveNewLineCharacter(lines[(i)*19+10])
    answer3 = RemoveNewLineCharacter(lines[(i)*19+11])
    answer4 = RemoveNewLineCharacter(lines[(i)*19+12])
    answer5 = RemoveNewLineCharacter(lines[(i)*19+13])
    answer6 = RemoveNewLineCharacter(lines[(i)*19+14])
    interval = int(lines[(i)*19+15])
    repetitionDate = RemoveNewLineCharacter(lines[(i)*19+16])
    easinessFactor = round(float(lines[(i)*19+17]),4)
    numberOfCorrectRepetitions = int(lines[(i)*19+18])
    numberOfIncorrectRepetitions = int(lines[(i)*19+19])
    # print('i='+str(i))
    # print('id='+id)
    # print('numberOfCorrectRepetitions='+numberOfCorrectRepetitions)
    # print('numberOfIncorrectRepetitions='+numberOfIncorrectRepetitions)

    unit = Unit(id, isTaught, isVerbIrregular, question, question1, question2,
              answer, answer1, answer2, answer3, answer4, answer5, answer6,
              interval, repetitionDate, easinessFactor, numberOfCorrectRepetitions, numberOfIncorrectRepetitions)
    units.append(unit)

#Konwersja obiektu do słownika
units_dict = []

for unit in units:
    # print('qqqq='+unit.question)

    units_dict.append({
    "id": unit.id,
    "isTaught": unit.isTaught,
    "isVerbIrregular": unit.isVerbIrregular,
    "question": unit.question,
    "question1": unit.question1,
    "question2": unit.question2,
    "answer": unit.answer,
    "answer1": unit.answer1,
    "answer2": unit.answer2,
    "answer3": unit.answer3,
    "answer4": unit.answer4,
    "answer5": unit.answer5,
    "answer6": unit.answer6,
    "interval": unit.interval,
    "repetitionDate": unit.repetitionDate,
    "easinessFactor": unit.easinessFactor,
    "numberOfCorrectRepetitions": unit.numberOfCorrectRepetitions,
    "numberOfIncorrectRepetitions": unit.numberOfIncorrectRepetitions
    })

# print(units_dict)

#Ustawienie indent=4 spowoduje wcięcie o cztery spacje dla każdego zagnieżdżenia,
#co sprawi, że plik JSON będzie sformatowany i czytelny.

# Zapis do pliku JSON za pomocą json.dump()
with (open("E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\data_esp.json", "w", encoding='utf-8')
      as json_file):
    json.dump(units_dict, json_file, ensure_ascii=False,  indent=4)

# Lub zapis do stringa JSON za pomocą json.dumps()
# json_string = json.dumps(units_dict, ensure_ascii=False, indent=4)
# print(json_string)

# Fifteen the most difficult items to lear
df = pd.DataFrame(units_dict)
df2 = df.sort_values('numberOfIncorrectRepetitions', ascending=False)
df2 = df2.nlargest(15, 'numberOfIncorrectRepetitions')
df2 = df2.rename(columns={"numberOfIncorrectRepetitions": "IncRep"})
print("====The most difficult items=================")
print(df2[['question', 'answer', 'IncRep']])

# Fifteen the easiest items to lear
# df = pd.DataFrame(units_dict)
# df3 = df[df.numberOfIncorrectRepetitions == 0].sort_values('numberOfCorrectRepetitions', ascending=False)
# df3 = df3.nlargest(15, 'numberOfCorrectRepetitions')
# df3 = df3.rename(columns={"numberOfCorrectRepetitions": "CorRep"})
# print("====The easies items=========================")
# # Ustawienie maksymalnej liczby kolumn do wyświetlenia na brak limitu
# df3['question2'] = df3['question'].str[0:15]
# print(df3[['question2', 'answer', 'CorRep']])