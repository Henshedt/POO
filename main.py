from pessoa import Pessoa #Importa a classe com as funções dentro dela no file "pessoa.py".

p1 = Pessoa('', 0) #Determine nome e idade.

# p1.nome_da_função() Chama a função para Pessoa 1 ou Objeto.

p1.falar('POO') #Caso chame duas vezes falar() para mesma váriavel(pessoa), irá reproduzir um aviso sobre ela já estar falando.
p1.parar_falar() #Encerra a conversa para poder chamar outra com a função falar().

p1.comer('morango') #Caso chame duas vezes comer()para mesma váriavel(pessoa), irá reproduzir um aviso sobre p1 já estar comendo.
p1.parar_de_comer() #Encerra a função para poder chamar outro alimento em comer().

print(p1.ano_nascimento()) #Com base na idade determinada, calcula e retorna o ano do Nascimento da pessoa.
