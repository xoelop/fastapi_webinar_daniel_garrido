from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Model = declarative_base(name='Model')


def init_db(engine):
    Model.metadata.create_all(bind=engine)


class Product(Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image_path = Column(String, nullable=True)
