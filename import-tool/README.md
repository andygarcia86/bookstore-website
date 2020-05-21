# Python application for read .opf files and import to a MySQL Database

Python application for read OPF files and organize your personal library in your computer.

## Requirements

1. Python 3+
2. Docker

## Setup

1. Install the requirements. Run `pip install -r requirements.txt` in terminal or CMD
2. Run MySQL docker compose `docker-compose -f docker-compose-mysql-database.yml up --build` in terminal or CMD
3. Run `python app.py` in terminal or CMD

### Run Tests

1. Open terminal or CMD
2. Run the following command: `pytest .\tests\test_utils.py`

### Connect to MySQL database

You should be able to connect to the MySQL database using any MySQL client with the following configuration

- Connection:
  - host: localhost
  - port: 33060
  - user: root
  - password: root

