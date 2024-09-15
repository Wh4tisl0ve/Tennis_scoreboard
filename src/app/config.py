from dataclasses import dataclass
from dotenv import dotenv_values


config = dotenv_values()


@dataclass(frozen=True)
class RunConfig:
    host: str = 'localhost'
    port: int = 8000


@dataclass(frozen=True)
class Settings:
    DB_HOST: str = config['DB_HOST']
    DB_PORT: int = config['DB_PORT']
    DB_USER: str = config['DB_USER']
    DB_PASS: str = config['DB_PASS']
    DB_NAME: str = config['DB_NAME']

    @property
    def DATABASE_URL_pymysql(self):
        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()
