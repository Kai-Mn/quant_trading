# Setup Project on Windows
## Requirements
* [WSL 2.0](https://learn.microsoft.com/en-us/windows/wsl/install)
* [Docker](https://docs.docker.com/desktop/install/windows-install/)

## Setup
1) Clone Project
2) Build image `docker build --no-cache -t quant_trading .`
3) Start docker-compose container `docker-compose up`

## usefull commands
Run Stylchecker: `docker-compose exec web flake8 quant_trading/ --max-line-length=127` TODO: Make this commit hook
Run migrations manually: `docker-compose exec web python3 quant_trading/manage.py migrate`
Start python shell `docker compose exec app python3 quant_trading/manage.py shell`
Run migrations linux `docker compose exec app python3 quant_trading/manage.py migrate`
Run specific script `docker-compose exec web <script.py>`
Run script from python shell `exec(open('./quant_trading/frontend/tasks.py').read())`
Undo all frontend migrations `sudo docker compose exec app python3 quant_trading/manage.py migrate frontend zero`
`docker-compose exec app sh`