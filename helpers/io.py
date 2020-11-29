
def load_data(file_name='questions.csv'):
    with open(file_name, 'r') as f:
        rows = [row.split(',') for row in f.read().split('\n')]
    return rows

def write_response(response, file_name='responses.csv'):
    with open(file_name, 'a') as f:
        f.write('{}, {}\n'.format(response['id'], response['response']))

def load_responses(file_name='responses.csv'):
    with open(file_name, 'r') as f:
        rows = [row.split(',') for row in f.read().split('\n')]
    print(rows)
    return {row[0]: row[1] for row in rows}