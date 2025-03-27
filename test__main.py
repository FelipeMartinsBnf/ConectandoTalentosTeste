
import entity
import time
def test_usuario_cadastro():
    """ Teste Unitário """
    """Testa se um Usuário consegue ser inicializado corretamente"""
    nome = "Felipe Martins"
    email = "felipemartinsbn@gmail.com.br"
    area_interesse = ["Dev", "Java"]
    
    usuario = entity.Usuario(nome, email, area_interesse)
    assert usuario.nome == nome
    assert usuario.email == email
    assert usuario.area_interesse == area_interesse
    assert usuario.vagas_cadastradas == []

def test_usuario_cadastro_email_errado():
    """Verifica se o sistema bloqueia a criação com um e-mail inválido"""
    """ Teste Unitário """
    nome = "Felipe Martins"
    email = "felipemartinsbn"
    area_interesse = ["Dev", "Java"]

    try:   
        usuario = entity.Usuario(nome, email, area_interesse)
        assert False
    except Exception as e:
        assert str(e) == "Email Inválido"

def test_verificar_candidatar():
    """Verifica se o usuário consegue se candidatar a uma vaga"""
    """ Teste De integração entre usuário e Empresa"""

    estudante = entity.Usuario("Paulo", "Tusiozshi@airbus.com", "Passarologia")
    empresa = entity.Empresa("Fepi", "Educação")
    vaga = empresa.criar_vaga("Professor", "Professor de engenharia de pássaros", ["Passarologia", "Biologia"])
    empresa.vagas[0].candidatar(estudante);
    print(empresa.vagas)
    assert empresa.vagas[0].candidatos[0] == estudante

def test_verificar_candidatar_inapto():
    """Verifica se o sistema recusa a inscrever um usuários que não possui uma area de interesse para a vaga"""
    """ Teste De Sistema - Fluxo Completo"""

    estudante = entity.Usuario("Paulinho", "paulinhoGardenia@valonia.com", "Busologia")
    empresa = entity.Empresa("Hambugeria do Toninho", "Comida")
    vaga = empresa.criar_vaga("Tecnico de chapa", "Cozinhiro com mais de 2 anos ....", ["Cozinha", "Liderança"])
    empresa.vagas[0].candidatar(estudante)
    
    assert not vaga.candidatos

def test_desempenho():
    """Verifica se o sistema consegue cadastrar 200 usuários em menos de 5 segundos"""
    """ Teste De desempenho"""
    inicio = time.time();
    for x in range(200000):
        estudante = entity.Usuario("Paulinho", "paulinhoGardenia@valonia.com", "Busologia")
        empresa = entity.Empresa("Cesar burges lanchonete", "Comida")
        vaga = empresa.criar_vaga("Tecnico de chapa", "Tecnico para manuseat chapas qunetes", ["Chapa", "Lanche"])
        empresa.vagas[0].candidatar(estudante)

    final = time.time();
    assert final - inicio < 1