from sqlalchemy import Column, Integer, Text

from database import Base 

class Livro(Base):
    _tablename_ = 'livros'

    id: int = Column(Integer, primary_key= True, index = True)
    titulo: str = Column(String(100), nullable = True)
    descricao: str = Column(String(100), nullable = True)
    numero_pag: int = Column(Integer, nullable = True)