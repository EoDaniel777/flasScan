#!/usr/bin/env python3
import nmap
import subprocess

scanner = nmap.PortScanner()

print("Seja Bem vindo ao Flash Sacan")
print(" -> ⒷⒺⓂ ⓋⒾⓃⒹⓄ ⒶⓄ ⒻⓁⒶⓈⒽ ⓈⒸⒶⓃ <- ")

ip = input("Digite o IP a ser scaneado: ")
print("o ip digitado foi: ", ip)
type(ip)

menu = input(""""\n Escolha o tipo de scan a ser realizado!
                1 -> Scan do tipo SYN
                2 -> Scan do tipo UDP (NECESSÁRIO ROOT)
                3 -> Scan do tipo Bruto
                Escolha o número correspondente a opção desejada: """)
print("A opção escolhida foi", menu)

if menu == "1":

    scanner.scan(ip)
    print(scanner.scaninfo())
    scanner.command_line()
    print("Status do IP:", scanner[ip].state())
    scanner[ip].all_protocols()
    print("")
    scanner[ip]['tcp'].keys()
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

elif menu == "2":

    scanner.scan(ip)
    command = 'nmap -sU'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output.decode('utf-8'))
    '#print(scanner.scaninfo())'
    '#print("Status do IP:", scanner[ip].state())'
    '#print(scanner[ip].all_protocols())'
    '#print("")'
    '#scanner[ip][''udp''].keys()'
    '#print("Portas Abertas: ", scanner[ip][''udp''].keys())'

elif menu == "3":

    scanner.scan(ip, '1-1024', '-v -sC')
    print("Status do IP:", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas Abertas: ", scanner[ip]['tcp'].keys())

else:
    print("Escolha uma opção válida!!!")
