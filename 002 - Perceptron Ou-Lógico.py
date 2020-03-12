#!/usr/bin/env python3
# exercício: implementar o Ou-lógico

def passo(v):
  return 1 if v >= 0 else 0

def main():
  print(' '+ '='*13)
  print(' | Ou-lógico |')
  print(' '+ '='*13)
  # por conveniência, o dataset será armazenado nesta classe, em redes reais isso não ocorre
  dataset = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [-1, -1],
    [2, 3],
    [0.1, 0.2],
    [0.9, 1.2],
  ]
  for instancia in dataset:
    x1 = instancia[0]
    x2 = instancia[1]
    v = x1 + x2 - 0.5
    y = passo(v)

    # msg = "f(" + str(x1) + ", " + str(x2) + ") = " + str(y)
    msg = "f({}, {}) = {}".format(x1, x2, y)
    print(msg)

main()