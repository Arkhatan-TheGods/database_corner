import CRUDS_QUERYS.query_medical_history as history_query


# insere valores no medical history

def insert_medical_history():

    id_paciente = int(input('informe o id do paciente: ')).strip()

    doenca = input('informe a doença(s): ')

    alergia = input('informe a(s) alergia(a): ')

    medicacao = input('informe os medicamentos: ')


# vish já me perco um pouco com python ksksk, imagina shell
