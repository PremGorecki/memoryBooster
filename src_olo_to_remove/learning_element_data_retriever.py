import json
import pandas as pd
from learning_element import LearningElement

folder_path = "/Users/BRFT46/Desktop/REPOS/memoryBooster/data/"
source_file = "data_esp.txt"
result_file = "data_esp.json"

def learning_elements_from_file(file_path):
    learning_elements = []
    with open(file_path, "r", encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        i = 2
        while i < num_lines:
            if lines[i].strip() == '-' * len(lines[i].strip()):
                i += 1
                continue
            id = int(lines[i].strip())
            isTaught = lines[i + 1].strip() == "true"
            isVerbIrregular = lines[i + 2].strip() == "true"
            questions = []
            for j in range(3, 6):
                if lines[i + j].strip():
                    questions.append(lines[i + j].strip())
            answers = []
            for j in range(6, 13):
                if lines[i + j].strip():
                    answers.append(lines[i + j].strip())
            interval = int(lines[i + 13].strip())
            repetitionDate = lines[i + 14].strip()
            easinessFactor = float(lines[i + 15].strip())
            numberOfCorrectRepetitions = int(lines[i + 16].strip())
            numberOfIncorrectRepetitions = int(lines[i + 17].strip())
            learning_element = LearningElement(id, isTaught, isVerbIrregular, questions, answers,
                                               interval, repetitionDate, easinessFactor,
                                               numberOfCorrectRepetitions, numberOfIncorrectRepetitions)
            learning_elements.append(learning_element)
            i += 18
    return learning_elements


def json_from_learning_elements_to_file(learning_elements, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([element.to_dict() for element in learning_elements], f, indent=4, ensure_ascii=False)


def show_items(amount):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    data = [element.to_dict() for element in learning_elements]
    result = pd.DataFrame(data)
    result = (result.nlargest(amount, 'numberOfIncorrectRepetitions')
              .rename(columns={"numberOfIncorrectRepetitions": "IncRep"}))
    print("====The most difficult items=================")
    print(result[['questions', 'answers', 'IncRep']])


learning_elements = learning_elements_from_file(folder_path + source_file)
json_from_learning_elements_to_file(learning_elements, folder_path + result_file)
show_items(15)
