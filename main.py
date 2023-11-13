class Empregado:
    aumento = 1.04

    def __init__(self, nome, ordenado):
        self.nome = nome
        self.ordenado = ordenado

    def get_nome(self):
        return self.nome

    def set_aumento(self):
        self.ordenado *= self.aumento #incrementa o ordenado em 4%

    def get_ordenado(self):
        return self.ordenado

class Programador(Empregado):
    aumento = 1.2

    def __init__(self, nome, ordenado, linguagem):
        super().__init__(nome, ordenado)
        self.linguagem = linguagem

    def get_linguagem(self):
        return self.linguagem

class Gerente(Empregado):
    aumento = 1.5

    def __init__(self, nome, ordenado, empregados=None):
        super().__init__(nome, ordenado)
        # Empregado.__init__(nome, ordenado)
        if empregados == None: #comparação
            self.empregados = []
        else:
            self.empregados = empregados

    def adicionar_empregado(self, empregado):
        if empregado not in self.empregados:
            self.empregados.append(empregado)

    def remover_empregado(self, empregado):
        if empregado in self.empregados:
            self.empregados.remove(empregado)

    def listar_empregados(self):
        for empregado in self.empregados:
            print(empregado.get_nome())

    def devolver_empregados(self):
        return self.empregados

class Contabilista(Empregado):
    aumento = 1.1

    def __init__(self, nome, ordenado, TOCouROC):
        super().__init__(nome, ordenado)
        self.TOCouROC = TOCouROC

    def get_TOCouROC(self):
        return self.TOCouROC

#---------------------------------------------------------------------#
emp = Empregado('António', 710)
print(emp.get_ordenado())
emp.set_aumento()
print(emp.get_ordenado())

print("-"*25)

prog1 = Programador("José Policarpo", 950, 'Python')
print(prog1.get_ordenado())
prog1.set_aumento()
print(prog1.get_ordenado())

prog2 = Programador("Mariana", 800, 'C++')

print("="*25)

ger = Gerente('Cristina', 1000, [prog1])
print(ger.get_ordenado())
print(ger.get_nome())

ger.adicionar_empregado(prog2)
ger.listar_empregados()

empregados = ger.devolver_empregados()
for empregado in empregados:
    print(empregado.get_nome(), empregado.get_ordenado())

print(ger.get_ordenado())
ger.set_aumento()
print(ger.get_ordenado())

print("-"*25)

cont1 = Contabilista("Maria Andrioleta", 900, 'TOC')
print(cont1.get_nome(), cont1.get_ordenado(), cont1.get_TOCouROC())
cont1.set_aumento()
print(cont1.get_ordenado())