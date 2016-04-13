"""Programa que lee el archivo cuadruplos.txt y traduce sus instrucciones"""
import turtle

f = open('cuadruplos.txt',r)
for line in f:
    s = f.readline();
    """String viene de la forma ('op', 'operando1', 'operando2','memoria')"""
    lista = s.split("\"",3)