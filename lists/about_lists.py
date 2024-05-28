# Lista
fruits_list = ['apple', 'manga', 'peach', 'orange', 'watermelon', 'grape']
print(fruits_list)

# Tupla
fruits_tuples = ('apple', 'manga', 'peach', 'orange', 'watermelon', 'grape')
print(fruits_tuples)

# Dicionário
people_dictionaries = {
    "Edgar": 32,
    "Rob": 40,
}
print(people_dictionaries["Edgar"])

# Criando dicionário com dict()
people_dict = dict(
    john=32,
    rob=45,
    tim=20
)
people_dict["mike"] = 30  # Adicionar 'mike'
del people_dict["mike"]    # Remover 'mike'
print(people_dict)

# Obtendo valores de dicionários
print(people_dictionaries.get("Rob"))

# Atualizando dicionários
prices = {'iphone': 500, 'ipad': 400}
new_prices = {'iphone': 600, 'imac': 1500}
prices.update(new_prices)  # Atualizar preços
prices.pop('ipad')         # Remover 'ipad'
print(prices)

# Obtendo chaves, valores e itens de dicionários
print(prices.values())  # Valores do dicionário
print(prices.keys())    # Chaves do dicionário
print(prices.items())   # Itens do dicionário (pares chave-valor)
