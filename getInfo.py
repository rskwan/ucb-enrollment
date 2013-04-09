import re, requests, sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
from dbaccess import insert_sect
from depts import depts

def search_dept(dept):
    payload = { 'p_term': 'FL',
                'p_deptname': '-- Choose a Department Name --',
                'p_classif': '-- Choose a Course Classification --',
                'p_presuf': '-- Choose a Course Prefix/Suffix --',
                'p_dept': dept }
    r = requests.get('http://osoc.berkeley.edu/OSOC/osoc', params=payload)
    analyze_html(r.text)

    # get the total rows so we can keep searching
    soup = BeautifulSoup(r.text)
    tables = soup.find_all('table')

    # this is the 'see next results' link
    nextlink = str(tables[0].find_all('tr')[1].find_all('td')[1].br.a['href'])

    # use regex to get the total rows out
    match = re.search('p_total_rows=\d+', nextlink)
    totalrows = int(match.group().split('=')[1])

    # each page displays 100 rows (sections); index starts with 1, not 0
    for i in range(1, (totalrows/100)):
        payload['p_start_row'] = str(100*i + 1)
        r = requests.get('http://osoc.berkeley.edu/OSOC/osoc', params=payload)
        analyze_html(r.text)

def analyze_html(txt):
    soup = BeautifulSoup(txt)

    # each section is displayed as a table
    tables = soup.find_all('table')
    sections = tables[1:(len(tables)-1)]

    for section in sections:
        rows = section.find_all('tr')

        title = rows[0].find_all('td')[2].b.string.strip()
        ccn = rows[5].find_all('td')[1].tt.contents[0]
        try:
            ccn = int(ccn)
        except ValueError:
            # sections with non-integer CCNs usually don't have enrollment info
            continue

        enrollinfo = rows[10].find_all('td')
        enrollnums = enrollinfo[1].tt.string.split()[:3]
        date = enrollinfo[0].b.string.split()[2][:-1]
        dt = get_datetime(date)
        
        data = {}
        data['seatlimit'] = int(enrollnums[0][6:])
        data['enrolled'] = int(enrollnums[1][9:])
        data['waitlist'] = int(enrollnums[2][9:])

        show_section(title, ccn, dt, data)
        insert_sect(title, ccn, dt, data)

def get_datetime(date):
    return datetime.strptime(date, '%m/%d/%y')

def show_section(title, ccn, dt, data):
    date = dt.date()
    out = str(title).strip() + " (CCN " + str(ccn).strip() + "): Limit "
    out += str(data['seatlimit']) + ", Enrolled " + str(data['enrolled'])
    out += ", Waitlist " + str(data['waitlist']) + " (" + str(date) + ")"
    print out

for dept in depts:
    search_dept(dept)
