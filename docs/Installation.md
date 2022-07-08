# Установка
* python3.X -m venv venv
* pip install -r requirements.txt
* Создайте файл `.env` в корне проекта со следующими полями:

```markdown
SECRET_KEY=verystrongsomethingkey321xxx
DEBUG=1
DB_NAME=public
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
JWT_ACCESS_TOKEN_LIFETIME=12
JWT_REFRESH_TOKEN_LIFETIME=1
```