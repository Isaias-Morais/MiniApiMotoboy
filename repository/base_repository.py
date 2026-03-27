from sqlalchemy.orm import Session


def salvar_objeto(session:Session, objeto):
    session.add(objeto)
    session.commit()
    session.refresh(objeto)
    return objeto