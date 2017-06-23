from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from models import db


class Page(db.Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    site_id = Column(ForeignKey)
    url = Column(String)
    created = Column(DateTime)
    last_parse = Column(DateTime)
