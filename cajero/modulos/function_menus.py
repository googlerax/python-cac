"""
modulo con funciones principales y menu
"""
# funcion que calcula ganancia plazo fijo en pesos
def menu_plazoP(monto, dias):
    ganan = (dias * 92.47)/30
    return round(monto + ganan, 2)

# funcion que calcula ganancia plazo fijo en dólares
def menu_plazoD(monto, dias):
    ganan = (dias * 0.04) / 30
    return round(monto + ganan, 2)

# funcion que calcula el valor maximo con funcion max() entre el saldo y la extraccion de dinero, si retorna 0, significa que se excede al saldo.
def extraer(saldo, monto):
    return max(saldo-monto, 0)

# menu principal
def menu(saldo, dolar):
    # arrays donde se guardan los cambios (extraccion,deposito,venta etc)
    list_ingreso = []
    list_extrac = []
    list_trans = []
    list_compra = []
    list_venta = []
    list_plazo_peso = []
    list_plazo_dolar = []
    while True:
        print("")
        print("----------MENU PRINCIPAL-----------------")
        print("Seleciona una opcion: ")
        print("#########################################")
        print("     #1  consultar saldo")
        print("     #2  depositar dinero")
        print("     #3  extraer dinero")
        print("     #4  transferir dinero")
        print("     #5  comprar dolares")
        print("     #6  vender dolares")
        print("     #7  crear plazo fijo")
        print("     #8  ver ultimos movimientos")
        print("     #9  salir de la cuenta")
        print("#########################################")
        while True:
            try:
                opcion = int(input("Ingresa tu opcion:\n "))
                break
            except ValueError:
                print("Error, debe ingresar un numero entero: ")
                print("")
        #a partir de python 3.10 se implementa el condicional switch llamado 'match.
        match opcion:
            # consultar saldo
            case 1:
                print("")
                print(f"Tu saldo actual en pesos es de: ${saldo}")
                print(f"Tu saldo actual en dolares es de: uS${dolar}")
                print("")
            # depositar dinero
            case 2:
                while True:
                    try:
                        print("#########################################")
                        ingreso = float(input("Digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
                        print("#########################################")
                        break
                    except ValueError:
                        print("Error, debe ingresar un dato numerico: ")
                saldo += ingreso
                print("--Gracias por ingresar su dinero, su saldo actual es de: $", saldo, "--")
                list_ingreso.append(ingreso)
            # extraer dinero
            case 3:
                while True:
                    while True:
                        try:
                            extraccion = float(input("Ingresa el monto a extraer: "))
                            break
                        except ValueError:
                            print("Error, debe ingresar un numero entero:")
                    if extraer(saldo, extraccion) == 0:
                        print(f"Monto excedido al saldo, su saldo es de ${saldo}")
                    else:
                        break
                saldo -= extraccion
                print("Gracias por extraer, tu saldo restante es: $", saldo)
                list_extrac.append(extraccion)
            # transferir dinero
            case 4:
                tranferir = (input("Ingrese el Alias/CBU de la cuenta a la cual deseas tranferir: "))
                while True:
                    while True:
                        try:
                            monto1 = float(input("Ingresa el monto a tranferir: "))
                            print("#########################################################")
                            print("#########################################################")
                            break
                        except ValueError:
                            print("Error, debe ingresar un numero entero: ")
                    if extraer(saldo, monto1) == 0:
                        print(
                            f"Monto excedido al saldo, su saldo es de ${saldo}")
                    else:
                        break
                confirmar = (input(
                    f"Estas por realizar una transferencia al numero de cuenta {tranferir} con el siguiente monto: {monto1} estas seguro que deseas realizar esta accion ? ingresa: \n # si para confirmar la transferencia. \n # no para cancelar: \n "))
                if confirmar == "si":
                    saldo -= monto1
                    print(
                        "Gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $", saldo)
                elif confirmar == "no":
                    print("Transferencia cancelada ")
                else:
                    print("Has ingresado un valor invalido ")
                list_trans.append(monto1)
            # compra de dolares
            case 5:
                print("#####################################")
                print("    El precio del dolar para la compra es de $164,5")
                print(f"   Tu saldo en dolares es el siguiente: u$S{dolar}")
                print(f"    Tu saldo en pesos es de ${saldo}")
                print("#####################################")
                while True:
                    while True:
                        try:
                            compraDolar = float(input("Ingresa el monto de dolares a comprar: "))
                            break
                        except ValueError:
                            print("Error, debe ingresar un numero entero: ")
                    conversiond = compraDolar * 164.5
                    print("#####################################")
                    if extraer(saldo, conversiond) == 0:
                        print(
                            f"Monto excedido al saldo, su saldo es de ${saldo}")
                    else:
                        break
                confirma = (input(f"¿estas seguro de comprar : u$s {compraDolar} dolares ? ingresa \n #si para confirmar. \n #no para cancelar ")).lower()
                print("#####################################")
                if confirma == "si":
                    conversiond = compraDolar * 164.5
                    saldo -= conversiond
                    dolar += compraDolar
                    print("#####################################################")
                    print("Tu saldo en tu cuenta pesos es de: $", saldo)
                    print("Tu saldo en tu cuenta dolares es de: u$s", dolar)
                    print("#####################################################")
                elif confirma == "no":
                    print("Has cancelado tu compra")
                else:
                    print("Has ingresado un valor invalido ingresa 'si' o 'no' ")
                list_compra.append(compraDolar)
                # venta de dolares
            case 6:
                print("#####################################")
                print("    El precio del dolar para la venta de $170")
                print("    tu saldo en dolares es de: ", dolar)
                print("#####################################")
                while True:
                    while True:
                        try:
                            venderDolar = float(input("Ingresa el monto de dolares a vender: "))
                            break
                        except ValueError: print("Error, debe ingresar un numero entero")
                    if extraer(dolar, venderDolar) == 0:
                        print(f"Monto excedido al saldo, su saldo es de ${saldo}")
                    else:
                        break
                confirma = (input(f"¿estas seguro de vender u$s{venderDolar}? ingresa \n #si para confirmar. \n #no para cancelar ")).lower()
                print("##############################################")
                if confirma == "si":
                    conversionp = venderDolar * 170
                    saldo += conversionp
                    dolar -= venderDolar
                    print("#####################################################")
                    print("tu saldo en tu cuenta pesos es de: $", round(saldo,2))
                    print("tu saldo en tu cuenta dolares es de: u$s", round(dolar,2))
                    print("#####################################################")
                elif confirma == "no":
                    print("has cancelado tu compra")
                else:
                    print("Has ingresado un valor invalido ingresa 'si' o 'no' ")
                list_venta.append(venderDolar)
                # plazo fijos:
            case 7:
                print("#####################################################")
                print("tu saldo en tu cuenta pesos es de: $", saldo)
                print("tu saldo en tu cuenta dolares es de: u$s", dolar)
                while True:
                    try:
                        op = int(input("Para plazo fijo en Pesos ingrese 1:\n Para plazo Fijo en dolares ingrese 2: "))
                        print("#####################################################")
                        break
                    except ValueError: print("Error, debe ingresar un numero entero")
                match op:
                    # plazo fijo funciona. hay que consultar saldo antes de hacerlo sino bucle infinito.
                    # plazo fijo en pesos
                    case 1:
                        while True:
                            while True:
                                try:
                                    monto = float(input("Ingrese el monto a invertir (minimo de $1500): "))
                                    break
                                except ValueError:print("Error, debe ingresar un numero entero")
                            if monto < 1500 or extraer(saldo, monto) == 0:
                                print("monto debe ser mayor a $1500 o monto excedido para la operacion")
                            else:
                                break
                        while True:
                            while True:
                                try:
                                    dias = int(input("Ingrese el plazo (minimo 30 dias): "))
                                    break
                                except ValueError:print("Error, debe ingresar un numero entero")
                            if dias < 30:
                                print("El plazo debe ser mayor a 30 dias: ")
                            else:
                                break
                        plazo_en_pesos = menu_plazoP(monto, dias)
                        confir = input((f"Generará una ganancia de ${plazo_en_pesos} ¿Confirmar?  SI o NO\n")).upper()
                        if confir == "SI":
                            saldo -= monto
                            print(f"Transacción exitosa saldo actual {round(saldo,2)}")
                        elif confir == "NO":
                            print("Plazo Fijo Cancelado.")
                        else:
                            print(f"Opcion no valida")
                        list_plazo_peso.append(monto)
                        # plazo fijo en dolares
                    case 2:
                        while True:
                            while True:
                                try:
                                    monto2 = float(input("Ingrese el monto a invertir (minimo de u$s100): "))
                                    break
                                except ValueError:print("Error, debe ingresar un numero entero")   
                            if monto2 < 100 or extraer(dolar, monto2) == 0:
                                print(
                                    "monto debe ser mayor a u$s100 o monto excedido para la operacion: ")
                            else:
                                break
                        while True:
                            while True:
                                try:
                                    dias2 = int(input("Ingrese el plazo (minimo 30 dias): "))
                                    break
                                except ValueError:print("Error, debe ingresar un numero entero")
                            if dias2 < 30:
                                print("El plazo debe ser mayor a 30 dias: ")
                            else:
                                break
                        plazo_en_dolares = menu_plazoD(monto2, dias2)
                        confirm = input(
                            (f"Generará una ganancia de ${plazo_en_dolares} ¿Confirmar?  SI o NO\n")).upper()
                        if confirm == "SI":
                            dolar -= monto2
                            print(
                                f"Transacción exitosa saldo actual u$S{round(dolar,2)}")
                        elif confirm == "NO":
                            print("Plazo Fijo Cancelado.")
                        else:
                            print(f"Opcion no valida.")
                        list_plazo_dolar.append(monto2)
                    case other:
                        print("Opcion invalida: 1-plazo fijo en peso 2-plazo fijo en dolares")
            # consultar ultimos movimientos
            case 8:
                for i in list_ingreso:
                    print(f"Se deposito ${i}")

                for i in list_extrac:
                    print(f"Se extrajo ${i}")

                for i in list_trans:
                    print(f"Se transfirio ${i}")

                for i in list_compra:
                    print(f"Se compro u$${i}")

                for i in list_venta:
                    print(f"Se vendio u$${i}")

                for i in list_plazo_peso:
                    print(f"Se realizo plazo fijo de ${i}")

                for i in list_plazo_dolar:
                    print(f"Se realizo plazo fijo de u$${i}")
            case 9:
                print("Saliendo al menu de bienvenida.")
                print("")
                break
            case other:
                print("Opcion ingresada no valida, vuelva a intentarlo: ")


###### funcion que valida el usuario######
def usuario():
    print("----------has seleccionado el idioma español----------")
    print("")
    nombre = str(input("ingresa tu nombre: ")).upper()
    while True:
        # uso de try y except para capturar error de tipo
        try:
            clave = int(input("ingresa tu clave para acceder a tu cuenta: La clave es 1234: "))
            if clave == 1234:
                print("")
                print("#########################################")
                print(f"Bienvenido/a a tu cuenta {nombre} !!")
                print("#########################################")
                break
            else:
                print("")
                print("Incorrecto: Recorda que la clave es 1234: ")
                print("")
        except ValueError:
            print("")
            print(f"Error,no es un entero: ")
            print("")


#### funcion menu bienvenida ######
def menu_bienvenida(saldo, dolar):
    while True:
        try:
            print("----------Hola Bienvenido al cajero de codo a codo----------")
            print("")
            idioma = int(input("Seleccione el idioma: \n 1 Español: \n 2 Ingles: \n 3 Portugues: \n 4 Salir: "))
            print("")
            match idioma:
                case 1:
                    usuario()
                    menu(saldo, dolar)
                    continue
                case 2:
                    print("")
                    print("pronto Disponible")
                    print("")
                    continue
                case 3:
                    print("")
                    print("pronto Disponible")
                    print("")
                    continue
                case 4:
                    print("")
                    print("Saliendo..")
                    print("")
                    break
            if idioma > 4:
                print("")
                print("Numero invalido: ")
                print("")
        except ValueError:
            print("")
            print("Error, debe ingresar un numero entero: ")
            print("")

