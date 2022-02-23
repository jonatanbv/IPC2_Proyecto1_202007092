from tkinter import filedialog
from xml.dom import minidom
from piso import Piso


##############################################################
def abrir():
    ruta = filedialog.askopenfilename(title='abrir', filetypes=(('archivos xml', '*.xml'), ('archivos txt', '*.txt')))

    xml = minidom.parse(ruta) # convertimos el xml en objeto

    R = xml.getElementsByTagName('R') # obtenemos los elementos de la etiqueta R

    C = xml.getElementsByTagName('C') # obtenemos los elementos de la etiqueta C

    F = xml.getElementsByTagName('F') # obtenemos los elementos de la etiqueta F

    S = xml.getElementsByTagName('S') # obtenemos los elementos de la etiqueta S

    codigo = xml.getElementsByTagName('patron') # obtenemos los elementos de la etiqueta patron 

    row = []
    colum = []
    flip = []
    swap = []
    patron= []
    piso = []
    ############################################################

    for r in R:
        s = int(r.firstChild.data)
        row.append(s)

    for c in C:
        s = int(c.firstChild.data)
        colum.append(s)

    for f in F:
        s = int(f.firstChild.data)
        flip.append(s)
        
    for s in S:
        n = int(s.firstChild.data)
        swap.append(n)

    for pat in codigo:
        patron.append(pat.firstChild.data)

    for i in range(len(row)):
        piso.append(Piso(row[i], colum[i], flip[i], swap[i], patron[i+i], patron[i+i+1]))


    for pi in piso:
        print('\nRow: ', pi.R)
        print('Column: ', pi.C)
        print('Flip: ', pi.F)
        print('Swap: ', pi.S)
        print('patron Inicial: ', pi.patronIn)
        print('Patron Final: ', pi.patronFin)

    return piso
#################################################################

def menu():
    while True:
        print('''
    ---- Menú ----
    1. Cargar Archivo xml
    2. Salir
    ---- ---- ----
            ''')

        opt = input('Ingresa una opción: ')
        if opt == '1':
            print('Se cargo el archivo Correctamente')
            abrir()
        elif opt == '2':
            print('Saliendo...')
            break
        else:
            print('proyecto en proceso')

menu()

