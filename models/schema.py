from pydantic import BaseModel, conint, constr

from typing import List, Optional

class Product(BaseModel):
    name: constr(max_length=50)
    price: float
    category: str
    description: Optional[str]
    image_path: Optional[str]