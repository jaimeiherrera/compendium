from sqlalchemy import Column, Integer, String

from .database import Base


class Demon(Base):
    __tablename__ = "demons"

    id = Column(Integer, primary_key=True, index=True,
                unique=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    url_image = Column(String)
