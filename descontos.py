
from abc import ABC, abstractmethod


class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass


class ICupom(ABC):
    @abstractmethod
    def aplicar_cupom(self, codigo: str) -> bool:
        pass


class IVIP(ABC):
    @abstractmethod
    def validar_usuario_vip(self, usuario: str) -> bool:
        pass


class DescontoNormal(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1


class DescontoVIP(Desconto, ICupom, IVIP):
    def calcular(self, valor: float) -> float:
        return valor * 0.2

    def aplicar_cupom(self, codigo: str) -> bool:
        return codigo == "DESC10"

    def validar_usuario_vip(self, usuario: str) -> bool:
        return usuario == "VIP"


class DescontoPremium(Desconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.3


def aplicar_desconto(desconto: Desconto, valor: float) -> float:
    return desconto.calcular(valor)


class Pedido:
    def __init__(self, desconto: Desconto) -> None:
        self.desconto = desconto

    def calcular_preco_final(self, valor: float) -> float:
        return valor - self.desconto.calcular(valor)



if __name__ == "__main__":
    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print("Desconto normal:", aplicar_desconto(normal, valor))
    print("Desconto VIP:", aplicar_desconto(vip, valor))
    print("Desconto Premium:", aplicar_desconto(premium, valor))
    print("Cupom VIP:", vip.aplicar_cupom("DESC10"))

    pedido = Pedido(DescontoNormal())
    print("Preço final do pedido:", pedido.calcular_preco_final(valor))
