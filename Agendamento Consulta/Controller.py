
import uuid
from Model import PacienteModel, HistoricoModel, ConsultaModel
from View import PacienteView, HistoricoView, ConsultaView
from datetime import datetime

class PacienteController:

    def __init__(self, view: PacienteView, model: PacienteModel):
        self.view = view
        self.model = model

    def controllerAdquirirDados(self):
        nome, idade, sexo, telefone, plano_saude = self.view.viewAdquirirDados()
        id = str(uuid.uuid4())
        self.model.setId(id)
        self.model.setNome(nome)
        self.model.setIdade(idade)
        self.model.setSexo(sexo)
        self.model.setTelefone(telefone)
        self.model.setPlanoSaude(plano_saude)

    def controllerInserir(self):
        self.model.modelInserir(self.model)
    
    def controllerListarTodos(self):
        objetos_paciente = self.model.modelListarTodos()
        self.view.viewMostrarDados(objetos_paciente)

    def controllerListarId(self, id):
        objeto_paciente = self.model.modelListarId(id)
        self.view.viewMostrarDado(objeto_paciente)
    
    def controllerExcluir(self, id):
        self.model.modelExcluir(id)
    
class HistoricoController:

    def __init__(self, view: HistoricoView, model: HistoricoModel):
        self.view = view
        self.model = model
    
    def controllerAdquirirDados(self):
        medicamentos, historicos, id_paciente = self.view.viewAdquirirDados()
        pacientemodel = PacienteModel()
        paciente = pacientemodel.modelListarId(id_paciente)

        id = str(uuid.uuid4())
        self.model.setId(id)
        self.model.setMedicamento(medicamentos)
        self.model.setHistorico(historicos)
        self.model.setPaciente(paciente.__dict__)

    def controllerInserir(self):
        self.model.modelInserir(self.model)
    
    def controllerListarTodos(self):
        objetos_historico = self.model.modelListarTodos()
        self.view.viewMostrarDados(objetos_historico)
    
    def controllerListarId(self, id):
        objeto_historico = self.model.modelListarId(id)
        self.view.viewMostrarDado(objeto_historico)
    
    def controllerExcluir(self, id):
        self.model.modelExcluir(id)

class ConsultaController:

    def __init__(self, view: ConsultaView, model: ConsultaModel):
        self.view = view
        self.model = model
    
    def controllerAdquirirDados(self):
        horario_consulta, nome_medico, valor_consulta, id_paciente = self.view.viewAdquirirDados()
        pacientemodel = PacienteModel()
        paciente = pacientemodel.modelListarId(id_paciente)

        id = str(uuid.uuid4())
        self.model.setId(id)
        self.model.setHorarioConsulta(horario_consulta)
        self.model.setNomeMedico(nome_medico)
        self.model.setValorConsulta(valor_consulta)
        self.model.setPaciente(paciente.__dict__)

    def controllerInserir(self):
        self.model.modelInserir(self.model)
    
    def controllerListarTodos(self):
        objetos_consulta = self.model.modelListarTodos()
        self.view.viewMostrarDados(objetos_consulta)

    def controllerListarId(self, id):
        objeto_consulta = self.model.modelListarId(id)
        self.view.viewMostrarDado(objeto_consulta)
    
    def controllerExcluir(self, id):
        self.model.modelExcluir(id)
    
    def controllerPlanoSaude(self, id_consulta):
        objeto_consulta = self.model.modelListarId(id_consulta)
        valor_consulta = objeto_consulta.valor_consulta
        plano_saude = objeto_consulta.paciente['plano_saude']
        valor = self.model.modelPlanoSaude(plano_saude, valor_consulta)
        self.view.viewPlanoSaude(valor)

    

