import sqlite3
from  tqdm import  tqdm

TABLE_QUESTION = 'Questions'
TABLES = [
    {'name': 'quiz_subject', 'column': 'subject_id'},
    {'name': 'quiz_subjectone', 'column': 'sub_subject_one_id'},
    {'name': 'quiz_subjecttwo', 'column': 'sub_subject_two_id'},
    {'name': 'quiz_subjecthree', 'column': 'sub_subject_three_id'},
    {'name': 'quiz_examcategory', 'column': 'exam_category_id'},
    {'name': 'quiz_examcategoryone', 'column': 'exam_category_one_id'},
    {'name': 'quiz_examcategorytwo', 'column': 'exam_category_two_id'},
    {'name': 'quiz_examcategorythree', 'column': 'exam_category_three_id'},
]


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def main():
    con = sqlite3.connect('quiz_app_9.db')
    cur = con.cursor()
    cur.row_factory = dict_factory

    print('start of main program')
    for tables in tqdm(TABLES):
        table_name = tables['name']
        column_name = tables['column']

        """SET COUNT 0"""
        # query = "UPDATE {} SET count=0, count_2=1".format(table_name);

        query = f"SELECT id from {table_name}"

        cur.execute(query);
        table_ids = cur.fetchall()
        print(f'\nUPDATING {table_name}: ', table_ids)

        for value in tqdm(table_ids):
            # GET THE COUNT 1
            query = f"SELECT count('question') as count FROM {TABLE_QUESTION} WHERE {column_name}={value['id']} AND table_id=1"
            # print('query ', query)
            cur.execute(query)
            count_for_id = cur.fetchall()
            # print(f"count for id {value['id']}: {count_for_id[0]['count']}")

            # GET THE COUNT 2
            query = f"SELECT count('question') as count FROM {TABLE_QUESTION} WHERE {column_name}={value['id']} AND table_id=2"
            # print('query ', query)
            cur.execute(query)
            count2_for_id = cur.fetchall()
            # print(f"count2 for id {value['id']}: {count2_for_id[0]['count']}")

            # SET THE COUNT 1 AND 2
            query = f"UPDATE {table_name} SET count={count_for_id[0]['count']}, count_2={count2_for_id[0]['count']}"
            # print('set query, ', query)
            cur.execute(query)

        con.commit()


if __name__ == '__main__':
    main()
    print('program finished')
