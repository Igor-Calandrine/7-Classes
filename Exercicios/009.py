"""Upgrade de bateria: Use a última versão de electric_car.py desta seção. Acrescente um método chamado upgrade_battery() na classe Battery. Esse método deve verificar a capacidade da bateria e defini-la com 85 se o valor for diferente. Crie um carro elétrico com uma capacidade de bateria default, chame get_range() uma vez e, em seguida, chame get_range() uma segunda vez após fazer um upgrade da bateria. Você deverá ver um aumento na distância que o carro é capaz de percorrer"""

from modulos.Class_009 import Carro, Carro_Eletrico, Bateria

my_tesla = Carro_Eletrico("tesla", "modelo s", 2025)

my_tesla.bateria.bateria_descricao()
my_tesla.bateria.bateria_melhoria()
my_tesla.bateria.bateria_descricao()
my_tesla.capacidade_desclocamento()