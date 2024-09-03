from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'João da Silva',
            email = 'testedemodelo@gmail.com',
            cpf = '41917058063',
            data_nascimento = '1984-01-01',
            celular = '86 999999-9999'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()),set(['id','nome','email','cpf','data_nascimento','celular']))
    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        data = self.serializer_estudante.data
        self.assertEqual(data['nome'], self.estudante.nome)
        self.assertEqual(data['email'], self.estudante.email)
        self.assertEqual(data['cpf'], self.estudante.cpf)
        self.assertEqual(data['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(data['celular'], self.estudante.celular)

class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo = 'CTT1',
            descricao = 'Curso de Teste 1',
            nivel = 'B'
        )
        self.serializer_curso = CursoSerializer(instance=self.curso)

    def test_verifica_campos_serializados_de_curso(self):
        dados = self.serializer_curso.data
        self.assertEqual(set(dados.keys()),set(['id','codigo','descricao','nivel']))
    def test_verifica_conteudo_dos_campos_serializados_de_curso(self):
        data = self.serializer_curso.data
        self.assertEqual(data['codigo'], self.curso.codigo)
        self.assertEqual(data['descricao'], self.curso.descricao)
        self.assertEqual(data['nivel'], self.curso.nivel)

class SerializerMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante_matricula = Estudante.objects.create(
            nome = 'Teste Modelo Matricula',
            email='testemodelomatricula@gmail.com',
            cpf='91546870040',
            data_nascimento='2003-02-02',
            celular='86 99999-9999'
        )
        self.curso_matricula = Curso.objects.create(
            codigo='CTMM',descricao='Curso Teste Modelo Matricula',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante_matricula,
            curso=self.curso_matricula,
            periodo='M'
        )
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)

    def test_verifica_campos_serializados_de_matricula(self):
        dados = self.serializer_matricula.data
        self.assertEqual(set(dados.keys()),set(['id','estudante','curso','periodo']))
    def test_verifica_conteudo_dos_campos_serializados_de_matricula(self):
        data = self.serializer_matricula.data
        self.assertEqual(data['estudante'], self.matricula.estudante.id)
        self.assertEqual(data['curso'], self.matricula.curso.id)
        self.assertEqual(data['periodo'], self.matricula.periodo)
