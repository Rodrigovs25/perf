# Análise de Desempenho com `perf stat`

Este repositório contém scripts de demonstração para ilustrar o uso da ferramenta de `perf` para a disciplina
de Manutenção e Evolução de Software. O objetivo é demonstrar como o comando `perf stat` se comporta ao analisar diferentes perfis de carga de trabalho: **I/O Bound**, **Espera (Idle)** e **CPU Bound**.

---

## 1. Simulação de I/O Bound (Leitura de Disco)
O script `leitura.py` simula um programa que varre o disco lendo metadados de arquivos. É um processo rápido, mas que gera interrupções de hardware (Page Faults) para acessar informações do disco.

**Comando executado:**
```bash
sudo perf stat python3 leitura.py --path /etc
```

```text
[*] Iniciando varredura de I/O no diretório: /etc
[*] Varredura concluída! Arquivos lidos: 2770 | Erros de permissão: 0

 Performance counter stats for 'python3 leitura.py --path /etc':

                 2      context-switches                 #      15,6 cs/sec  cs_per_second      
                 0      cpu-migrations                   #       0,0 migrations/sec  migrations_per_second
             1.487      page-faults                      #  11568,9 faults/sec  page_faults_per_second
            128,53 msec task-clock                       #       0,9 CPUs  CPUs_utilized        
         2.026.592      branch-misses                    #       4,7 %  branch_miss_rate         (49,73%)
        42.679.431      branches                         #   332,0 M/sec  branch_frequency      (50,55%)
       175.897.699      cpu-cycles                       #       1,4 GHz  cycles_frequency       (67,42%)
       203.930.234      instructions                     #       1,2 instructions  insn_per_cycle  (50,27%)
        54.107.267      stalled-cycles-frontend          #      0,31 frontend_cycles_idle        (49,45%)

       0,133541088 seconds time elapsed

       0,080744000 seconds user
       0,052832000 seconds sys
```

## Passo 2: Simulação de Espera / Rede (Idle)
Simula uma aplicação web ou API que faz uma requisição externa e fica aguardando a resposta, sem exigir esforço do processador.

**Comando executado:**
```bash
sudo perf stat python3 espera.py --tempo 3
```

```text
[*] Iniciando simulação de espera (Ex: Aguardando Banco de Dados ou API externa)...
[*] O programa vai dormir por 3.0 segundos. A CPU ficará livre.
[*] Espera concluída! Tempo real decorrido no relógio: 3.00 segundos.

 Performance counter stats for 'python3 espera.py --tempo 3':

                 2      context-switches                 #      28,2 cs/sec  cs_per_second      
                 0      cpu-migrations                   #       0,0 migrations/sec  migrations_per_second
             1.469      page-faults                      #  20679,8 faults/sec  page_faults_per_second
             71,04 msec task-clock                       #       0,0 CPUs  CPUs_utilized        
         1.203.884      branch-misses                    #       5,0 %  branch_miss_rate         (48,40%)
        23.460.572      branches                         #   330,3 M/sec  branch_frequency      (49,43%)
        97.125.225      cpu-cycles                       #       1,4 GHz  cycles_frequency       (66,31%)
       110.079.782      instructions                     #       1,1 instructions  insn_per_cycle  (51,60%)
        31.545.503      stalled-cycles-frontend          #      0,32 frontend_cycles_idle        (50,57%)

       3,076789084 seconds time elapsed

       0,052398000 seconds user
       0,024183000 seconds sys
```

## Passo 3: Simulação de CPU Bound (Processamento Intensivo)
Possui um laço de repetição que exige 100% de capacidade de processamento de um núcleo. Utilizamos a flag `-d` (detailed) para ler métricas adicionais direto dos contadores do hardware (como cache L1).

**Comando executado:**
```bash
sudo perf stat python3 processamento.py --carga 50000000
```

```text
[*] Iniciando cálculo matemático intensivo com 50,000,000 operações...
[*] O processador será levado ao limite neste núcleo.
[*] Processamento concluído! Tempo decorrido: 10.23 segundos.

 Performance counter stats for 'python3 processamento.py --carga 50000000':

                95      context-switches                 #      9,2 cs/sec  cs_per_second     
                 1      cpu-migrations                   #      0,1 migrations/sec  migrations_per_second
             1.476      page-faults                      #    143,4 faults/sec  page_faults_per_second
         10.295,56 msec task-clock                       #      1,0 CPUs  CPUs_utilized       
         5.360.620      L1-dcache-load-misses            #      0,0 %  l1d_miss_rate            (42,86%)
         4.011.444      branch-misses                    #      0,0 %  branch_miss_rate         (42,86%)
    10.352.040.751      branches                         #   1005,5 M/sec  branch_frequency     (42,85%)
    16.997.741.316      cpu-cycles                       #      1,7 GHz  cycles_frequency       (42,86%)
    52.789.840.100      instructions                     #      3,1 instructions  insn_per_cycle  (42,86%)
     2.828.041.381      stalled-cycles-frontend          #     0,17 frontend_cycles_idle        (42,86%)

      10,299179381 seconds time elapsed

      10,278457000 seconds user
       0,021007000 seconds sys

```