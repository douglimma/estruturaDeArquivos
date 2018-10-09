# -*- coding: utf-8 -*-
'''
Created on 03 de out de 2018
@author: Douglas Lima Viana
'''
import struct
import sys
import os
from random import randint

filename = "cep_ordenado.dat"
f = open (filename, "r") 
regCep = struct.Struct("72s72s72s72s2s8s2s")
cepCol = 5
tam = os.path.getsize("cep_ordenado.dat") / regCep.size
print ("Quantidade de linhas: %d" % tam) 

contLinhas = 0
qtdLinhas = 20
fout1 = open ("cep1.txt", "wb")
fout2 = open ("cep2.txt", "wb")
line = f.readline()
while contLinhas < qtdLinhas:

    rand = randint(0,1)
    
    line = f.readline()
    if (rand == 1):
        
        fout1.write(line)
           
    else:
        
        fout2.write(line)
        
    contLinhas += 1

fout1.close();
fout2.close();

def cmp (ta, tb):
    if ta[cepCol] == tb[cepCol]: return 0
    if ta[cepCol] > tb[cepCol]: return 1    
    return -1


resultado = open ("result.txt", "wb")
tamA = os.path.getsize("cep1.txt")/regCep.size
tamB = os.path.getsize("cep2.txt")/regCep.size

conta = 0
contb = 0

a = open("cep1.txt", "rb")
b = open("cep2.txt", "rb")

lineA = regCep.unpack(a.readline(regCep.size))
lineB = regCep.unpack(b.readline(regCep.size))
while (conta < tamA and contb < tamB):
	if cmp(lineA, lineB) == 1:
		resultado.write(regCep.pack(*lineB))
		contb += 1
		if contb < tamB:
			lineB = regCep.unpack(b.readline(regCep.size))
	else:
		resultado.write(regCep.pack(*lineA))
		conta += 1
		if conta < tamA:
			lineA = regCep.unpack(a.readline(regCep.size))

while (conta < tamA):
	resultado.write(regCep.pack(*lineA))
	conta += 1
	if conta < tamA:
		lineA = regCep.unpack(a.readline(regCep.size))

while (contb < tamB):
	resultado.write(regCep.pack(*lineB))
	contb += 1
	if contb < tamB:
		lineB = regCep.unpack(b.readline(regCep.size))


f.close()
resultado.close()