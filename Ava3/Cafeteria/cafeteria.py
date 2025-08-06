import simpy
import time
import random
import sys

# Cafeteria Café Aqui Teria

total_espera = 0.0           # Soma de todos os tempos de espera na fila
total_sistema = 0.0          # Soma dos tempos totais no sistema (espera + atendimento)
tempo_ocupado = 0.0          # Tempo total em que a balcao esteve ocupada
clientes_atendidos = 0       # Contador de clientes atendidos
media_chegada_clients = 7    # Media da frequencia da chegada de clientes
media_de_atendimento = 5     # Media do tempo de atendimento

def cliente(env, nome, balcao):
    global total_espera, total_sistema, tempo_ocupado, clientes_atendidos, media_de_atendimento  # Acesso às variáveis globais

    chegada = env.now

    with balcao.request() as req:
        yield req
        inicio_servico = env.now             # Tempo em que o cliente começa a ser atendido
        espera = inicio_servico - chegada    # Calcula o tempo de espera

        duracao = random.expovariate(1.0/media_chegada_clients)
        tempo_ocupado += duracao             # Acumula o tempo que a balcao será usada

        yield env.timeout(duracao)
        fim = env.now

        tempo_total = fim - chegada          # Tempo total no sistema
        total_espera += espera               # Atualiza estatística de espera
        total_sistema += tempo_total         # Atualiza estatística de tempo total
        clientes_atendidos += 1              # Contabiliza cliente atendido

def gerador(env, balcao):
    global media_chegada_clients
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0/media_chegada_clients))
        i += 1
        env.process(cliente(env, f"Cliente {i}", balcao))

def main():
    global media_chegada_clients , media_de_atendimento
    media_chegada_clients = float( sys.argv[1] )
    media_de_atendimento = float( sys.argv[2] )
    run_time = float( sys.argv[3])
    random.seed(int(time.time()))
    env = simpy.Environment()
    balcao = simpy.Resource(env, capacity=1)
    env.process(gerador(env, balcao))
    env.run(until=run_time)

    # Relatório
    if clientes_atendidos > 0:
        media_espera = total_espera / clientes_atendidos
        media_total = total_sistema / clientes_atendidos
        utilizacao = tempo_ocupado / run_time
        # Saída CSV
        print(f"{run_time},{media_chegada_clients},{media_de_atendimento},{clientes_atendidos},{media_espera:.4f},{media_total:.4f},{utilizacao:.4f}")
    else:
        print("Nenhum cliente atendido.")

main()

