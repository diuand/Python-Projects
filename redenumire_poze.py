import os

def parcurgere_fisiere(fisier):
    dictionar = {}
    for dir , folder ,file in os.walk(fisier):
        dictionar[dir] = file
    return dictionar

def change_pircure_names(fisier_actual):
    dictionar = parcurgere_fisiere(fisier_actual)
    extensie = ['.png','.jpeg']
    nume_fisier = input('scrie numele fisierului pe care il cauti: ')
    if nume_fisier in extensie:
        rename = input('redenumeste fisierele: ')
    for k,v in dictionar.items():
        if nume_fisier in v:
            print(nume_fisier ,' ----> ' ,v)
        else:
            ct = 0
            for fisier in v :
                if nume_fisier in fisier:
                    if nume_fisier in extensie:
                        old_file = k +'\\' +fisier
                        new_file = k +'\\' + rename + '_'+ str(ct) +'.png'
                        os.rename(old_file , new_file )
                        ct+=1
                    print(k, ' ----> ', fisier)

fisier_actual = os.getcwd()
change_pircure_names(fisier_actual)