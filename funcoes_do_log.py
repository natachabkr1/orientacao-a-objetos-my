# Dentro do espaço de nomes do meu mkódulo - funçõs do log, eu defini uma variável e uma função

nome_do_usuario = 'Dori'

def imprimir_no_log(texto, nivel='info'):
    if nivel == 'info':
        print(f'INFO: {texto}')
    elif nivel == 'alerta':
        print(f'ALERTA: {texto}')
    elif nivel == 'erro':
        print(f'ERRO: {texto}')
    else:
        print(f'[ERRO] Nível "{nivel}" não é válido!')
        