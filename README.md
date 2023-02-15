# Simporter Test Task

### Small Flask API that provides data for visualisation
## Installing using Github
Python 3.10 and Docker must be installed

- Clone repo and set up virtual environment:
```shell
git clone TBA
python -m venv venv
source venv/bin/activate (Linux and macOS) or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

- Build docker container for database:
```shell
docker-compose up --build
```
- Populate database:
```shell
python populate_database.py
```