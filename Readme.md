# General info

This is a project in work. 
The purpose of this application is to make back testing for our trading strategies easy. Not to much attention has been given yet on performance or look and feel.
The biggest pet peeve currently is that it contains blocking code that will be put into tasks with celery later on once we get to testing.

## Docker compose

We use a `docker compose` set up for our development because some libraries don’t run under windows and it simplifies deployment. 

## Database

We are using `Mariadb` because we are familiar with it. `SQlite` would have done an equally well job here. 

## Deployment
TODO

This project isn't meant to be really deployed but will be as a showcase and because i wanted to try github actions. 
