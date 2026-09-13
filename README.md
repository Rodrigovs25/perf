# Análise de Desempenho com perf stat

Este repositório contém scripts de demonstração para ilustrar o uso da ferramenta de perf para a disciplina
de Manutenção e Evolução de Software. O objetivo é demonstrar como o comando perf stat se comporta ao analisar diferentes perfis de carga de trabalho: **I/O Bound**, **Espera (Idle)** e **CPU Bound**.

---

## 1. Simulação de I/O Bound (Leitura de Disco)
O script leitura.py simula um programa que varre o disco lendo metadados de arquivos. É um processo rápido, mas que gera interrupções de hardware (Page Faults) para acessar informações do disco.

**Comando executado:**
```bash
sudo perf stat python3 leitura.py 
```

```text
[*] Iniciando varredura de I/O no diretório: /etc
[*] Varredura concluída! Arquivos lidos: 2770 | Erros de permissão: 0

 Performance counter stats for 'python3 leitura.py':

                 0      context-switches                 #      0,0 cs/sec  cs_per_second     
                 0      cpu-migrations                   #      0,0 migrations/sec  migrations_per_second
             1.128      page-faults                      #  34182,6 faults/sec  page_faults_per_second
             33,00 msec task-clock                       #      0,8 CPUs  CPUs_utilized       
         1.596.707      branch-misses                    #      4,6 %  branch_miss_rate         (47,64%)
        34.446.796      branches                         #   1043,9 M/sec  branch_frequency     (50,74%)
       141.795.943      cpu-cycles                       #      4,3 GHz  cycles_frequency       (68,90%)
       167.902.268      instructions                     #      1,2 instructions  insn_per_cycle  (52,36%)
        41.793.585      stalled-cycles-frontend          #     0,29 frontend_cycles_idle        (49,26%)

       0,034800860 seconds time elapsed

       0,012951000 seconds user
       0,021918000 seconds sys
```

## Passo 2: Simulação de Espera / Rede (Idle)
O script espera.py simula uma aplicação web ou API que faz uma requisição externa e fica aguardando a resposta, sem exigir esforço do processador.

**Comando executado:**
```bash
sudo perf stat python3 espera.py 
```

```text
[*] Simulação de espera de 3s (Ex: Aguardando Banco de Dados)...
[*] A CPU ficará livre neste período.
[*] Espera concluída! Tempo real decorrido no relógio: 3.00 segundos.

 Performance counter stats for 'python3 espera.py':

                 1      context-switches                 #     45,7 cs/sec  cs_per_second     
                 0      cpu-migrations                   #      0,0 migrations/sec  migrations_per_second
             1.115      page-faults                      #  51010,8 faults/sec  page_faults_per_second
             21,86 msec task-clock                       #      0,0 CPUs  CPUs_utilized       
           690.427      branch-misses                    #      4,8 %  branch_miss_rate         (46,54%)
        16.142.305      branches                         #    738,5 M/sec  branch_frequency     (47,24%)
        74.095.311      cpu-cycles                       #      3,4 GHz  cycles_frequency       (64,10%)
        73.742.748      instructions                     #      1,0 instructions  insn_per_cycle  (53,46%)
        20.502.069      stalled-cycles-frontend          #     0,31 frontend_cycles_idle        (52,76%)

       3,025103151 seconds time elapsed

       0,017901000 seconds user
       0,006961000 seconds sys
```

## Passo 3: Simulação de CPU Bound (Processamento Intensivo)
O script processamento.py possui um laço de repetição que exige 100% de capacidade de processamento de um núcleo. Utilizamos a flag -d(detailed) para ler métricas adicionais direto dos contadores do hardware (como cache L1).

**Comando executado:**
```bash
sudo perf stat -d python3 processamento.py
```

```text
[*] Iniciando cálculo matemático com 100,000,000 operações...
[*] O processador será levado ao limite neste núcleo.
[*] Processamento concluído! Tempo decorrido: 13.01 segundos.

 Performance counter stats for 'python3 processamento.py':

               137      context-switches                 #     10,5 cs/sec  cs_per_second     
                 7      cpu-migrations                   #      0,5 migrations/sec  migrations_per_second
             1.118      page-faults                      #     85,9 faults/sec  page_faults_per_second
         13.012,13 msec task-clock                       #      1,0 CPUs  CPUs_utilized       
         5.558.795      L1-dcache-load-misses            #      0,0 %  l1d_miss_rate            (42,85%)
         5.110.916      branch-misses                    #      0,0 %  branch_miss_rate         (42,85%)
    35.460.874.639      branches                         #   2725,2 M/sec  branch_frequency     (42,86%)
    52.213.101.604      cpu-cycles                       #      4,0 GHz  cycles_frequency       (42,87%)
   185.888.937.081      instructions                     #      3,6 instructions  insn_per_cycle  (42,87%)
     4.079.996.758      stalled-cycles-frontend          #     0,08 frontend_cycles_idle        (42,86%)

      13,025719469 seconds time elapsed

      13,007384000 seconds user
       0,006993000 seconds sys
```