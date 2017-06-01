
from sqlalchemy import Column, Integer, String, ForeignKey

from models import db


class Resource(db.Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True)
    page_id = Column(ForeignKey)
    created = Column(DateTime)
    path = Column(String)
    type = Column(String)
