import time
import argparse

def simular_espera(segundos):
    print("[*] Iniciando simulação de espera (Ex: Aguardando Banco de Dados ou API externa)...")
    print(f"[*] O programa vai dormir por {segundos} segundos. A CPU ficará livre.")
    
    inicio = time.time()
    time.sleep(segundos)
    fim = time.time()
    
    print(f"[*] Espera concluída! Tempo real decorrido no relógio: {fim - inicio:.2f} segundos.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simula um workload ocioso (Sleep/Wait).")
    parser.add_argument("--tempo", type=float, default=2.0, help="Tempo de espera em segundos")
    args = parser.parse_args()
    simular_espera(args.tempo)