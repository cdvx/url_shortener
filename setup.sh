#/usr/bin/bash

echo --------------------Setting up venv--------------------
test -d "venv" && echo "venv exists" || python -m venv venv
sleep 2 


echo --------------------Installing requirements--------------------
. venv/bin/activate
pip install -r requirements.txt

echo --------------------Exporting env vars--------------------
export $(cat .env | xargs)
sleep 2
echo --------------------Running migrations--------------------
test -d "migrations" && echo "Migrations folder Exist" || flask db init
flask db migrate
flask db upgrade

echo --------------------Setup done--------------------
