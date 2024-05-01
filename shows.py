#!/usr/bin/env python3

import sys
import sqlite3
import subprocess

if len(sys.argv) < 2:
    print("Usage: shows FILE")
    sys.exit(1)

db_path = sys.argv[1]

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
    try:
        selection = int(input()) - 1
    except (KeyboardInterrupt, EOFError):
        exit()
    print_menu_for_selected_show(list(shows.items())[selection][0])


def issue_sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()


def print_report(db, statement):
    # SELECT statements are run via shell to produce the "-box" output format
    subprocess.run([f"sqlite3 -box {db} '{statement}'"], shell=True)


def print_menu_for_selected_show(table):
    menu = [
    '',
    '1. List episodes',
    '2. Next episode',
    '3. Random episode',
    '4. Mark episode as watched',
    'm. Main menu',
    ]
    if table == 'xfiles':
        menu.append('a. List mythology arc')
    for i in menu:
        print(i)
    sql_all_episodes = f"SELECT * from {table}"
    sql_next_episode = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY NumOverall LIMIT 1"
    sql_random_episode = f"SELECT * FROM {table} WHERE WatchedDate IS NULL ORDER BY random() LIMIT 1"
    sql_mytharc_episodes = f"SELECT * FROM {table} WHERE Mytharc IS NOT NULL"

    try:
        while True:
            choice = input(f'\n{shows[table]}> ')
            if choice == '1':
                print()
                print_report(db_path, sql_all_episodes)
            elif choice == '2':
                print()
                print_report(db_path, sql_next_episode)
            elif choice == '3':
                print()
                print_report(db_path, sql_random_episode)
            elif choice == '4':
                episode = int(input('\nEpisode: '))
                sql_update_episode = f"UPDATE {table} SET WatchedDate = date('now', 'localtime') WHERE NumOverall = {episode}"
                issue_sql_statement(db_path, sql_update_episode)
            elif choice == 'm':
                print()
                main()
            elif choice == 'a':
                print_report(db_path, sql_mytharc_episodes)
    except (KeyboardInterrupt, EOFError):
        pass


main()
