# pydate
Python program to scrape email server for events, due dates, and time sensitive events

## Overview
This program is designed to scrape emails from your GMail server that contain information about events. Namely, this algorithm looks for formatted dates (dd/mm/yyyy) and times (dd:dd). The program Get_Emails.py is responsible for establishing a connection to the server, retriving a list of emails from the server, and parsing the emails. The front facing program is Display_Emails.py, which will allow a user to interact with the database of stored emails to print emails, search for a specific email, and delete emails from the database.

## Requirements
* [Shelve](https://docs.python.org/2/library/shelve.html)

## Usage
```
python Get_Emails.py
```
Starts the script to scrape a save event-sensitive emails to database. After logging in, does not require further user interaction

```
python Display_Emails.py
```
Starts the interactive script to print, search, and delete from the database
