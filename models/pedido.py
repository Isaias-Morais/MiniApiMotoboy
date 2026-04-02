from sqlalchemy.orm import Mapped,mapped_column,relationship
from decimal import Decimal
from sqlalchemy import ForeignKey, Numeric, Integer, func, String
from database.base import Base
from datetime import datetime
from models.enum import StatusPedidos as SqlEnum


class Pedidos(Base):
    __tablename__ = "pedidos"


    id : Mapped[int] = mapped_column(primary_key=True)
    usuario :Mapped[str] = mapped_column(nullable=False)
    descricao : Mapped[str] = mapped_column(nullable=False)
    observacao : Mapped[str] = mapped_column(nullable=False)
    endereco : Mapped[str] = mapped_column(nullable=False)
    valor : Mapped[Decimal] = mapped_column(Numeric(10,2),nullable=False)
    status : Mapped[SqlEnum] = mapped_column(String,nullable=False,default=SqlEnum.PENDENTE)
    data_de_criacao : Mapped[datetime] = mapped_column(server_default=func.now(),nullable=False)
    motoboy_id : Mapped[int] = mapped_column(Integer,ForeignKey('motoboy.id',ondelete='CASCADE'),nullable=True)

    motoboy : Mapped['Motoboy'] = relationship(back_populates='pedidos')

    def __repr__(self):
        return f'{self.id}|{self.descricao}|{self.observacao}|{self.valor}|{self.status}|{self.motoboy_id}|{self.data_de_criacao}'

