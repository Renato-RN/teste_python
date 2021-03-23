# arquivo app.py

import db
import mensagens as msg

def main():
    NOVA_TAREFA     = 1
    CONCLUIR_TAREFA = 2
    
    while True:
        msg.exibir_cabecalho()
        msg.exibir_tarefas()
        try:
            # exibe as op��es dispon�veis
            opcao = int(input("O que deseja fazer? 1 = Nova tarefa, 2 = Concluir tarefa => "))

            # verifica qual op��o o usu�rio escolheu
            if opcao == NOVA_TAREFA:
                msg.mostrar_opcao_nova_tarefa()
            elif opcao == CONCLUIR_TAREFA:
                msg.mostrar_opcao_concluir_tarefa()
            else:
                print ("Op��o n�o reconhecida, por favor informar um n�mero")    
        except ValueError as e :
            print ("Op��o n�o reconhecida, por favor informar um n�mero")
        except Exception:
            exit(0)

if __name__ == "__main__":
    db.criar_tabela_todo()

main()