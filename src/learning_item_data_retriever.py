import json
import pandas as pd
from learning_item import LearningItem

FOLDER_PATH = "E:\\Mi unidad\\_PYTHON\\PycharmProjects\\memoryBooster\\data\\"
SOURCE_FILE = "data_esp.txt"
RESULT_FILE = "data_esp.json"


def parse_boolean(line):
    return line.strip() == "true"


def parse_int(line):
    return int(line.strip())


def parsing_items_from_lines(lines, num_lines):
    learning_items = []
    i = 2
    while (i < num_lines):
        if lines[i].strip() == '-' * len(lines[i].strip()):
            i += 1
            continue
        id = parse_int(lines[i])
        isTaught = parse_boolean(lines[i + 1])
        isVerbIrregular = parse_boolean(lines[i + 2])
        questions = []
        for j in range(3, 6):
            if lines[i + j].strip():
                questions.append(lines[i + j].strip())
        answers = []
        for j in range(6, 13):
            if lines[i + j].strip():
                answers.append(lines[i + j].strip())
        interval = parse_int(lines[i + 13])
        repetitionDate = lines[i + 14].strip()
        easinessFactor = round(float(lines[i + 15].strip()), 4)
        numberOfCorrectRepetitions = parse_int(lines[i + 16])
        numberOfIncorrectRepetitions = parse_int(lines[i + 17])
        learning_item = LearningItem(id, isTaught, isVerbIrregular, questions, answers,
                                     interval, repetitionDate, easinessFactor,
                                     numberOfCorrectRepetitions, numberOfIncorrectRepetitions)
        learning_items.append(learning_item)
        i += 18
    return learning_items


def learning_items_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    number_of_units = int(lines[0])
    num_lines = len(lines)

    return parsing_items_from_lines(lines, num_lines)


def json_from_learning_items_to_file(learning_elements, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump([item.__dict__ for item in learning_items], file, indent=4, ensure_ascii=False)


def hardest_questions(df, amount):
    result = (df.nlargest(amount, 'number_of_incorrect_repetitions')
              .rename(columns={"number_of_incorrect_repetitions": "IncRep"}))
    print("====The most difficult items=================")
    print(result[['questions', 'answers', 'IncRep']])


def easiest_questions(df, amount):
    result = (((df[df.number_of_incorrect_repetitions == 0]
                .sort_values('number_of_incorrect_repetitions', ascending=False))
               .nlargest(amount, 'number_of_correct_repetitions'))
              .rename(columns={"number_of_correct_repetitions": "CorRep"}))
    print("====The easies items=========================")
    print(result[['questions', 'answers', 'CorRep']])


def show_items(learning_items, amount, is_hardest):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    data = [item.__dict__ for item in learning_items]
    df = pd.DataFrame(data)
    if is_hardest:
        hardest_questions(df, amount)
    else:
        easiest_questions(df, amount)


learning_items = learning_items_from_file(FOLDER_PATH + SOURCE_FILE)
json_from_learning_items_to_file(learning_items, FOLDER_PATH + RESULT_FILE)
show_items(learning_items, 15, False)
