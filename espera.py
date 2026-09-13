import time

tempo_espera = 3
print(f"[*] Simulação de espera de {tempo_espera}s ")
print("[*] A CPU ficará livre neste período.")

inicio = time.time()
time.sleep(tempo_espera) # O programa dorme e libera a CPU
fim = time.time()

print(f"[*] Espera concluída! Tempo real decorrido no relógio: {fim - inicio:.2f} segundos.")
