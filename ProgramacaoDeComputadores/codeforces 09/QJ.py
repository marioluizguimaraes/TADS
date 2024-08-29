numeroCandidatos = int(input())
minimo = int(input())
classificados = []
notasCandidatos = []
for i in range(numeroCandidatos):
    notas = int(input())
    notasCandidatos.append(notas)

notasOrdenadas = sorted(notasCandidatos)

for x in range(minimo):
    classificados.append(notasOrdenadas[len(notasOrdenadas)-(x+1)])

maiorNota = classificados[-1]

if (notasCandidatos.count(maiorNota) > 1):
    for y in range(classificados.count(maiorNota), notasCandidatos.count(maiorNota)):
        classificados.append(maiorNota)

print(len(classificados))