# Análise de Desempenho com perf stat

Este repositório contém scripts de demonstração para ilustrar o uso da ferramenta de perf para a disciplina
de Manutenção e Evolução de Software. O objetivo é demonstrar como o comando perf stat se comporta ao analisar diferentes perfis de carga de trabalho: **I/O Bound**, **Espera** e **CPU Bound**.

---

## 1. Simulação de I/O Bound (Leitura de Disco)
O script leitura.py simula um programa que varre o disco lendo metadados de arquivos. É um processo rápido, mas que gera interrupções de hardware (Page Faults) para acessar informações do disco.

**Comando executado:**
```bash
sudo perf stat python3 leitura.py 
```

```text
Iniciando varredura de I/O no diretório: /etc
Arquivos lidos: 2770 | Erros de permissão: 0

 Performance counter stats for 'python3 leitura.py':

                 6      context-switches                 #    180,0 cs/sec  cs_per_second     
                 0      cpu-migrations                   #      0,0 migrations/sec  migrations_per_second
             1.127      page-faults                      #  33819,2 faults/sec  page_faults_per_second
             33,32 msec task-clock                       #      0,7 CPUs  CPUs_utilized       
         1.599.339      branch-misses                    #      4,6 %  branch_miss_rate         (46,54%)
        33.729.700      branches                         #   1012,2 M/sec  branch_frequency     (49,72%)
       138.557.426      cpu-cycles                       #      4,2 GHz  cycles_frequency       (67,57%)
       167.274.210      instructions                     #      1,2 instructions  insn_per_cycle  (53,46%)
        41.325.657      stalled-cycles-frontend          #     0,30 frontend_cycles_idle        (50,28%)

       0,036165500 seconds time elapsed

       0,017013000 seconds user
       0,019014000 seconds sys
```

## Passo 2: Simulação de Espera / Rede (Idle)
O script espera.py simula uma aplicação web ou API que faz uma requisição externa e fica aguardando a resposta, sem exigir esforço do processador.

**Comando executado:**
```bash
sudo perf stat python3 espera.py 
```

```text
Simulação de espera de 3s 
A CPU ficará livre neste período.
Tempo: 3.00 segundos.

 Performance counter stats for 'python3 espera.py':

                 5      context-switches                 #    240,3 cs/sec  cs_per_second     
                 0      cpu-migrations                   #      0,0 migrations/sec  migrations_per_second
             1.116      page-faults                      #  53644,5 faults/sec  page_faults_per_second
             20,80 msec task-clock                       #      0,0 CPUs  CPUs_utilized       
           762.774      branch-misses                    #      4,6 %  branch_miss_rate         (45,83%)
        15.247.882      branches                         #    732,9 M/sec  branch_frequency     (53,12%)
        62.937.777      cpu-cycles                       #      3,0 GHz  cycles_frequency       (71,22%)
        65.057.753      instructions                     #      1,0 instructions  insn_per_cycle  (54,17%)
        20.491.575      stalled-cycles-frontend          #     0,31 frontend_cycles_idle        (46,88%)

       3,024258810 seconds time elapsed

       0,010901000 seconds user
       0,012883000 seconds sys
```

## Passo 3: Simulação de CPU Bound (Processamento Intensivo)
O script processamento.py possui um laço de repetição que exige 100% de capacidade de processamento de um núcleo. Utilizamos a flag -d para ler métricas adicionais direto dos contadores do hardware (como cache L1).

**Comando executado:**
```bash
sudo perf stat -d python3 processamento.py
```

```text
Iniciando cálculo com 100,000,000 operações...
Tempo: 11.87 segundos.

 Performance counter stats for 'python3 processamento.py':

               159      context-switches                 #     13,4 cs/sec  cs_per_second     
                 5      cpu-migrations                   #      0,4 migrations/sec  migrations_per_second
             1.118      page-faults                      #     94,1 faults/sec  page_faults_per_second
         11.877,81 msec task-clock                       #      1,0 CPUs  CPUs_utilized       
         6.025.767      L1-dcache-load-misses            #      0,0 %  l1d_miss_rate            (42,85%)
         4.583.500      branch-misses                    #      0,0 %  branch_miss_rate         (42,85%)
    32.961.874.607      branches                         #   2775,1 M/sec  branch_frequency     (42,85%)
    50.639.502.020      cpu-cycles                       #      4,3 GHz  cycles_frequency       (42,87%)
   176.414.125.819      instructions                     #      3,5 instructions  insn_per_cycle  (42,86%)
     4.106.774.673      stalled-cycles-frontend          #     0,08 frontend_cycles_idle        (42,87%)

      11,886748174 seconds time elapsed

      11,876041000 seconds user
       0,003997000 seconds sys
```