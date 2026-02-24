dia_da_semana = 0

match dia_da_semana:
    case 1 | 2 | 3 | 4 | 5:
        print("É dia de semana")
    case 6 | 7:
        print("É fim de semana")
    case _:
        print("Dia inválido")  