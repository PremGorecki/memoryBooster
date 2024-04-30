class LearningItem:
    def __init__(self, id, is_taught, is_verb_irregular, questions, answers,
                 interval, repetition_date, easiness_factor, number_of_correct_repetitions,
                 number_of_incorrect_repetitions):
        self.id = id
        self.is_taught = is_taught
        self.is_verb_irregular = is_verb_irregular
        self.questions = questions
        self.answers = answers
        self.interval = interval
        self.repetition_date = repetition_date
        self.easiness_factor = easiness_factor
        self.number_of_correct_repetitions = number_of_correct_repetitions
        self.number_of_incorrect_repetitions = number_of_incorrect_repetitions

    def to_dict(self):
        return {
            "id": self.id,
            "is_taught": self.is_taught,
            "is_verb_irregular": self.is_verb_irregular,
            "questions": self.questions,
            "answers": self.answers,
            "interval": self.interval,
            "repetition_date": self.repetition_date,
            "easiness_factor": self.easiness_factor,
            "number_of_correct_repetitions": self.number_of_correct_repetitions,
            "number_of_incorrect_repetitions": self.number_of_incorrect_repetitions
        }