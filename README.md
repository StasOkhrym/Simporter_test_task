# Simporter Test Task

### Small Flask API that provides data for visualisation
Let’s suppose we have a number of events that are distributed in time. Each event has several
attributes. And we have a service (webpage) which purpose is to visualize this distribution (i.e.
show a timeline) using different filters. API returns JSON with data required to provide visualization.

## Installing using Github
Python 3.10 and Docker must be installed

- Clone repo and set up virtual environment:
```shell
git clone https://github.com/StasOkhrym/Simporter_test_task.git
python -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```
- Configure your `.env` file using `.env-sample` to set Production/Development environment

- Build docker container for database:
```shell
docker-compose up --build
```
- Populate database:
```shell
python populate_database.py
```
- Run app:
```shell
python -m flask run
```
  