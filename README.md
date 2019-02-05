# About
This is a reporting tool that analyzes visitor activity on a news website. It queries a PostgreSQL database of over one million records and returns the results in plain text. The tool uses python code to connect to the database to answer these questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Getting Started
This project uses data from newsdata.sql and database software provided by a Linux virtual machine.

# Prerequisites
- Python
- Vagrant
- VirtualBox

# Built With
This project consists of the following files:
- README.md - This readme file
- Vagrantfile - Configuration file for the Vagrant virtual machine
- reports.py - The Python program that connects to the PostgreSQL database, runs the SQL queries and displays the results in plain text
- newsdata.zip - Contains the file that populates the news PostgreSQL database

The newsdata.sql database contains three tables:
- articles - Includes titles of articles
- authors  - Includes names of authors
- log - Date, time and HTTP status code of every request made for articles on the company website

# Setup
1. Install Vagrant And VirtualBox
2. Clone this repository
3. Download and unzip [newsdata.zip][8c048302]

  [8c048302]: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "newsdata"

# To Run
From the command line interface:
1. Launch Vagrant VM: `vagrant up` and Connect: `vagrant ssh`
2. Load data: `psql -d news -f newsdata.sql`
3. To run the program, execute: `python reports.py`

# Acknowledgments
Udacity.com Full Stack Developer Nanodegree program - Logs Analysis Project
