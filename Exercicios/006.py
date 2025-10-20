"""Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma classe chamada IceCreamStand que herde da classe Restaurant escrita no Exercício 1 ou no Exercício 4. Qualquer versão da
classe funcionará; basta escolher aquela de  que você mais gosta. Adicione um atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de IceCreamStand e chame esse método."""

from modulos.Class_006 import Restaurante, Sorveteria

ice_sabores = ["chocolate", "morango", "cereja"]
ice_sorveteria = Sorveteria("ice", "sorveteria", ice_sabores)

ice_sorveteria.descrição()
ice_sorveteria.lista_sobres()
ice_sorveteria.info_entregas()