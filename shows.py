import sqlite3
import subprocess
import platform

if platform.system() == 'Linux':
    path = '/home/maf/docs/db/'
else:
    path = '/Users/maf/docs/db/'

# change the string part of value of this variable to "test.db" for testing
media_db = path + 'media.db'

# 'table name': 'show title'
shows = {
    'tos': 'Star Trek: The Original Series',
    'tas': 'Star Trek: The Animated Series',
    'tng': 'Star Trek: The Next Generation',
    'ds9': 'Star Trek: Deep Space Nine',
    'stv': 'Star Trek: Voyager',
    'ste': 'Star Trek: Enterprise',
    'babylon5': 'Babylon 5',
    'cosmos': 'Cosmos',
    'connections': 'Connections',
    'growingup': 'Growing Up in the Universe',
    'xfiles': 'The X-Files',
    'twilightzone': 'The Twilight Zone',
    'ft': 'Fawlty Towers',
    'mk': 'Master Keaton',
    'monster': 'Monster',
    'lotgh': 'Legend of the Galactic Heroes',
    'rolw': 'Record of Lodoss War'
}

def main():
    index = 1
    print()
    for i in list(shows.items()):
       print(f'{index}. {i[1]}')
       index += 1
    print()
    selection = int(input()) - 1
    show(list(shows.items())[selection][0])

def sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()

def sql_select(db, statement):
    # SELECT statements are run via shell to produce the "-box" output format
    subprocess.run([f"sqlite3 -box {db} '{statement}'"], shell=True)

def show(table):
    db = media_db
    menu = [
    '',
    '1. List episodes',
    '2. Next episode',
    '3. Random episode',
    '4. Mark episode as watched',
    'q. Quit'
    ]
    if table == 'xfiles':
        menu.append('m. List mythology arc')
    for i in menu:
        print(i)
    select_all = f"SELECT * from {table}"
    select_next = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY NumOverall LIMIT 1"
    select_random = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY random() LIMIT 1"
    select_mytharc = f"SELECT * FROM {table} WHERE Mytharc IS NOT NULL"

    while True:
        choice = input(f'\n{shows[table]}> ')
        if choice == '1':
            print()
            sql_select(db, select_all)
        elif choice == '2':
            print()
            sql_select(db, select_next)
        elif choice == '3':
            print()
            sql_select(db, select_random)
        elif choice == '4':
            episode = int(input('\nEpisode: '))
            update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
            sql_statement(db, update_episode)
        elif choice == 'q':
            print()
            break
        elif choice == 'm':
            sql_select(db, select_mytharc)

main()
