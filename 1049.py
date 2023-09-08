aguia = ['vertebrado', 'ave', 'carnivoro']
pomba = ['vertebrado', 'ave', 'onivoro']
homem = ['vertebrado', 'mamifero', 'onivoro']
vaca = ['vertebrado', 'mamifero', 'herbivoro']
pulga = ['invertebrado', 'inseto', 'hematofago']
lagarta = ['invertebrado', 'inseto', 'herbivoro']
sanguessuga = ['invertebrado', 'anelideo', 'hematofago']
minhoca = ['invertebrado', 'anelideo', 'onivoro']

animais = [
    {'nome': 'aguia', 'caracteristicas': aguia},
    {'nome': 'pomba', 'caracteristicas': pomba},
    {'nome': 'homem', 'caracteristicas': homem},
    {'nome': 'vaca', 'caracteristicas': vaca}, 
    {'nome': 'pulga', 'caracteristicas': pulga}, 
    {'nome': 'lagarta', 'caracteristicas': lagarta}, 
    {'nome': 'sanguessuga', 'caracteristicas': sanguessuga}, 
    {'nome': 'minhoca', 'caracteristicas': minhoca}
           ]
grupo = input()
classe = input()
dieta = input()

animal_misterioso = [grupo, classe, dieta]

for animal in animais:
    if animal_misterioso == animal['caracteristicas']:
        print(animal['nome'])