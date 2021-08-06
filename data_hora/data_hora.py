import datetime as dt


def datas():
    data = dt.datetime.now()
    data_br = data.strftime('%d/%m/%Y')
    return data_br


def horas():
    hora = dt.datetime.now()
    hora_br = hora.strftime('%H:%M:%S')
    return hora_br

