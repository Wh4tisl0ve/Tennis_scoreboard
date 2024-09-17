from app.database_engine import db_engine_mysql
from app.models import Base


def main():
    with db_engine_mysql.engine.begin() as conn:
        Base.metadata.create_all(conn)


if __name__ == '__main__':
    main()

