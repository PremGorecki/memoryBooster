from sqlalchemy import Column, Integer, Text, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LearningItem(Base):
    __tablename__ = 'learning_item'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    subject = Column(Text, nullable=False)
    is_taught = Column(Integer, nullable=False)
    is_verb_irregular = Column(Integer, nullable=False)
    questions = Column(Text, nullable=False)
    answers = Column(Text, nullable=False)
    interval = Column(Integer, nullable=False)
    repetition_date = Column(Text)
    easiness_factor = Column(Float, nullable=False)
    number_of_correct_repetitions = Column(Integer, nullable=False)
    number_of_incorrect_repetitions = Column(Integer, nullable=False)
