# Requisito 1
import csv
from collections import Counter


def criar_lista_de_pedidos(path_to_file):
    with open(path_to_file, "r") as file:
        keys = ["nome_do_cliente", "prato_pedido", "dia_da_semana"]
        dicionario_de_pedidos = csv.DictReader(file, fieldnames=keys)
        lista_de_pedidos = []
        [lista_de_pedidos.append(pedido) for pedido in dicionario_de_pedidos]
    return lista_de_pedidos


def prato_mais_pedido(nome_do_cliente, lista_de_pedidos):
    pratos_pedidos = [
        pedido["prato_pedido"]
        for pedido in lista_de_pedidos
        if pedido["nome_do_cliente"] == nome_do_cliente
    ]
    contagem = Counter(pratos_pedidos)
    prato_mais_pedido = contagem.most_common(1)[0][0]
    return prato_mais_pedido


def quantidade_pedida(nome_do_cliente, prato_pedido, lista_de_pedidos):
    pratos_pedidos = [
        pedido["prato_pedido"]
        for pedido in lista_de_pedidos
        if pedido["nome_do_cliente"] == nome_do_cliente
    ]
    contagem = Counter(pratos_pedidos)
    quantidade_pedida = contagem.get(prato_pedido)
    return quantidade_pedida


def pratos_sem_pedidos(nome_do_cliente, lista_de_pedido):
    todos_os_pratos = {pedido["prato_pedido"] for pedido in lista_de_pedido}
    pratos_pedidos = {
        pedido["prato_pedido"]
        for pedido in lista_de_pedido
        if pedido["nome_do_cliente"] == nome_do_cliente
    }
    pratos_sem_pedidos = todos_os_pratos.symmetric_difference(pratos_pedidos)
    return pratos_sem_pedidos


def dias_sem_ir(nome_do_cliente, lista_de_pedido):
    todos_os_dias = {pedido["dia_da_semana"] for pedido in lista_de_pedido}
    dias_frequentados = {
        pedido["dia_da_semana"]
        for pedido in lista_de_pedido
        if pedido["nome_do_cliente"] == nome_do_cliente
    }
    dias_sem_ir = todos_os_dias.symmetric_difference(dias_frequentados)
    return dias_sem_ir


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        arquivo_texto = "data/mkt_campaign.txt"
        lista_de_pedidos = criar_lista_de_pedidos(path_to_file)
        prato_mais_pedido_maria = prato_mais_pedido("maria", lista_de_pedidos)
        quantidade_pedida_hamburguer_arnaldo = quantidade_pedida(
            "arnaldo", "hamburguer", lista_de_pedidos
        )
        pratos_sem_pedidos_joao = pratos_sem_pedidos("joao", lista_de_pedidos)
        dias_sem_ir_joao = dias_sem_ir("joao", lista_de_pedidos)
        conteudo_arquivo = [
            f"{prato_mais_pedido_maria}\n",
            f"{quantidade_pedida_hamburguer_arnaldo}\n",
            f"{pratos_sem_pedidos_joao}\n",
            f"{dias_sem_ir_joao}",
        ]
        with open(arquivo_texto, "w") as arquivo:
            arquivo.writelines(conteudo_arquivo)
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
