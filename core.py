from sqlalchemy.orm import Session

from models import Livro

class LivroCore:
    def find_all(db: Session):
        return db.query(Livro).all()

    def save(db: Session, livro:Livro):
        if livro.id:
            db.merge(Livro)
        else:
            db.add(livro)
        db.commit()
        return livro

    def find_by_id(db:Session, id:int) -> Livro:
        return db.query(Livro).filter(Livro.id == id).first() is not None

    def find_by_tittle(db:Session, titulo:str) -> Livro:
        return db.query(Livro).filter(Livro.titulo == titulo).first() is not None 

    def exists_by_id(db: Session, id: int):
        return db.query(Livro).filter(Livro.id == id).first() is not None

    def delete_by_id(db: Session, id: int):
        livro = db.query(Livro).filter(Livro.id == id).first()
        if livro is not None:
            db.delete(livro)
            db.commit()