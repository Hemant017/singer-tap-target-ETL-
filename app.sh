FILE=data_db.db

if [ -f "$FILE" ]; then
    echo "$FILE exists."
    python tap2.py | target-sqlite -c config.json
else 
    echo "$FILE does not exist."
    python tap1.py | target-sqlite -c config.json
    python tap2.py | target-sqlite -c config.json
fi

crontab -e
#1 0 * * * /home/pratham/PersonalSpace/asss/src/app.sh > /home/pratham/logs/backup.log 2>&1