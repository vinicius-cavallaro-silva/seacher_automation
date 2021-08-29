from datetime import datetime

import os
from pytz import timezone
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


ENGINE = create_engine('sqlite://', echo=False)
DBSESSION = scoped_session(sessionmaker(bind=ENGINE))
BASE = declarative_base()


def create_all():
    from model.searcher_table import SearcherModel
    BASE.metadata.create_all(ENGINE)


def cur_datetime():
    return datetime.now(tz=timezone('Europe/Rome'))
