# Скрипт для контроля (покупки/продажи энергии)
import ips

psm = ips.init()

clients = psm.powersystem.get_all_clients()
total_consumption = 0 # прогноз суммарного потребления
total_generation = 0 # прогноз суммарной генерации

# все значения клиентов положительные
for client in clients:
    if client.is_generator():
        total_generation += client.power[-1] if client.power else 0
    else:
        total_consumption += client.power[-1] if client.power else 0

total_consumption *= 1.25
total_generation *= 0.75

energy_difference = total_consumption - total_generation

if energy_difference > 0:
    psm.orders.trade0.buy(energy_difference)
else:
    psm.orders.trade0.sell(-energy_difference)