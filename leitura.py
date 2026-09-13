import os

caminho = "/etc"
print(f"Iniciando varredura de I/O no diretório: {caminho}")

arquivos_lidos = 0
erros_permissao = 0

# Percorre a pasta ignorando arquivos bloqueados pelo sistema
for root, dirs, files in os.walk(caminho):
    for arquivo in files:
        try:
            caminho_completo = os.path.join(root, arquivo)
            os.stat(caminho_completo)
            arquivos_lidos += 1
        except PermissionError:
            erros_permissao += 1

print(f"Arquivos lidos: {arquivos_lidos} | Erros de permissão: {erros_permissao}")
