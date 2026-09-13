import os
import sys
import argparse

def ler_diretorio(caminho):
    print(f"[*] Iniciando varredura de I/O no diretório: {caminho}")
    arquivos_lidos = 0
    erros_permissao = 0

    if not os.path.exists(caminho):
        print(f"[!] Erro: O diretório '{caminho}' não existe.")
        sys.exit(1)

    try:
        # Percorre a pasta e todas as subpastas
        for root, dirs, files in os.walk(caminho):
            for arquivo in files:
                caminho_completo = os.path.join(root, arquivo)
                try:
                    # Lê os metadados do arquivo (gera I/O e page-faults)
                    os.stat(caminho_completo)
                    arquivos_lidos += 1
                except PermissionError:
                    erros_permissao += 1
                except FileNotFoundError:
                    pass
    except Exception as e:
        print(f"[!] Erro inesperado ao acessar os arquivos: {e}")

    print(f"[*] Varredura concluída! Arquivos lidos: {arquivos_lidos} | Erros de permissão: {erros_permissao}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simula um workload de leitura de disco (I/O Bound).")
    parser.add_argument("--path", type=str, default="/var/log", help="Diretório alvo para leitura")
    args = parser.parse_args()
    ler_diretorio(args.path)