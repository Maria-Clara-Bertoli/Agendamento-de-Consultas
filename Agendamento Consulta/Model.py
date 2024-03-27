import json
from datetime import datetime

class PacienteModel:

    def __init__(self):
        pass
    
    def setId(self, id: str):
        self.id = id

    def setNome(self, nome: str):
        self.nome = nome
    
    def setIdade(self, idade: int):
        self.idade = idade
    
    def setSexo(self, sexo: str):
        self.sexo = sexo
    
    def setTelefone(self, telefone: str):
        self.telefone = telefone
    
    def setPlanoSaude(self, plano_saude: bool):
        self.plano_saude = plano_saude
    
    def modelInserir(self, dados):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_paciente.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
            except:
                json_arquivo = None

        if json_arquivo is None:
            json_lista = []
            with open(caminho_arquivo, "r+") as saida_json:
                json_lista.append(dados.__dict__)
                json_arquivo = json.dumps(json_lista)
                saida_json.write(json_arquivo)
        else:
            with open(caminho_arquivo, "w") as saida_json:
                pass
            with open(caminho_arquivo, "w") as saida_json:
                json_arquivo.append(dados.__dict__)
                saida_json.write(json.dumps(json_arquivo))
    
    def modelListarTodos(self):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_paciente.json'
        objetos_paciente = []

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                for json_dado in json_arquivo:
                    pacientemodel = PacienteModel()
                    pacientemodel.id = json_dado['id']
                    pacientemodel.nome = json_dado['nome']
                    pacientemodel.idade = json_dado['idade']
                    pacientemodel.sexo = json_dado['sexo']
                    pacientemodel.telefone = json_dado['telefone']
                    pacientemodel.plano_saude = json_dado['plano_saude']
                    objetos_paciente.append(pacientemodel)
                return objetos_paciente
            except:
                pass
    
    def modelListarId(self, id):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_paciente.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                pacientemodel = PacienteModel()
                for json_dado in json_arquivo:
                    if id in json_dado['id']:
                        pacientemodel.id = json_dado['id']
                        pacientemodel.nome = json_dado['nome']
                        pacientemodel.idade = json_dado['idade']
                        pacientemodel.sexo = json_dado['sexo']
                        pacientemodel.telefone = json_dado['telefone']
                        pacientemodel.plano_saude = json_dado['plano_saude']
                        break
                return pacientemodel
            except:
                pass
        
    def modelExcluir(self, id):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_paciente.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
            except:
                json_arquivo = None

        if json_arquivo is not None:
            json_lista = []

            for json_dado in json_arquivo:
                if json_dado['id'] != id:
                    json_lista.append(json_dado)
            
            with open(caminho_arquivo, "w") as saida_json:
                pass

            with open(caminho_arquivo, "w") as saida_json:
                saida_json.write(json.dumps(json_lista))

class HistoricoModel:

    def __init__ (self):
        pass

    def setId(self, id: str):
        self.id = id

    def setMedicamento(self, medicamento: list):
        self.medicamento = medicamento
    
    def setHistorico(self, historico: list):
        self.historico = historico
    
    def setPaciente(self, paciente: dict):
        self.paciente = paciente
    
    def modelInserir(self, dados):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_historico.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
            except:
                json_arquivo = None

        if json_arquivo is None:
            json_lista = []
            with open(caminho_arquivo, "r+") as saida_json:
                json_lista.append(dados.__dict__)
                json_arquivo = json.dumps(json_lista)
                saida_json.write(json_arquivo)
        
        else:
            with open(caminho_arquivo, "w") as saida_json:
                pass
            with open(caminho_arquivo, "w") as saida_json:
                json_arquivo.append(dados.__dict__)
                saida_json.write(json.dumps(json_arquivo))
    
    def modelListarTodos(self):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_historico.json'
        objetos_historico = []

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                for json_dado in json_arquivo:
                    historicomodel = HistoricoModel()
                    historicomodel.id = json_dado['id']
                    historicomodel.medicamento = json_dado['medicamento']
                    historicomodel.historico = json_dado['historico']
                    historicomodel.paciente = json_dado['paciente']
                    objetos_historico.append(historicomodel)
                return objetos_historico
            except:
                pass
    
    def modelListarId(self, id):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_historico.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                historicomodel = HistoricoModel()
                for json_dado in json_arquivo:
                    if id in json_dado['id']:
                        historicomodel.id = json_dado['id']
                        historicomodel.historico = json_dado['historico']
                        historicomodel.medicamento = json_dado['medicamento']
                        historicomodel.paciente = json_dado['paciente']
                        break
                return historicomodel
            except:
                pass
    
    def modelExcluir(self, id):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_historico.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
            except:
                json_arquivo = None

        if json_arquivo is not None:
            json_lista = []

            for json_dado in json_arquivo:
                if json_dado['id'] != id:
                    json_lista.append(json_dado)
            
            with open(caminho_arquivo, "w") as saida_json:
                pass

            with open(caminho_arquivo, "w") as saida_json:
                saida_json.write(json.dumps(json_lista))

class ConsultaModel:

    def __init__(self):
        pass

    def setId(self, id: str):
        self.id = id
    
    def setHorarioConsulta(self, horario: datetime):
        self.horario = horario
    
    def setNomeMedico(self, nome_medico: str):
        self.nome_medico = nome_medico
    
    def setValorConsulta(self, valor_consulta: float):
        self.valor_consulta = valor_consulta
    
    def setPaciente(self, paciente: dict):
        self.paciente = paciente
    
    def modelInserir(self, dados):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_consulta.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
            except:
                json_arquivo = None

        if json_arquivo is None:
            json_lista = []
            with open(caminho_arquivo, "r+") as saida_json:
                json_lista.append(dados.__dict__)
                json_arquivo = json.dumps(json_lista)
                saida_json.write(json_arquivo)
        
        else:
            with open(caminho_arquivo, "w") as saida_json:
                pass
            with open(caminho_arquivo, "w") as saida_json:
                json_arquivo.append(dados.__dict__)
                saida_json.write(json.dumps(json_arquivo))
    
    def modelListarTodos(self):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_consulta.json'
        objetos_consulta = []

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                for json_dado in json_arquivo:
                    consultamodel = ConsultaModel()
                    consultamodel.id = json_dado['id']
                    consultamodel.horario = json_dado['horario']
                    consultamodel.nome_medico = json_dado['nome_medico']
                    consultamodel.valor_consulta = json_dado['valor_consulta']
                    consultamodel.paciente = json_dado['paciente']
                    objetos_consulta.append(consultamodel)
                return objetos_consulta
            except:
                pass
    
    def modelListarId(self, id):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_consulta.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
                consultamodel = ConsultaModel()
                for json_dado in json_arquivo:
                    if id in json_dado['id']:
                        consultamodel.id = json_dado['id']
                        consultamodel.horario = json_dado['horario']
                        consultamodel.paciente = json_dado['paciente']
                        consultamodel.nome_medico = json_dado['nome_medico']
                        consultamodel.valor_consulta = json_dado['valor_consulta']
                        break
                return consultamodel
            except:
                pass
    
    def modelExcluir(self, id):
        caminho_arquivo = r'C:\Users\User\Documents\Python\Agendamento Consulta\json_consulta.json'

        with open(caminho_arquivo, "r") as saida_json:
            try:
                json_arquivo = json.load(saida_json)
            except:
                json_arquivo = None

        if json_arquivo is not None:
            json_lista = []

            for json_dado in json_arquivo:
                if json_dado['id'] != id:
                    json_lista.append(json_dado)
            
            with open(caminho_arquivo, "w") as saida_json:
                pass

            with open(caminho_arquivo, "w") as saida_json:
                saida_json.write(json.dumps(json_lista))
    
    def modelPlanoSaude(self, plano_saude, valor_consulta):
        if plano_saude:
            valor_consulta = valor_consulta - ((valor_consulta/100) * 30)
            return valor_consulta
        else:
            return valor_consulta


    




