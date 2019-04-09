TODO
---starter 
python src/run.py

---environment stabil. 
set FLASK_ENV=development 

---docker compose edit
docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location
docker-compose up server

-graqhql add
-jwt token 
-test stabil. 
-sql orm add. 

++debugger ok
++logger ok

install and upgrade 
pip install --upgrade -r requirements.txt


issues suggestions

"ImportError: No Module named six; six already installed"
pip3  install --ignore-installed six

