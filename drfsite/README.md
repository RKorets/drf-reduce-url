# DFR-reduce-url

##ENV 
Firs need create .env file as project core (if run outside docker drfsite/drfsite/.env settings.py)
```sh 
drfsite/.env
```
Default in .env use sqlite3 db, if you need change db, edit Docker file too.
## Docker

DFR-reduce-url is very easy to install and deploy in a Docker container.

Run docker compose file

```sh
cd drfsite/
docker-compose up --build
```

## API PATH

| URL | Description | Permissions |
| ------ | ------ | ------ |
| <b>api/token/ | POST method for takes token {username password} | only register users
| <b>api/token/refresh/ | POST method for refresh current token | owner token
| <b>api/token/verify/ | POST method for refresh current token | owner token
| <b>api/v1/registrations/ | POST method for create new user | only admin
| <b>api/v1/create/ | POST method for generate new short url {origin} | only auth user
| <b>api/v1/urllist/ | GET method for show all generate url | only owner url or admin
| <b>api/v1/r/int:pk | GET method show info about url, PUT-DELETE-PATCH | any read, owner edit
| <b>short/str:short | GET method redirect for original url | any



