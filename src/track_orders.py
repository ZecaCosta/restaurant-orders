from collections import Counter


class TrackOrders:
    def __init__(self):
        self.lista_de_pedidos = []

    def __len__(self):
        return len(self.lista_de_pedidos)

    def add_new_order(self, costumer, order, day):
        self.lista_de_pedidos.append({"nome_do_cliente": costumer,
                                      "prato_pedido": order,
                                      "dia_da_semana": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        pratos_pedidos = [
            pedido["prato_pedido"]
            for pedido in self.lista_de_pedidos
            if pedido["nome_do_cliente"] == costumer
        ]
        contagem = Counter(pratos_pedidos)
        prato_mais_pedido = contagem.most_common(1)[0][0]
        return prato_mais_pedido

    def get_never_ordered_per_costumer(self, costumer):
        todos_os_pratos = {pedido["prato_pedido"]
                           for pedido in self.lista_de_pedidos}
        pratos_pedidos = {
            pedido["prato_pedido"]
            for pedido in self.lista_de_pedidos
            if pedido["nome_do_cliente"] == costumer
        }
        pratos_sem_pedidos = todos_os_pratos.symmetric_difference(
                                pratos_pedidos)
        return pratos_sem_pedidos

    def get_days_never_visited_per_costumer(self, costumer):
        todos_os_dias = {pedido["dia_da_semana"]
                         for pedido in self.lista_de_pedidos}
        dias_frequentados = {
            pedido["dia_da_semana"]
            for pedido in self.lista_de_pedidos
            if pedido["nome_do_cliente"] == costumer
        }
        dias_sem_ir = todos_os_dias.symmetric_difference(
                        dias_frequentados)
        return dias_sem_ir

    def get_busiest_day(self):
        dias_frequentados = [
            pedido["dia_da_semana"]
            for pedido in self.lista_de_pedidos
        ]

        contagem = Counter(dias_frequentados)
        dia_mais_frequentado = max(contagem, key=contagem.get)
        return dia_mais_frequentado

    def get_least_busy_day(self):
        dias_frequentados = [
            pedido["dia_da_semana"]
            for pedido in self.lista_de_pedidos
        ]

        contagem = Counter(dias_frequentados)
        dia_menos_frequentado = min(contagem, key=contagem.get)
        return dia_menos_frequentado

    def get_dish_quantity_per_costumer(self, costumer, order):
        pratos_pedidos = [
            pedido["prato_pedido"]
            for pedido in self.lista_de_pedidos
            if pedido["nome_do_cliente"] == costumer
        ]
        contagem = Counter(pratos_pedidos)
        quantidade_pedida = contagem.get(order)
        return quantidade_pedida
