import time

tempo_espera = 3
print(f"Simulação de espera de {tempo_espera}s ")
print("A CPU ficará livre neste período.")

inicio = time.time()
time.sleep(tempo_espera)
fim = time.time()

print(f"Tempo: {fim - inicio:.2f} segundos.")
