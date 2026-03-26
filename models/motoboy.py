from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from database.base import Base

class Motoboy(Base):
    __tablename__ = 'motoboy'


    id : Mapped[int] = mapped_column(primary_key=True)
    nome : Mapped[str] = mapped_column(nullable=False)
    veiculo : Mapped[str] = mapped_column(nullable=False)
    telefone : Mapped[str] = mapped_column(nullable=False)
    status_ativo : Mapped[bool] = mapped_column(Boolean,default=False)

    pedidos : Mapped['Pedidos'] = relationship(back_populates='motoboy')

    def __repr__(self):
        return f'|{self.id}|{self.nome}|{self.veiculo}|{self.telefone}|{self.status_ativo}|'