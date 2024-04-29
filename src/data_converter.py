import json
import pandas as pd

def RemoveNewLineCharacter(input):
    return input.replace("\n", "")

with (open("E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\data_esp.txt", 'r', encoding='utf-8')
      as file):
    lines = file.readlines()

class LearningItem:
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

    unit = LearningItem(id, isTaught, isVerbIrregular, question, question1, question2,
                        answer, answer1, answer2, answer3, answer4, answer5, answer6,
                        interval, repetitionDate, easinessFactor, numberOfCorrectRepetitions, numberOfIncorrectRepetitions)
    units.append(unit)

#Konwersja obiektu do słownika
units_dict = []

for unit in units:

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

#Ustawienie indent=4 spowoduje wcięcie o cztery spacje dla każdego zagnieżdżenia,
#co sprawi, że plik JSON będzie sformatowany i czytelny.

# Zapis do pliku JSON za pomocą json.dump()
with (open("E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\data_esp.json", "w", encoding='utf-8')
      as json_file):
    json.dump(units_dict, json_file, ensure_ascii=False,  indent=4)

def TheMostDifficultOrEasiestItems(howMany, isDifficutl ):
    if (isDifficutl):
        # Fifteen the most difficult items to lear
        df = pd.DataFrame(units_dict)
        df_sorted = df.sort_values('numberOfIncorrectRepetitions', ascending=False)
        df_largest = df_sorted.nlargest(howMany, 'numberOfIncorrectRepetitions')
        resultDF = df_largest.rename(columns={"numberOfIncorrectRepetitions": "IncRep"})
        print("====The most difficult items=================")
        print(resultDF[['question', 'answer', 'IncRep']])
    else:
        #Fifteen the easiest items to lear
        df = pd.DataFrame(units_dict)
        df_sorted = df[df.numberOfIncorrectRepetitions == 0].sort_values('numberOfCorrectRepetitions', ascending=False)
        df_largest = df_sorted.nlargest(howMany, 'numberOfCorrectRepetitions')
        resultDF = df_largest.rename(columns={"numberOfCorrectRepetitions": "CorRep"})
        print("====The easies items=========================")
        # Set up - maximum column width
        resultDF['question2'] = resultDF['question'].str[0:15]
        print(resultDF[['question2', 'answer', 'CorRep']])
