from sqlalchemy import Column, INTEGER, VARCHAR, DateTime

from model.conection_db import BASE, DBSESSION, cur_datetime


class SearcherModel(BASE):
    __tablename__ = 'searcher_table'

    created = Column(DateTime, default=cur_datetime)
    updated = Column(DateTime, default=cur_datetime, onupdate=cur_datetime)

    id = Column(INTEGER, autoincrement=True, primary_key=True)
    photo_name = Column(VARCHAR(200), nullable=False)
    link_searched = Column(VARCHAR(200), nullable=False)

    def __init__(self,
                 link_searched: str,
                 photo_name: str):
        self.link_searched = link_searched
        self.photo_name = photo_name

    @classmethod
    def create_or_update(cls,
                         link_searched: str,
                         photo_name: str) -> 'SearcherModel':
        data = DBSESSION.query(cls).filter_by(photo_name=photo_name).first()

        if data:
            data.link_searched = link_searched or data.link_searched
            DBSESSION.commit()
            return data

        new_searcher = SearcherModel(link_searched=link_searched, photo_name=photo_name)

        DBSESSION.add(new_searcher)
        DBSESSION.commit()
        return new_searcher
