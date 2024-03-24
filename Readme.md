# General info

The purpose of this application is to make back testing for our trading strategies easy. Not to much attention has been given yet on performance or look and feel.
Because it's a theoretical thesis we prioritize the paper and a lot of work is currently done by manually running scripts. The goal is develop this frontend in some spare time and have it working well by the end of it. 
The biggest pet peeve currently is that it contains blocking code that will be put into tasks with celery later on once we get to testing.

## Docker compose
We use a `docker compose` set up for our development because some libraries don’t run under windows and it simplifies deployment. 

## Database

We are using `Mariadb` because we are familiar with it. `SQlite` would have done an equally well job here. 

## Deployment

This project isn't meant to be really deployed but will be as a showcase. 
It currently gets deployed manually over a github action that builds a docker image and pushes it to the ghcr then ssh in to the server where it pulls the image and runs it. 

## TODOs

* Make a deployment conf with Debugger disabled. 
* Only enable https on deployment
* Get a decent Bootstrap template
