import os
from class_Vendedor_POO_20 import*

nome = input("Digite seu nome: ")
vendas = int(input("Digite a quantidade de vendas: "))

os.system("cls")
os.system("pause")

pessoa = Vendedor(nome, vendas)
pessoa.vendeu(vendas)
pessoa.bateu_meta(100)