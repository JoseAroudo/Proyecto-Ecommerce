import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sqlite_file_name = 'database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
sqlite_file_path = os.path.join(base_dir,"..",sqlite_file_name)

database_url = f"sqlite:///{sqlite_file_path}"

engine = create_engine(database_url, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()