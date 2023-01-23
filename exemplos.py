print("Bem vindo ao Controle do Hospital")

pergunta = input(("""
1 - mostrar tabelas
2 - consultar registro na tabela
3 - atualizar registro
4 - deletar registro
5 - voltar ao menu
6 - sair
 """))

# question_ = '1'
match pergunta:
    case "1":
        print('foi')
