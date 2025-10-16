"""Pessoas atendidas: Comece com seu programa do Exercício 001. Acrescente um atributo chamado number_served cujo valor default é 0. Crie uma instância chamada restaurant a partir dessa classe. Apresente o número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente. Adicione  um  método  chamado  set_number_served() que permita definir o número de clientes atendidos. Chame esse método com um novo número e mostre o valor novamente.
Acrescente  um  método  chamado  increment_number_served() que permita incrementar o número de clientes servidos. Chame esse método com qualquer número que você quiser e que represente quantos clientes foram  atendidos, por exemplo, em um dia de funcionamento"""

from modulos.Class_004 import Restaurante

japa_loko = Restaurante("Japa Loko", "japonesa")

print(f"Restaurante - {japa_loko.nome.title()}")
japa_loko.descrição_restaurante()
japa_loko.total_qnt_servidos()
japa_loko.total_qnt_servidos()
japa_loko.total_qnt_servidos()