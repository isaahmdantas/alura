class ContaSalario:
  def __init__(self, codigo, saldo):
    self._codigo = codigo
    self._saldo = saldo

  def __eq__(self, value):
    if type(value) != ContaSalario:
      return False
    
    return self._codigo == value._codigo and self._saldo == value._saldo

  def deposita(self, valor):
    self._saldo += valor 

  def __str__(self):
    return "[>>Codigo {} Saldo {} <<<]".format(self._codigo, self._saldo)
  

conta1 = ContaSalario("123-4", 1000)
conta1.deposita(200)
print(conta1)

conta2 = ContaSalario("123-4", 85)
print(conta2)

print(conta1 == conta2)

print(isinstance(conta1, ContaSalario))

idades = [15,87,37,45,56,32,49,37]
for i in range(len(idades)):
    print(i,idades[i])

print(sorted(idades))
print(sorted(idades, reverse=True))
print(list(reversed(idades)))
idades.sort()
print(idades)
