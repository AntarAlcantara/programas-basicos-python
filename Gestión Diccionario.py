opc1 = 0  
while(opc1 !=3):  
    print("       DICCIONARIO ") 
    print("__________________________")
    print("  1.  Español / Ingles ") 
    print("__________________________")
    print("  2.  Ingles / Español ")
    print("__________________________")
    print("  3.     Para salir    ")
    print("__________________________")
    opc1 = int(input("Elige una opcion: ")) 


    if (opc1 == 1): 
 
 
        diccionario = {"trabajo":"job", "hola": "hello", "si": "yes", "manzana": "apple", "respuesta": "answer", "banco": "bank",
                       "flor": "flower", "comida": "food",
                       "silla": "chair", "ciudad": "city", "dia": "day", "diccionario": "dicctionary", "mama":"mom,",
                       "cuaderno":"notebook", "lapiz":"pencil", "numero":"number", "programa":"Program",
                       "redes":"networks", "musica":"music", "traductor":"translator", "palabra":"word", "caminar":"walk",
                       "celular":"mobile", "juego":"game", "comer":"eat", "galleta":"cookie", "escuela":"school",
                       "lentes":"glasses", "jugo":"juice", "mochila":"backpack", "maestro":"teacher"}
  
        print("                                          *Español/Ingles*                                             ") 
        print(" ______________________________________________________________________________________________________")
        print("| hola, si, manzana, respuesta, banco, flor, comida, silla, ciudad, dia, diccionario, mama, cuaderno  |")
        print("| lapiz, trabajo, numero, programa, redes, musica, traductor, palabra, caminar, celular, juego, comer |")
        print("| galleta, escuela, lentes, jugo, mochila, computadora, maestro                                       |")
        print(" ______________________________________________________________________________________________________")

        opc = input("                                Ingresa la palabra: ") 
        print("                                _________________________________")
        print("                                      {} : {}   ".format(opc, diccionario[opc]))     
        print("                                _________________________________")

    if (opc1 == 2): 

         
        diccionario = {"hello":"hola", "yes":"si", "apple":"manzana","answer":"respuesta","bank":"banco",
                       "flower":"flor","food":"comida",
                       "chair":"silla","city":"ciudad","day":"dia","dicctionary":"diccionario","mom":"mama",
                       "notebook":"cuaderno", "pencil":"lapiz", "job":"trabajo", "number":"numero", "program":"programa",
                       "networks":"redes", "music":"musica", "translator":"traductor", "word":"palabra", "walk":"caminar",
                       "mobile":"celular", "game":"juego", "eat":"comer","computer":"computadora", "teacher":"maestro", "cookie":"galleta", "school":"escuela",
                       "glasses":"lentes", "juice":"jugo", "backpack":"mochila",}

        
        print("                                             *Ingles/Español* ")
        print(" ______________________________________________________________________________________________________")
        print("| hello, yes, apple, answer, bank, flower, food, chair, city, day, dicctionary, mom, notebook, pencil |")
        print("| job, number, program, networks, music, translator, word, walk, mobile, game, eat, cookie, school,   |")
        print("| glasses, juice, backpack, computer, teacher                                                         |")
        print(" ______________________________________________________________________________________________________")

        opc = input("                                 Ingresa la palabra: ")  
        print("                                 __________________________________")
        print("                                        {} : {}   ".format(opc, diccionario[opc]))   
        print("                                 __________________________________")

print("Saliste")  
