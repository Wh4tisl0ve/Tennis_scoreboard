from dataclasses import dataclass
from dotenv import dotenv_values


@dataclass(frozen=True)
class RunConfig:
    host: str = 'localhost'
    port: int = 8000


@dataclass(frozen=True)
class DatabaseConfig:
    __config = dotenv_values()
    DB_HOST: str = __config['DB_HOST']
    DB_PORT: int = __config['DB_PORT']
    DB_USER: str = __config['DB_USER']
    DB_PASS: str = __config['DB_PASS']
    DB_NAME: str = __config['DB_NAME']

    @property
    def DATABASE_URL_pymysql(self) -> str:
        return f'mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


@dataclass(frozen=True)
class Settings:
    db: DatabaseConfig = DatabaseConfig()
    run: RunConfig = RunConfig()


settings = Settings()
