import random
import collections
#Valores de los palos
PALOS = ['espada', 'corazon', 'rombo', 'trebol']
#Valores de las cartas
VALORES = ['1', '2', '3' ,'4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#Array de escalera real
ESCALERA_REAL=['1','10', 'J', 'Q', 'K']

#Main Function
def main(tamano_mano, intentos):
    #Crear la baraja
    baraja = crear_baraja()
    #Crear array para guardar las manos que salgan
    manos = []
    #Obenter mano
    for _ in range(intentos):
        mano = obtener_mano(baraja, tamano_mano)
        manos.append(mano)
    #Calular probabilidades
    calc_prob(manos, intentos)

#Creacion de la baraja con PALOS y VALORES
def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    return barajas

#Obtener mano
def obtener_mano(baraja, tamano_mano):
    #Random sample -> obtener valores sin repeticion
    mano = random.sample(baraja, tamano_mano)
    return mano

#Calcular probabilidades de manos de Poker
def calc_prob(manos, intentos):
    
    ##########Combinaciones en el poker(Mano de Cinco)#########
    escalera_real = 0           #[10, J, Q, K], todos del mismo palo. 
    escalera_de_colores = 0     #Cinco cartas del mismo palo en orden.
    poker = 0                   #Cuatro cartas del mismo valor en mano.
    full = 0                    #Un Trio y un doble de diferentes valores
    color = 0                   #Cinco cartas del mismo palo.
    escalera = 0                #Cinco cartas consecutivas.
    trio = 0                    #Tres cartas del mismo valor en mano.
    par = 0                     #Dos cartas del mismo valor


    for mano in manos:
        mismo_palo = True
        valores = []
        palo = []
        for carta in mano:
            #Dividir la mano en valores y palos
            valores.append(carta[1])
            palo.append(carta[0])
            ##Comprobar si pertenencen a un mismo palo
            if carta[0] == mano[0][0]:
                pass
            else:
                mismo_palo = False

        #Ordenar valores ascendentes
        mano_ordenada = []
        for posicion in VALORES:
            for valor in valores:
                if posicion == valor:
                    mano_ordenada.append(posicion)
                else:
                    pass

        #Obtener el valor de inicio de la escalera
        start = -1
        for valor in mano_ordenada:
            if start == -1:
                for i in range(len(VALORES)):
                    if valor == VALORES[i]:
                        start = i
                        break
            else:
                break
        
        #Verificar si son valores concecutivos de la mano
        valores_concecutivos=0
        concecutivo = True
        i=0
        for valor in mano_ordenada:    
            if concecutivo == True:
                for posicion in VALORES[start+i:]:
                    if valor == posicion:
                        valores_concecutivos+=1
                        i+=1
                        break
                    else:
                        concecutivo=False
                        break
            else:
                break

        ##Conteo de combinaciones##
        if mismo_palo == True:
            #ESCALERA REAL
            if mano_ordenada == ESCALERA_REAL:
                escalera_real+=1
            #ESCALERA DE COLORES
            elif valores_concecutivos == 5:
                escalera_de_colores+=1
            #COLOR
            else:
                color+=1
        else:
            #ESCALERA
            if valores_concecutivos == 5:
                escalera+=1

        #Contar cartas del mismo valor
        counter = dict(collections.Counter(valores))
        #Verificar el full
        full_trio = False
        full_par = False
        #Contar las cartas
        for val in counter.values():
            #POKER
            if val == 4:
                poker += 1
                break
            #TRIO            
            if val == 3:
                trio += 1
                full_trio = True
            #PAR
            if val == 2:
                par += 1
                full_par = True
        #FULL
        if full_trio and full_par:
            full+=1           
        ##Conteo de combinaciones##

    # RESULTADOS
    get_escalera_real = "{:.5f}".format((escalera_real/intentos) * 100)
    get_escalera_de_colores = "{:.4f}".format((escalera_de_colores/intentos) * 100)
    get_poker = "{:.2f}".format((poker/intentos) * 100)
    get_full = "{:.2f}".format((full/intentos) * 100)
    get_color = "{:.2f}".format((color/intentos) * 100)
    get_escalera = "{:.2f}".format((escalera/intentos) * 100)
    get_trio = "{:.2f}".format((trio/intentos) * 100)
    get_par = "{:.2f}".format((par/intentos) * 100)
    print(f'Intentos: {intentos}')
    print(f'Probabilidad de escalera_real: {get_escalera_real}%')
    print(f'Probabilidad de escalera_de_colores: {get_escalera_de_colores}%')
    print(f'Probabilidad de poker: {get_poker}%')
    print(f'Probabilidad de full: {get_full}%')
    print(f'Probabilidad de color: {get_color}%')
    print(f'Probabilidad de escalera: {get_escalera}%')
    print(f'Probabilidad de trio: {get_trio}%')
    print(f'Probabilidad de par: {get_par}%')


if __name__ == '__main__':
    #Tamaño de mano
    tamano_mano = 5
    #Veces que se corre la simulacion
    intentos = 10000000
    #Llamar main
    main(tamano_mano, intentos)
