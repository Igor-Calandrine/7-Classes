"""
Importanto Classes
    À medida que acrescentar mais funcionalidades às classes, seus arquivos ficarão maiores, mesmo quando usar herança de forma apropriada. Para estar de acordo com a filosofia geral de Python, quanto menos entulhados estiverem seus arquivos, melhor será. Escreva uma docstring que descreve rapidamente o conteúdo de cada módulo que criar.
    
    Ex:Uma classe que pode ser usada para representar um carro.
       class Carro():
    
    Depois de criar um arquivo separado, por exemplo car, esse arquivo importará a classe Carro e então criará uma instância dessa classe:
    
    Ex: from car import Carro
    
    A instrução #import diz a Python para abrir o módulo #car e importar a classe #Carro. Agora podemos usar a classe como se ela estivesse definida nesse arquivo.
    Quando transferimos a classe para um módulo e o importamos, continuamos usufruindo da mesma funcionaliade, porém o arquivo com o programa principal permanece limpo e fácil de ler. Também armazenamos a maior parte da lógica em arquivos separados. Depois que suas classes estiverem funcionando conforme esperado, você poderá deixar de lado esses arquivos e se concentrar na lógica de mais alto nível de seu programa principal.
    
Armazenando e Importando várias classes em um módulo
    Você pode armazenar tantas classes quantas forem necessárias em um único módulo, embora cada classe deva estar relacionada com outra.
    Podemos importar ta,bém quantas classes forem necessárias em um arquivo de programa. Se quisermo criar um carro comum e um carro elétrico no mesmo mesmo carquivo, precisamos importar tanto a classe #Carro quanro a #Carro_Eletrico.
    Observe que como já foi visto, a vírgula separada cada classe.
    
    Ex: from car import Carro, Carro_Eletrico
    
Importando um módulo completo
    Também podemos importar um módulo completo e então acessar as classes necessárias usando a notação do ponto. Essa abordagem é simples e resulta em um código fácil de ler. Como toda chamada que cria uma instância de uma classe inclui o nome do módulo, você não terá conflito de nomes com qualquer nome usado no arquivo atual.
    
    Ex: import car
    
    Para acessar as classes iremos fazer:
        nome_do_modulo.nome_da_classe.
    
    meu_c3 = car.Carro('Citroen', 'C3', '2024')
    meu_tesla = car.Carro_Eletrico('Tesla', 'roadster', 2025)
    
Importando todas as classes de um módulo
    Esse método não é recomendado por dois motivos:
    Em primeiro lugar é conveniente ser capaz de ler as instruções #import no início de um arquivo e ter uma noção clara de quais classes um programa utiliza. Com essa abordagem não fica claro quais são as classes do módulo que você está usando. 
    Em segundo lugar, se você acidetalmente importar uma classes com o mesmo nome que outri item em se arquivo de programa, poderá gerar erros difíceis de serem diagnosticados.
    Se precisar importar muitas classes de um módulo, é melhor importar o módulo todo e usar a sintaxe 
    
        nome_do_modulo.nome_da_classe.
    
    Você não verá todas as classes usadas no início do arquivo, mas verá claramente em que lugares o módulo é utilizado no programa. Possíveis conlitos de nomes que possam ocorrrer ao importar todas as classes de um módulo também serão evitados.
    
Importando um módulo em um módulo
    Às vezes você vai querer esoalhar suas classes em vários módulos para impedir que um arquivo cresça demais e evitar a armazenagem de classes não relacionadas o mesmo módulo. Ao armazenar suas classes em várias módulos, você poderá descobrir que uma classe em um módulo depende de uma classe que está em outro módulo. Se isso acontecer, importe a classe necessária no primeiro módulo.
    Como exemplo utilizaresmos:
    
    class Carro - classe-pai - Contido no módulo car
    class Carro_Eletrico - classe-filha - Contido no módulo eletric_car
    class Bateria - classe-filha - Contido no módulo eletric_car
    
    Vamos super que seja colocado a classe-pai em um módulo diferente, então a classe filha deve importar a class-pai direntamente no módulo da classe-filha.
    
    Ex: no módulo da classe-filha iremos importar:
        
        from car import Carro
        
    Quando criarmos o tipo de carro que for necessário, devemos importar os dois módulos separadamente
    
    Ex: from car import Carro
        from eletric_car import Carro_Eletrico
       
Definindo o seu próprio fluzo de trabalho
    Quando estiver começando a programar, mantenho a estrutura de seu código simples. Procure fazer tudo em um só arquivo e transifra suas classes para módulas separadas depois que tudo estiver funcionando. Se gostar do modo como so módulas e os arquivos interagem, experimente armazenar suas classes em módulos quando inicar um projeto."""





