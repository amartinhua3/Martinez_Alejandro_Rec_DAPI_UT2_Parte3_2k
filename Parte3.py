def calculate_grade(Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud):
    '''Esta función calcula la recibe la nota final con una formula y devuelve un booleano de True si ha aprobado o False si ha suspendido
        Parametros:
            Entrada: como parametros de entrada tenemos las totas de cada apartado
            Practica01, Practica02, Practica03, Examen, Recuperacion, Actitud

            Salida: como parametros de salida tenemos la nota final con una True si ha aprobado o False si ha suspendido'''
    NotaFinal = (Practica01 + Practica02 + Practica03)/3 * 0.3 + max(Examen, Recuperacion)* 0.6 + Actitud * 0.1
    if NotaFinal >= 5:
        print(NotaFinal, True)
    else:
        print(NotaFinal, False)
calculate_grade(1.9, 6.2, 2.8, 2.2, 2.4, 8.3)