#/usr/bin/bash
echo --------------------Running Server--------------------
. venv/bin/activate
export $(cat .env | xargs)
flask run 
echo --------------------Server Stopped--------------------