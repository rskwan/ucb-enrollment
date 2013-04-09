import sqlite3

def insert_sect(title, ccn, dt, data):
    date = str(dt.date())
    conn = sqlite3.connect('enrollment.db')
    c = conn.cursor()
    check = c.execute('select ccn from courses where ccn=?', [ccn]).fetchall()
    if len(check) == 0:
        c.execute('insert into courses values (?, ?)', [ccn, title])
    check2 = c.execute('select * from enrinfo where ccn=? and date=?',
                       [ccn, date]).fetchall()
    if len(check2) == 0:
        c.execute('insert into enrinfo values (?, ?, ?, ?, ?)',
                  [ccn, date, data['seatlimit'], data['enrolled'],
                   data['waitlist']])
    conn.commit()
    conn.close()

def get_course_map():
    courses = {}
    conn = sqlite3.connect('enrollment.db')
    c = conn.cursor()
    result = c.execute('select * from courses').fetchall()
    for row in result:
        courses[row[0]] = str(row[1])
    conn.close()
    return courses

def get_enroll_info(ccn):
    info = {}
    conn = sqlite3.connect('enrollment.db')
    c = conn.cursor()
    result = c.execute('select * from enrinfo where ccn=?', [ccn]).fetchall()
    if len(result) == 0:
        return None
    for row in result:
        date = row[1]
        info[date] = { 'seatlimit': row[2],
                       'enrolled': row[3],
                       'waitlist': row[4] }
    conn.close()
    return info
