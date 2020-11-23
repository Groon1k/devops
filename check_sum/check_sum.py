from pathlib import Path
import hashlib
import pymysql

def do_file_list_filtr(address, filtr):
    spisok = list()
    current_dir = Path(address)
    for current_file in current_dir.glob(filtr):
        spisok.append(current_file)
    return spisok

def do_digest(file_list):
    check = list()
    for i in range(0, len(file_list)):
        md5 = hashlib.md5()
        file = open(file_list[i], 'rb', buffering = 0)
        data = file.read(65535)
        if not data:
            data = b''
        md5.update(data)
        hsh = md5.hexdigest()
        digest = i, file_list[i], hsh
        check.append(digest)
    return check

def insert_in_db(values):
    conn = pymysql.connect(host = 'localhost', user = 'elgr', password = 'neo', db = 'fim')
    cur = conn.cursor()
    command = f"INSERT INTO checklist (id, path, hash) VALUES ({int(values[0])}, '{str(values[1])}', '{str(values[2])}')"
    cur.execute(command)
    conn.commit()

def save_check_to_db(check_list):
    for a in check_list:
        insert_in_db(a)

def validate_check_list(check_list):
    conn = pymysql.connect(host = 'localhost', user = 'elgr', password = 'neo')
    cur = conn.cursor()
    for check in check_list:
        command = f"SELECT * FROM fim.checklist WHERE path='{check[1]}'"
        cur.execute(command)
        test = cur.fetchone()
        if test[2] == check[2]:
            print(f'hash for {check[1]} is valid')
        else:
            print(f'DANGER! HASH FOR {check[1]} IS NOT VALID!')
            
address = '/home/kali/Documents/'
filtr = '*.py'
file_list = do_file_list_filtr(address, filtr)
check_list = do_digest(file_list)
#save_check_to_db(check_list)
validate_check_list(check_list)

