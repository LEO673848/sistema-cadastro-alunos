alunos = {}
 
while True:
print("\n=== SISTEMA DE ALUNOS ===")
print("1 - Cadastrar aluno")
print("2 - Consultar aluno")
print("3 - Listar alunos")
print("4 - Sair")
 
opcao = input("Escolha uma opção: ")
 
if opcao == "1":
nome = input("Nome do aluno: ")
idade = input("Idade: ")
turma = input("Turma: ")
 
alunos[nome] = {
"idade": idade,
"turma": turma
}
 
print("Aluno cadastrado com sucesso!")
 
elif opcao == "2":
nome = input("Nome do aluno: ")
 
if nome in alunos:
print(f"Nome: {nome}")
print(f"Idade: {alunos[nome]['idade']}")
print(f"Turma: {alunos[nome]['turma']}")
else:
print("Aluno não encontrado.")
 
elif opcao == "3":
if len(alunos) == 0:
print("Nenhum aluno cadastrado.")
else:
for nome, dados in alunos.items():
print("\n------------------")
print(f"Nome: {nome}")
print(f"Idade: {dados['idade']}")
print(f"Turma: {dados['turma']}")
 
elif opcao == "4":
print("Sistema encerrado.")
break
 
else:
print("Opção inválida.")
