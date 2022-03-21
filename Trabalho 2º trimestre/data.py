class Data():
    def __init__(self, data) -> None:
        
        dia, mes, ano = int(data[:2]), int(data[3:5]), int(data[6:])
        
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Calendario():

    
    def passar_dia(data):
        #declaro a quantidade de dias de cada mes para verificação futura
        meses_30 = [4,6,9,11]
        meses_31 = [1,3,5,7,8,10,12]

        def passar_mes(data):
            data.mes += 1
            data.dia = 1

        data.dia += 1

        if data.mes in meses_30 and data.dia>30:
            passar_mes(data)
        elif data.mes in meses_31 and data.dia>31:
            passar_mes(data)
        elif data.mes == 2:
            if (data.ano%4 ==0 and data.ano%100 == 0) or (data.ano%400):
                if data.dia>29:
                    passar_mes(data)
            else:
                if data.dia>28:
                    passar_mes(data)

        
        if data.mes>12:
            data.mes = 1
            data.ano +=1
        

    def verificar_data(data):
        meses_30 = [4,6,9,11]
        meses_31 = [1,3,5,7,8,10,12]

        if data.mes in meses_30 and data.dia<31 and data.ano >= 2021:
            return True
        elif data.mes in meses_31 and data.dia<32 and data.ano >= 2021:
            return True
        elif data.mes == 2:
            if (data.ano%4 ==0 and data.ano%100 == 0) or (data.ano%400):
                if data.dia<29:
                    return True
            else:
                if data.dia<28:
                    return True
        else:
            return False


    def retornar_data(data):
        if data.mes < 10:
            data.mes = "0" + str(data.mes)
        
        if data.dia < 10:
            data.dia = "0" + str(data.dia)
        
        return str(data.dia) + "/" + str(data.mes) + "/" + str(data.ano)
        
