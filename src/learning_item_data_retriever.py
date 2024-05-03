import json
import os

import os
from learning_item import LearningItem
import items_analysis

FOLDER_PATH = os.getenv('FOLDER_PATH')
SOURCE_FILE = os.getenv('SOURCE_FILE')
RESULT_FILE = os.getenv('RESULT_FILE')

print(FOLDER_PATH)
print(SOURCE_FILE)
print(RESULT_FILE)


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


learning_items = learning_items_from_file(FOLDER_PATH + "\\" + SOURCE_FILE)
json_from_learning_items_to_file(learning_items, FOLDER_PATH + "\\" + RESULT_FILE)
items_analysis.show_items(learning_items, 15, False)
