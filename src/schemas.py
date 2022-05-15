from pydantic import BaseModel


class DemonBase(BaseModel):
    name: str
    description: str = None
    url_image: str = None


class DemonCreate(DemonBase):
    pass


class Demon(DemonBase):
    id: int
    name: str
    description: str = None
    url_image: str = None

    class Config:
        orm_mode = True
