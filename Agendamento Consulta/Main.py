from Model import PacienteModel, HistoricoModel, ConsultaModel
from View import PacienteView, HistoricoView, ConsultaView
from Controller import PacienteController, HistoricoController, ConsultaController
from datetime import datetime

class Main:

    pacientemodel = PacienteModel()
    pacienteview = PacienteView()
    pacientecontroller = PacienteController(pacienteview, pacientemodel)

    historicomodel = HistoricoModel()
    historicoview = HistoricoView()
    historicocontroller = HistoricoController(historicoview, historicomodel)

    consultamodel = ConsultaModel()
    consultaview = ConsultaView()
    consultacontroller = ConsultaController(consultaview, consultamodel)

    print("Opção 1: Inserir paciente")
    print("Opção 2: Listar todos os pacientes")
    print("Opção 3: Listar paciente pelo código do paciente")
    print("Opção 4: Excluir paciente")
    print()
    print("Opção 5: Inserir histórico")
    print("Opção 6: Listar todos os históricos")
    print("Opção 7: Listar histórico pelo código do histórico")
    print("Opção 8: Excluir histórico")
    print()
    print("Opção 9: Inserir consulta")
    print("Opção 10: Listar todas as consultas")
    print("Opção 11: Listar consulta pelo código da consulta")
    print("Opção 12: Excluir consulta")
    print("Opção 13: Calcular desconto referente ao plano de saúde")
    print()
    print("Opção 14: Sair")
    print()

    while True:

        opcao = int(input("Informe a opção desejada: "))

        match opcao:
            case 1:
                pacientecontroller.controllerAdquirirDados()
                pacientecontroller.controllerInserir()
            case 2:
                pacientecontroller.controllerListarTodos()
            case 3:
                codigo = str(input("Informe o código de busca: "))
                pacientecontroller.controllerListarId(codigo)
            case 4:
                codigo = str(input("Informe o código de busca: "))
                pacientecontroller.controllerExcluir(codigo)
            case 5:
                historicocontroller.controllerAdquirirDados()
                historicocontroller.controllerInserir()
            case 6:
                historicocontroller.controllerListarTodos()
            case 7:
                codigo = str(input("Informe o código de busca: "))
                historicocontroller.controllerListarId(codigo)
            case 8:
                codigo = str(input("Informe o código de busca: "))
                historicocontroller.controllerExcluir(codigo)
            case 9:
                consultacontroller.controllerAdquirirDados()
                consultacontroller.controllerInserir()
            case 10:
                consultacontroller.controllerListarTodos()
            case 11:
                codigo = str(input("Informe o código de busca: "))
                consultacontroller.controllerListarId(codigo)
            case 12:
                codigo = str(input("Informe o código de busca: "))
                consultacontroller.controllerExcluir(codigo)
            case 13:
                codigo = str(input("Informe o código de busca: "))
                consultacontroller.controllerPlanoSaude(codigo)
            case 14:
                break