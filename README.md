# TASK'S LIST API
## Flask, Flask-SQLAlchemy, SQLAlchemy, psycopg2 in Docker

A dockerized app built on top of Flask, Postgres and SQLAlchemy in Python3

## Requirements

- Docker
- Docker Compose

## Commands
### init
- docker-compose up
### erase
- docker-compose down
### erase all
- docker-compose down --volumes

## URLs API 

- get all task [GET] http://{{server}}:4000/api/tasks
- get task for filter name [GET] http://{{server}}:4000/api/tasks/<name>
- add task [POST] http://{{server}}:4000/api/tasks
  body: JSON
  {
      "name": "Proyect1",
      "description": "Cambiar diseño de la pantalla censo"
  }
- update task [PUT] http://{{server}}:4000/api/tasks/<id>
  body: JSON
  {
    "name": "Lavar",
    "description": "Lavar la ropa"
  }
- delete task [DELETE] http://{{server}}:4000/api/tasks/<id>
- complet task [PUT] http://{{server}}:4000/api/tasks/completed/<id>
## Credits

- Carlos Ivan Soto Perez

> Copyright (c) GAMEUE
