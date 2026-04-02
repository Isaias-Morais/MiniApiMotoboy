from enum import Enum

class StatusPedidos(str,Enum):
    PENDENTE = 'pendente'
    PREPARO = 'preparando'
    CANCELADO = 'cancelado'
    PRONTO = 'pronto'
    EM_ROTA = 'em_rota'
    ENTREGUE = 'entregue'
    FALHA_NA_ENTREGA = 'falha_na_entrega'