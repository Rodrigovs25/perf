import time

carga = 100000000
print(f"[*] Iniciando cálculo com {carga:,} operações...")
print("[*] O processador será levado ao limite neste núcleo.")

inicio = time.time()

resultado = 0
# Laço pesado para forçar alto uso da CPU e gerar ciclos
for i in range(carga):
    resultado += (i * 2) - (i / 2)
    
fim = time.time()

print(f"[*] Processamento concluído! Tempo decorrido: {fim - inicio:.2f} segundos.")
