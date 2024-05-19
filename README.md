# DB scripts

An assortment of terminal-based scripts that I use daily to interface with SQLite databases.

**Requires:** `python3`, `sqlite3`

Press `Ctrl+D` or `Ctrl+C` to exit any of the scripts.

## Water

`water.py` is used to log water consumption.

**Usage:**

Run `water.py` followed by the filepath of the database file and one of the two built-in commands:

```
water.py FILE entry [liters]
water.py FILE report [rows]
```

To insert a log entry into the database, use `water.py FILE entry [liters]`.  A new row will be inserted into the database with the current date and the specified number of liters.  A table will then be displayed showing all of the current day's log entries, and the current day's total.  Omit `liters` from the command to show the table without inserting an entry.

To show the totals for recent days, use `water.py FILE report [rows]`.  Specify the number of rows to display in the report (one day per row), or omit the `rows` to show the default of 10 rows.

For easy daily use, set an alias for each command:

```bash
alias we='/path/to/water.py /path/to/shows.db entry'
alias wr='/path/to/water.py /path/to/shows.db report'
```

Then use it in the following manner:

```
maf@nuc:~$ we .8
┌────────────┬────────┐
│    Date    │ Liters │
├────────────┼────────┤
│ 2024-05-04 │ 0.2    │
│ 2024-05-04 │ 0.2    │
│ 2024-05-04 │ 0.8    │
│ Total      │ 1.2    │
└────────────┴────────┘

maf@nuc:~$ wr
┌────────────┬────────┐
│    Date    │ Liters │
├────────────┼────────┤
│ 2024-05-04 │ 1.2    │
│ 2024-05-03 │ 2.5    │
│ 2024-05-02 │ 2.3    │
│ 2024-05-01 │ 2.1    │
│ 2024-04-30 │ 2.1    │
│ 2024-04-29 │ 2.0    │
│ 2024-04-28 │ 2.0    │
│ 2024-04-27 │ 1.7    │
│ 2024-04-26 │ 1.5    │
│ 2024-04-25 │ 2.6    │
└────────────┴────────┘
```

**Database schema:**

```sql
CREATE TABLE "water" (
	"Date" TEXT,
 	"Liters" DECIMAL(2, 1)
 );
```

## Yoga

`yoga.py` is used to log the date and duration of yoga sessions.

**Usage:**

```
yoga.py FILE [minutes]
```

To insert a log entry into the database, type `yoga.py FILE [minutes]`.  A new row will be inserted into the database with the current date and the specified number of minutes.  A table will then be displayed showing the 5 most recent log entries.  Alternatively, omit `minutes` from the command and enter the minutes at the prompt.

```bash
alias y='/path/to/yoga.py /path/to/yoga.db'
```

```
maf@nuc:~$ y 10
┌────────────┬─────────┐
│    Date    │ Minutes │
├────────────┼─────────┤
│ 2024-05-04 │ 10      │
│ 2024-05-03 │ 60      │
│ 2024-05-02 │ 15      │
│ 2024-05-02 │ 15      │
│ 2024-05-01 │ 20      │
└────────────┴─────────┘
maf@nuc:~$ y
Minutes: 20
┌────────────┬─────────┐
│    Date    │ Minutes │
├────────────┼─────────┤
| 2024-05-04 | 20      |
│ 2024-05-04 │ 10      │
│ 2024-05-03 │ 60      │
│ 2024-05-02 │ 15      │
│ 2024-05-02 │ 15      │
└────────────┴─────────┘
```

**Database schema:**

```sql
CREATE TABLE "yoga" (
	"Date" TEXT,
	"Minutes" INTEGER
);
````

## Shows

`shows.py` is used to log the dates of when I watched episodes of my favorite shows.

**Usage:**

Run `shows.py` followed by the path to the database file.

```
shows.py FILE
```

```bash
alias s='/path/to/shows.py /path/to/shows.db'
```

A menu is presented with the titles of all included shows.  Make a selection by number to move to the next menu, showing actions that can be taken.  Actions include displaying a list of all episodes in the series, showing the next episode (the earliest episode without a "Watched Date"), a random episode selected from those without a watched date, and marking an episode as watched.  To mark an episode as watched, enter the episode number in the **NumOverall** column of the episode list.  The current date is then entered into the **WatchedDate** field for that episode.

```
[maf@nuc]$ s

1. Star Trek: The Original Series
2. Cosmos
3. The X-Files
4. The Twilight Zone
5. Master Keaton
6. Legend of the Galactic Heroes
7. Record of Lodoss War

> 2

1. List episodes
2. Next episode
3. Random episode
4. Mark episode as watched
m. Main menu

Cosmos> 1

┌────────────┬────────────────────────────────┬─────────────────┬─────────────┐
│ NumOverall │             Title              │ OriginalAirDate │ WatchedDate │
├────────────┼────────────────────────────────┼─────────────────┼─────────────┤
│ 1          │ The Shores of the Cosmic Ocean │ 1980-09-28      │ 2023-07-17  │
│ 2          │ One Voice in the Cosmic Fugue  │ 1980-10-05      │ 2024-03-29  │
│ 3          │ Harmony of the Worlds          │ 1980-10-12      │ 2024-03-30  │
│ 4          │ Heaven and Hell                │ 1980-10-19      │ 2024-04-01  │
│ 5          │ Blues for a Red Planet         │ 1980-10-26      │ 2024-04-05  │
│ 6          │ Travellers' Tales              │ 1980-11-02      │ 2024-04-06  │
│ 7          │ The Backbone of Night          │ 1980-11-09      │             │
│ 8          │ Journeys in Space and Time     │ 1980-11-16      │             │
│ 9          │ The Lives of the Stars         │ 1980-11-23      │             │
│ 10         │ The Edge of Forever            │ 1980-11-30      │             │
│ 11         │ The Persistence of Memory      │ 1980-12-07      │             │
│ 12         │ Encyclopaedia Galactica        │ 1980-12-14      │             │
│ 13         │ Who Speaks for Earth?          │ 1980-12-21      │             │
└────────────┴────────────────────────────────┴─────────────────┴─────────────┘
```

The main menu showing the show titles comes from a dictionary located in `shows.py`.  The key of each dictionary item corresponds to the name of the table in the SQLite database, while the value corresponds to the title shown in the menu.  The menu item numbers used to select a show are generated automatically.  To add a new show, append a new item to the dictionary with the form `'table name': 'show title'`, and add a new table to the database with the episode information.

```python
# 'table name': 'show title'
shows = {
    'tos': 'Star Trek: The Original Series',
    'cosmos': 'Cosmos',
    'xfiles': 'The X-Files',
    'twilightzone': 'The Twilight Zone',
    'mk': 'Master Keaton',
    'lotgh': 'Legend of the Galactic Heroes',
    'rolw': 'Record of Lodoss War'
}
```

**Database schema:**

This schema has the disadvantage of requiring a new column for each additional "Watched Date" of an episode.  To populate the database tables with information about the episodes, I take a manual approach: copy from Wikipedia and other sources, paste into a spreadsheet, perform any necessary formatting and cleanup, export as CSV, and finally import the CSV into the SQLite database.

```sql
CREATE TABLE "tng" (
	"NumOverall" INTEGER,
	"Season" INTEGER,
	"NumInSeason" INTEGER,
	"Title" TEXT,
	"OriginalAirDate" TEXT,
	"WatchedDate" TEXT
);
```

Here is a link to a copy of [my shows.db database file](https://drive.google.com/file/d/1cktlN9zi2ttSK04KzEl0_L3DbuzMZfwI/view?usp=sharing), without any Watched Dates added.

## Fuel

`fuel.py` is used to log details of fuel refills.

**Usage:**

To insert a log into the database, use `fuel.py FILE` and follow the prompts.  After the final prompt, a new row with the specified information is inserted into the database and a report showing the 5 most recent rows is displayed.

```bash
alias fuel='/path/to/fuel.py /path/to/fuel.db'
```

```
maf@nuc:~$ fuel
Price: 45.99
Dollars Per Gallon: 4.599
Gallons: 10.000
Average Miles Per Gallon: 31.4
Odometer: 35050
┌────────────┬────────┬───────┬─────────┬────────┬───────┐
│    Date    │ Amount │  PPG  │ Gallons │ AvgMPG │ Miles │
├────────────┼────────┼───────┼─────────┼────────┼───────┤
│ 2024-05-09 │ 45.99  │ 4.599 │ 10.0    │ 31.4   │ 35050 │
│ 2024-05-05 │ 34.64  │ 5.099 │ 6.793   │ 31.4   │ 35027 │
│ 2024-04-25 │ 55.04  │ 4.999 │ 11.01   │ 29.8   │ 34768 │
│ 2024-04-02 │ 29.89  │ 4.599 │ 6.5     │ 28.9   │ 34480 │
│ 2024-03-14 │ 40.96  │ 4.299 │ 9.528   │ 31.7   │ 34295 │
└────────────┴────────┴───────┴─────────┴────────┴───────┘
```

**Database schema:**

```sql
CREATE TABLE "fuel" (
	"Date" TEXT,
	"Amount" REAL,
	"PPG" REAL,
	"Gallons" REAL,
	"AvgMPG" REAL,
	"Miles" INTEGER
);
```
