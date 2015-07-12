# CFBFilmRoom
CFBFilmRoom

#Prereqs
1. create and activate a virtual environment
pip install virtualenv
virtualenv cfbEnvironment
source cfbEnvironment/bin/activate

2. Install dependencies
pip install -r requirements.txt

#Set up database
1. Create Database Schema
python app/models.py
2. Import Data
python app/import_data.py

#Run API on localhost
1. Run Server
python app/app.py
2. Try out API
visit "http://localhost:1337/api/find/athlete" in the browser
