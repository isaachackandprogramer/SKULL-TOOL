import os


print('''   #####   ###  ##  ##   ##  ####     ####              ######    #####    #####   ####
 ##   ##   ##  ##  ##   ##   ##       ##               # ## #   ##   ##  ##   ##   ##
 #         ## ##   ##   ##   ##       ##                 ##     ##   ##  ##   ##   ##
  #####    ####    ##   ##   ##       ##                 ##     ##   ##  ##   ##   ##
      ##   ## ##   ##   ##   ##   #   ##   #             ##     ##   ##  ##   ##   ##   #
 ##   ##   ##  ##  ##   ##   ##  ##   ##  ##             ##     ##   ##  ##   ##   ##  ##
  #####   ###  ##   #####   #######  #######            ####     #####    #####   #######
''')
print('por favor tenha as ferramentas instaladas e ative o modo administrador')
print('     by zaack')
print('')
print('''1-nmap''')
print("")

var1 = input('>')

if var1 == '1':
    print('')
    print('''1-alvo''')
    print('')
    ip = input(">")
    if ip == '1':
        print('')
        print('digite o seu alvo')
        print('')
        var3 = input(":")
        os.system('nmap {}'.format(var3))   
