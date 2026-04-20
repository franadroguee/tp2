import random, time
from termcolor import colored

lista = list('!@#$%^&*()_+-=<>?/')
string = 'ERROR'

while True:
    print(colored(string, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))), end = ' ')
    string += random.choice(lista)
    if len(string) > 80:
        string = 'ERROR'
    time.sleep(0.01)