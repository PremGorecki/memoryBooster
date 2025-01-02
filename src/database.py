from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from model import LearningItem

def DbConnect():
    engine = create_engine(
        'sqlite:///E:\\Mój dysk\\_PROGRAMMING\\02_PYTHON\\01_MEMORY_BOOSTER\\memoryBooster\\db\\memory_booster.db')

    try:
        with engine.connect() as conection:
            Session = sessionmaker(bind=engine)

            with Session() as session:
                items2 = session.query(LearningItem).all()
                # for item in items2:
                #     print(item.questions)
                return items2
    except SQLAlchemyError as e:
        print(e)

