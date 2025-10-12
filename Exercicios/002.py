"""Três restaurantes: Comece com a classe do Exercício anterior. Crie três instâncias diferentes da classe e chame describe_restaurant() para cada instância."""

from modulos.Class_002 import Restaurante

japa_loko = Restaurante("japa loko", "japonesa", "refrigerantes" , True, True)
mc_donads = Restaurante("MC Donalds", "americana", "refrigerantes", True, False)
barreto = Restaurante("Barretos", "brasileira", "sucos", False, False)

print(f"\n {japa_loko.nome}")
print("-" * 20)
japa_loko.descrição_restaurante()

print(f"\n {mc_donads.nome}")
print("-" * 20)
mc_donads.descrição_restaurante()

print(f"\n {barreto.nome}")
print("-" * 20)
barreto.descrição_restaurante()