from pydantic import BaseModel

class LivroBase (BaseModel):
    titulo:str
    descricao:str
    numero_pag:int

class LivroRequest(LivroBase):
    ...

class LivroResponse(LivroBase):
    id: int

    class Config():
        orm_mode = True