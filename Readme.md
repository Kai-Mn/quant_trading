# Activating venv 

## Windows 
Run `.\venv\Scripts\activate.bat` in project root

## UNIX
Run `source venv/bin/activate` in project root

# Build Dockerimage
`docker build --no-cache -t quant_trading .`

# Start server
Run `docker run -it -p 8000:8000 quant_trading` in quant_trading root