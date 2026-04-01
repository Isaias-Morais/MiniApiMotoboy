from sqlalchemy import Boolean, DateTime, func
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from database.base import Base
from datetime import datetime

class Motoboy(Base):
    __tablename__ = 'motoboy'


    id : Mapped[int] = mapped_column(primary_key=True)
    nome : Mapped[str] = mapped_column(nullable=False)
    veiculo : Mapped[str] = mapped_column(nullable=False)
    telefone : Mapped[str] = mapped_column(nullable=False)
    status_ativo : Mapped[bool] = mapped_column(Boolean,default=False)
    status_livre : Mapped[bool] = mapped_column(Boolean, default=False)
    ultimo_pedido : Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    data_de_criacao: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())

    pedidos : Mapped['Pedidos'] = relationship(back_populates='motoboy')

    def __repr__(self):
        return f'|{self.id}|{self.nome}|{self.veiculo}|{self.telefone}|{self.status_ativo}|'