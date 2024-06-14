from datetime import datetime
from pprint import pprint
from typing import Tuple, Annotated
from uuid import UUID, uuid4

from annotated_types import Gt
from pydantic import BaseModel, ValidationError, PositiveInt, Field


# class User:
#     def __init__(self, uid: int, name: str, birthdate: datetime):
#         assert isinstance(uid, int)
#         self.uid = uid
#
#         assert isinstance(name, str)
#         self.name = name
#
#         assert isinstance(birthdate, datetime)
#         self.birthdate = birthdate


# reza = User(uid=1, name="reza", birthdate=datetime.now())
# reza = User(uid='1', name="reza", birthdate=datetime.now())

# print(reza)


# class User(BaseModel):
#     uid: int
#     name: str
#     birthdate: datetime | None = None
#     dimensions: Tuple[int, int] | None = None
#     is_active: bool = False
#     tastes: dict[str, PositiveInt] | None = None


# reza = User(uid=1, name="reza", birthdate=datetime.now())
# reza = User(uid='1', name="reza", birthdate=datetime.now())
# reza = User(uid='1', name="reza", birthdate="2024-06-12 20:30")

# try:
#     reza = User(uid=20.989, name="reza", birthdate="salam dfsfsdf f sfsfs f sf")
# except ValidationError as e:
#     pprint(e.errors())

# reza = User(
#     uid='1',
#     name="reza",
#     birthdate="2024-06-12 20:30",
#     dimensions=['1', '12'],
#     is_active='y',
#     # tastes={
#     #     "cookie": 10,
#     #     "stake": 2,
#     #     "one-h": 123,
#     # }
# )


# pprint(dict(reza))
# pprint(reza.model_fields_set)


class Sizes(BaseModel):
    x: Annotated[int, Gt(0)]
    y: Annotated[int, Gt(0)]


class Square(BaseModel):
    sizes: Sizes
    color: str


# my_square = Square(sizes=Sizes(x=10, y='1'), color="red")
# my_square = Square(sizes={'x': 10, 'y': 1}, color="red")
# pprint(dict(my_square))
# pprint(my_square.model_dump())

class User(BaseModel):
    id: str = Field(max_length=32, min_length=32, default_factory=lambda: uuid4().hex, init=False)


reza = User()
# reza = User(id=uuid4().hex)
pprint(reza.model_dump())
