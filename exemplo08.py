mes = 5
dia_da_semana = 4

match dia_da_semana:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("É dia de semana em Abril ")
    case 6 | 7 if mes == 5:
        print("É fim de semana no mês de Maio")
    case _:
        print("Sem correspondência")  