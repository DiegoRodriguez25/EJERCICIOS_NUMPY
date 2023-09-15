import numpy as np

votos = np.zeros(30, dtype=int)

esuis = 5000
votosg = np.random.randint(1, 31, size=esuis)

for voto in votosg:
    votos[voto-1] += 1

ordenado = np.argsort(votos)[::-1]


print("Listado de candidatos por número de votos:")
for i, indice in enumerate(ordenado):
    candidato = indice + 1
    votoobtenido = votos[indice]
    print(f"Candidato {candidato}: {votoobtenido} votos")

#LOS VOTOS SON GENERADOS ALEATORIAMENTE USANDO EL COMANDO "np.radnom.randint" DONDE LA SUMA DE TODOS LOS VOTOS SERÁ 5000 (en teoría, espero no quedar mal)