from disciplinas import Disciplina
from professores import Professor

p1 = Professor(nome="Fernando", ra='123456')
d1 = Disciplina(nome="LP2", cargaHoraria=80, mensalidade=700, professor=p1)

p1.adicionaDisciplina(d1)
print("Carga Horária: ", p1.retornaCargaHoraria())

print("Valor/Hora da disciplina: ", d1.retornaValorHora())
