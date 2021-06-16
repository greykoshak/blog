# blog
Flask, sqlalchemy

gunicorn - для сервера Heroku
1. pip install flask sqlalchemy qunicorn 

2. pip freeze > requirements.txt
3. В корневой папке /blog создать файл Procfile и записать управляющую строку для 
Heroku:
    echo "web:qunicorn app:app" > Procfile
