# Task Tracker

This project is the free verison of Jira-like task tracker.

## Start a docker network
```sh
docker network create -d bridge backend_db_network
```

## Start the database
```sh
docker-compose -f docker-compose.database.yml up -d
```

## Start the backend
```sh
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.prod.yml up -d --build
```
