"""Importando Restaurant: Usando sua classe Restaurant mais recente, armazene-a em um módulo. Crie um arquivo separado que importe Restaurant. Crie uma instância de Restaurant e chame um de seus métodos para mostrar que a instrução import funciona de forma apropriada"""

import modulos.Class_010

ice_sabores = ["chocolate", "morango", "cereja"]
ice_sorveteria = modulos.Class_010.Sorveteria("ice", "sorveteria", ice_sabores)

ice_sorveteria.descrição()
ice_sorveteria.lista_sobres()
ice_sorveteria.info_entregas()