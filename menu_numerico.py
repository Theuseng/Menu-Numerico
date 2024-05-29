#!/usr/bin/python
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Name: Menu numérico
# version: 1.0.0
# Developer: Theuseng
# Created: 19/03/2021
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os
import sys
import time
from time import sleep as timeout

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()

print()
print(" ███╗   ███╗███████╗███╗   ██╗██╗   ██╗     ██╗  ██╗ ")
print(" ████╗ ████║██╔════╝████╗  ██║██║   ██║     ╚██╗██╔╝ ")
print(" ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║█████╗╚███╔╝  ")
print(" ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║╚════╝██╔██╗  ")
print(" ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝     ██╔╝ ██╗ ")
print(" ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝      ╚═╝  ╚═╝ ")
print("Create By : Theuseng")
print()
print("           [1]> 1 - Escolha             ")
print("           [2]> 2 - Escolha              ")
print("           [3]> 3 - Escolha         ")
print("           [4]> 4 - Escolha    ")
print()
print(" [0]> Exit ")
print()
A = input("Option ==>> ")

if A == "1" or A == "01":
    print("1 - Escolha")

elif A == "2" or A == "02":
    print("2 - Escolha")  #

elif A == "3" or A == "03":
    print("3 - Escolha")

elif A == "4" or A == "04":
    print("4 - Escolha")

elif A == "0" or A == "00":
    sys.exit()

else:
    print("\nERROR: Wrong Input")
    timeout(3)
    restart_program()
