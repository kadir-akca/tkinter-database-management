import sqlite3
import subprocess

db_url = 'my_database.db'


def open_db():
    try:
        subprocess.call(['open', db_url])
    except subprocess.SubprocessError as e:
        print('Failed to open database', e)


def return_experience_id():
    a = x
    return a


def insert_accuracy_test(dev, op, dep, etype, artsn, certsn, sub, eid):
    try:
        if dev != '':
            conn = sqlite3.connect(db_url)
            cursor = conn.cursor()
            print('Succesfully connected to the database')
            insert_query_with_param = """INSERT INTO accuracy_test("device_sn", "operator","department","experience_type","artefact_sn","certificate_sn", subject, experience_id) VALUES (?, ?, ?, ? ,?, ?, ?, ?)"""
            data = (dev, op, dep, etype, artsn, certsn, sub, eid)
            cursor.execute(insert_query_with_param, data)
            conn.commit()
            global x
            x = eid
            return cursor
        else:
            pass
    except sqlite3.Error as e:
        print('Failed to insert accuracy test in database', e)


def insert_operator(us, d):
    try:
        conn = sqlite3.connect(db_url)
        c = conn.cursor()
        print('Succesfully connected to the database')
        insert_query_with_param = """INSERT INTO operator(name, "add_date") VALUES (?, ?)"""
        data = (us, d)
        if us != '':
            c.execute(insert_query_with_param, data)
            conn.commit()
        else:
            print('No value to add')
    except sqlite3.Error as e:
        print('Failed to insert user in database', e)


def check_operator_number():
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    cursor.execute("select * from operator")
    results = cursor.fetchall()
    return len(results)


def get_operators():
    conn = sqlite3.connect(db_url)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    data = c.execute('SELECT name FROM operator').fetchall()
    return data


def get_departments():
    conn = sqlite3.connect(db_url)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    data = c.execute('SELECT name FROM department').fetchall()
    return data


def get_experience_type():
    conn = sqlite3.connect(db_url)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    data = c.execute('SELECT name FROM experience_type').fetchall()
    return data


def get_artefact_sn(x):
    conn = sqlite3.connect(db_url)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    data = c.execute('SELECT sn FROM artefact_sn WHERE experience_type = ?', (x,)).fetchall()
    return data


def get_experience_id(x):
    conn = sqlite3.connect(db_url)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    data = c.execute('SELECT experience_id FROM accuracy_test WHERE device_sn = ?', (x,)).fetchall()
    if len(data) == 0:
        return 'xxxx'
    else:
        return data[-1]
