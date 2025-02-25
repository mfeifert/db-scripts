#!/usr/bin/env python3

import sys
import sqlite3
import subprocess

if len(sys.argv) < 3:
    print("Usage: water FILE entry [liters]")
    print("       water FILE report [rows]")
    sys.exit(1)

db_path = sys.argv[1]
table = 'water'


def main():
    try:
        if len(sys.argv) == 4:
            report_rows = sys.argv[3]
        else:
            report_rows = 10
        if sys.argv[2] == 'entry':
            insert_log_entry()
        elif sys.argv[2] == 'report':
            print_daily_report(report_rows)
        else:
            print('Command not recognized. Try "entry" or "report".')
    except (KeyboardInterrupt, EOFError):
        print()
        exit()


def insert_log_entry():
    if len(sys.argv) == 4:
        liters = sys.argv[3]
        sql_log_entry = f"INSERT INTO {table} VALUES (date('now', 'localtime'), {liters})"
        issue_sql_statement(db_path, sql_log_entry)
    sql_log_report = "SELECT Date, Liters \
                      FROM water WHERE Date IS date('now', 'localtime') \
                      UNION ALL SELECT 'Total', SUM(Liters) \
                      FROM water WHERE Date IS date('now', 'localtime');"
    print_report(db_path, sql_log_report)


def print_daily_report(rows):
    sql_daily_report = f"SELECT Date, sum(Liters) AS Liters \
                         FROM {table} \
                         GROUP BY Date ORDER BY Date DESC LIMIT {rows}"
    print_report(db_path, sql_daily_report)


def issue_sql_statement(db, statement):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(statement)
    con.commit()
    con.close()


def print_report(db, statement):
    # SELECT statements are run via shell to produce the "-box" output format
    subprocess.run([f'sqlite3 -box {db} "{statement}"'], shell=True)


main()
