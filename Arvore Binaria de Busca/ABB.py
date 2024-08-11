class No:
  def __init__ (self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

def altura (raiz):
  if raiz is None: return - 1
  resultado = max ( altura (raiz.esquerda), altura (raiz.direita)) + 1
  return resultado

def fator_de_balaceamento (node):
  if node is None: return 0
  return altura(node.esquerda) - altura(node.direita)

def em_ordem_fator_de_balaceamento(raiz):
  if raiz is None: 
    return
    
  em_ordem_fator_de_balaceamento(raiz.esquerda)
  print(f"Valor: {raiz.valor}, Fator de Balanceamento: {fator_de_balaceamento(raiz)}")
  em_ordem_fator_de_balaceamento(raiz.direita)

def pre_ordem(raiz):
  if raiz is None: return
  print(raiz.valor)
  pre_ordem(raiz.esquerda)
  pre_ordem(raiz.direita)

def pos_ordem(raiz):
  if raiz is None: return
  pos_ordem(raiz.esquerda)
  pos_ordem(raiz.direita)
  print(raiz.valor)

def em_ordem(raiz):
  if raiz is None: return
  em_ordem(raiz.esquerda)
  print(raiz.valor)
  em_ordem(raiz.direita)

def adicionar_no (raiz, valor):
  if (valor < raiz.valor):
    if (raiz.esquerda is None):
      raiz.esquerda = No(valor)
    else:
       adicionar_no(raiz.esquerda, valor)

  if (valor > raiz.valor):
    if (raiz.direita is None):
      raiz.direita = No(valor)
    else:
      adicionar_no(raiz.direita, valor)

raiz = No(20)
adicionar_no (raiz, 10)
adicionar_no (raiz, 30)
adicionar_no(raiz, 45)
adicionar_no(raiz, 15)

em_ordem_fator_de_balaceamento(raiz)