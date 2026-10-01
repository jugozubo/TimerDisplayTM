# main.py -- put your code here!
from machine import Pin, Timer, TouchPad
from time import sleep
import tm1637

TeclaTouch=TouchPad(Pin(15))
tim=Timer(0)
tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))

def llamado(t):
    global contador
    contador += 1
    tm.number(contador)

contador = 0
toco = 0

while True:
    valor=TeclaTouch.read()
    if valor<400:
        toco=not toco
        sleep(0.5)
        if toco:
            tim.init(period=1000, mode=Timer.PERIODIC, callback=llamado)
            print("Timer activado")    
        else:
            tim.deinit()
            print("Timer desactivado")
            tm.number(contador)


    