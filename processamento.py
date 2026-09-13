import argparse
import time

def processamento_pesado(iteracoes):
    print(f"[*] Iniciando cálculo matemático intensivo com {iteracoes:,} operações...")
    print("[*] O processador será levado ao limite neste núcleo.")
    
    inicio = time.time()
    
    # Laço matemático para forçar o uso da CPU (Instruções e Ciclos)
    resultado = 0
    for i in range(iteracoes):
        resultado += (i * 2) - (i / 2)
        
    fim = time.time()
    
    print(f"[*] Processamento concluído! Tempo decorrido: {fim - inicio:.2f} segundos.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simula um workload pesado (CPU Bound).")
    # Padrão é 30 milhões de loops. Ajuste na hora se precisar que demore mais ou menos
    parser.add_argument("--carga", type=int, default=30000000, help="Número de iterações matemáticas")
    args = parser.parse_args()
    processamento_pesado(args.carga)