from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import schema, models


engine = create_engine('sqlite:///introfastapi.sqlite')

models.init_db(engine)

db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

app = FastAPI()


@app.get('/product/{product_id}')
def get_product(product_id: int):
    """Returns a product given its ID
    """
    product = db_session.query(models.Product).get(product_id)
    return product


@app.post('/product/')
def insert_product(product: schema.Product):
    db_session.add(
        models.Product(
            **dict(product)
        )
    )
    db_session.commit()
    return {'product': product, 'message': 'se ha insertado OK'}


@app.put('/product/{product_id}')
def update_product(product_id: int, product: schema.Product):
    """Update a product given its ID
    """
    product = dict(product)
    product['id'] = product_id
    db_session.merge(models.Product(**product))
    db_session.commit()
    return {'message': 'product updated OK',
            'product': product}
