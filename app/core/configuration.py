import os


database_credentials = {
        "user" : os.getenv("POSTGRES_USER"),
        "password" : os.getenv("POSTGRES_PASSWORD"),
        "host" : os.getenv("POSTGRES_HOST"),
        "port" : os.getenv("POSTGRES_PORT")
    }

def get_database_url() -> str:
    if all(database_credentials.values()):
        return f'postgresql://{database_credentials["user"]}:{database_credentials["password"]}@{database_credentials["host"]}:{database_credentials["port"]}/graph'
