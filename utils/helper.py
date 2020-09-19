def formata_float_str_moeda(valor: float) -> str:
    valor = str(valor).replace('.', ',')
    return f'R$ {valor}'
