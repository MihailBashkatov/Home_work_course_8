

## Start project ##
1) Copy docker-compose.yml to your directory
2) Set there file .env 

            touch .env

3) Insert next variables

            nano .env

Generate SECRET_KEY

     tr -dc 'A-Za-z0-9!#$%&\()*+,-./:;<=>?@[\]^_{|}~' </dev/urandom | head -c 50  ; echo

SECRET_KEY=     
DEBUG=True  

POSTGRES_DB=test_docker_35_2  
POSTGRES_USER=postgres  
POSTGRES_PASSWORD=postgres  
POSTGRES_HOST=db  
POSTGRES_PORT=5432  



4) Insert command in the terminal

       docker compose up --build

5) App is available
127.0.0.1:80

5) To stop the programme

            CTRL C
