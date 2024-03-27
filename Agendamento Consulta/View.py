from datetime import datetime

class PacienteView:

    def __init__(self):
        pass

    def viewAdquirirDados(self):
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        sexo = str(input("Sexo: "))
        telefone = str(input("Telefone: "))
        plano_saude = str(input("Plano de saúde: "))
        return nome, idade, sexo, telefone, plano_saude
    
    def viewMostrarDados(self, dados):
        for dado in dados:
            print(f"Nome: {dado.nome}")
            print(f"Idade: {dado.idade}")
            print(f"Sexo: {dado.sexo}")
            print(f"Telefone: {dado.telefone}")
            print(f"Plano de Saúde: {dado.plano_saude}")
    
    def viewMostrarDado(self, dado):
        print(f"Nome: {dado.nome}")
        print(f"Idade: {dado.idade}")
        print(f"Sexo: {dado.sexo}")
        print(f"Telefone: {dado.telefone}")
        print(f"Plano de Saúde: {dado.plano_saude}")

class HistoricoView:

    def __init__(self):
        pass

    def viewAdquirirDados(self):
        medicamentos = []
        historicos = []
        
        while True:
            medicamento = str(input("Medicamentos utilizados: "))
            if medicamento == "ok":
                break
            medicamentos.append(medicamento)
            
        while True:
            historico = str(input("Histórico de doenças: "))
            if historico == "ok":
                break
            historicos.append(historico)
            
        id_paciente = str(input("Código do paciente: "))
        return medicamentos, historicos, id_paciente
    
    def viewMostrarDados(self, dados):
        for dado in dados:
            print(f"Medicamentos: {dado.medicamento}")
            print(f"Historico de doenças: {dado.historico}")
            print(f"Paciente: {dado.paciente}")
    
    def viewMostrarDado(self, dado):
        print(f"Medicamentos: {dado.medicamento}")
        print(f"Historico de doenças: {dado.historico}")
        print(f"Paciente: {dado.paciente}")

class ConsultaView:

    def __init__(self):
        pass
    
    def viewAdquirirDados(self):
        
        dia = int(input("Dia: "))
        mes = int(input("Mês: "))
        ano = int(input("Ano: "))
        hora = int(input("Hora: "))
        minuto = int(input("Minuto: "))

        horario_consulta = datetime(ano, mes, dia, hora, minuto)
        horario_consulta = horario_consulta.strftime('%Y-%m-%d %H:%M')
        nome_medico = str(input("Nome do médico: "))
        valor_consulta = float(input("Valor da consulta: "))
        id_paciente = str(input("Código do paciente: "))
        return horario_consulta, nome_medico, valor_consulta, id_paciente
    
    def viewMostrarDados(self, dados):
        for dado in dados:
            print(f"Horário da consulta: {dado.horario}")
            print(f"Nome do Médico: {dado.nome_medico}")
            print(f"Valor da consulta: {dado.valor_consulta}")
            print(f"Paciente: {dado.paciente}")
    
    def viewMostrarDado(self, dado):
            print(f"Horário da consulta: {dado.horario}")
            print(f"Nome do Médico: {dado.nome_medico}")
            print(f"Valor da consulta: {dado.valor_consulta}")
            print(f"Paciente: {dado.paciente}")
    
    def viewPlanoSaude(self, valor):
        print(f"Valor com desconto: {valor}")
    
    