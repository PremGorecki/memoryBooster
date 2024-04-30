class LearningElement:
    def __init__(self, id, isTaught, isVerbIrregular, questions, answers, interval, repetitionDate, easinessFactor,
                 numberOfCorrectRepetitions, numberOfIncorrectRepetitions):
        self.id=id
        self.isTaught = isTaught
        self.isVerbIrregular = isVerbIrregular
        self.questions = questions
        self.answers = answers
        self.interval = interval
        self.repetitionDate = repetitionDate
        self.easinessFactor = easinessFactor
        self.numberOfCorrectRepetitions = numberOfCorrectRepetitions
        self.numberOfIncorrectRepetitions = numberOfIncorrectRepetitions

    def to_dict(self):
        return {
            "id": self.id,
            "isTaught": self.isTaught,
            "isVerbIrregular": self.isVerbIrregular,
            "questions": self.questions,
            "answers": self.answers,
            "interval": self.interval,
            "repetitionDate": self.repetitionDate,
            "easinessFactor": self.easinessFactor,
            "numberOfCorrectRepetitions": self.numberOfCorrectRepetitions,
            "numberOfIncorrectRepetitions": self.numberOfIncorrectRepetitions
        }

