from sqlalchemy import Column, Integer, String

from models import db


class Site(db.Base):
    __tablename__ = 'site'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created = Column(String)
