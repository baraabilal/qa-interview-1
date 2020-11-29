import pandas as pd

def load_data(file_name='questions.csv'):
    with open(file_name, 'r') as f:
        rows = [row.split(',') for row in f.read().split('\n')]
        rows = rows[1:len(rows)]
        print("answers are")
        print(rows)
    return rows

def write_response(response, file_name='responses.csv'):
    with open(file_name, 'a') as f:
        f.write('{}, {}\n'.format(response['id'], response['response']))

def load_responses(file_name='responses.csv'):
    with open(file_name, 'r') as f:
        rows = [row.split(',') for row in f.read().split('\n')]
        print("my answers are")
        print(rows)

    return {row[1]: row[0] for row in rows}