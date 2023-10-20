class Fatura:
    def __init__(self, nome='fatura', preco=0, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco * self.quantidade

        return (f"Fatura do item {self.nome}\n"
                f"Preço: {self.preco}\n"
                f"Quantidade: {self.quantidade}\n"
                f"Valor total: {self.valor_total}")

fatura = Fatura(preco=250, quantidade=2, nome='Teclado Mecanico')

print(fatura.gerar_fatura())
