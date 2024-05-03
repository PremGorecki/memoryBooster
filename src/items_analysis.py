import pandas as pd


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
