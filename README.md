# **Documentação de Testes de Software**

## **Parte 1 - Levantamento de Requisitos e Conversa com o Cliente**

### **Visão Geral do Sistema**
Nosso sistema será uma plataforma voltada para ajudar estudantes de tecnologia a encontrarem oportunidades de estágio ou emprego. Da mesma forma, empresas poderão cadastrar e divulgar suas vagas para atingir candidatos qualificados. 

A partir das interações com o cliente, foram identificados os seguintes requisitos essenciais:

### **Requisitos do Sistema**

1. **Cadastro de Usuários**
   - Estudantes podem criar contas com:
     - Nome
     - E-mail
     - Área de interesse
     - Nível de experiência
     - Currículo anexado

2. **Cadastro de Empresas**
   - Empresas podem:
     - Criar um perfil empresarial
     - Registrar vagas de estágio/emprego
     - Visualizar perfis de candidatos

3. **Pesquisa de Vagas**
   - Estudantes podem buscar vagas aplicando filtros como:
     - Tecnologia exigida
     - Nível de experiência
     - Localização

4. **Candidatura a Vagas**
   - Usuários podem se candidatar diretamente pelo sistema.

5. **Sistema de Notificações**
   - Envio de alertas sobre:
     - Novas vagas disponíveis
     - Atualizações no processo seletivo

6. **Dashboard de Acompanhamento**
   - Os estudantes poderão visualizar o status de suas candidaturas.

7. **Autenticação Segura**
   - Implementação de login com:
     - E-mail e senha
     - MFA (Autenticação Multifator) opcional para maior segurança

---

## **Parte 2 - Plano de Testes**

### 1. **Introdução**
Este documento tem como objetivo estabelecer um plano de testes para o sistema de empregabilidade destinado a estudantes de tecnologia. O plano cobre diferentes tipos de testes para garantir a qualidade, estabilidade e usabilidade do sistema.

### 2. **Objetivos dos Testes**
O objetivo principal dos testes é validar a corretude, integração, desempenho e usabilidade do sistema, garantindo que ele atenda aos requisitos funcionais e não funcionais. O plano visa:

- Garantir que os usuários possam se cadastrar e buscar vagas corretamente.
- Confirmar que a candidatura às vagas funciona sem erros.
- Avaliar se as alterações no sistema não impactam funcionalidades antigas.
- Verificar o desempenho do sistema sob diferentes condições de carga.

### **3. Testes e Requisitos Correspondentes**

### **3.1. Teste de Unidade** (Verifica componentes isolados)

- **Objetivo:** Garantir que componentes individuais funcionam corretamente de forma isolada.
- **Cenário:** Verificar se o cadastro de usuários valida corretamente e-mails.
- **Critério de Sucesso:** Usuário só pode cadastrar-se com um e-mail válido.

### **3.2. Teste de Integração** (Verifica a interação entre módulos)

- **Objetivo:** Verificar a interação entre os módulos do sistema.
- **Cenário:** Validar se um estudante pode se candidatar corretamente a uma vaga.
- **Critério de Sucesso:** A candidatura é registrada corretamente e aparece no painel da empresa.

### **3.3. Teste de Sistema** (Verifica o funcionamento completo do sistema)

- **Objetivo:** Testar o sistema como um todo.
- **Cenário:** Criar um fluxo completo: cadastro de usuário → busca de vagas → candidatura → feedback da empresa.
- **Critério de Sucesso:** O estudante consegue navegar pelo sistema e concluir o processo sem erros.

### **3.4. Teste de Aceitação** (Valida se atende às necessidades do usuário)

- **Objetivo:** Avaliar a usabilidade do sistema para os usuários finais.
- **Cenário:** Um estudante tenta se cadastrar e encontrar uma vaga compatível.
- **Critério de Sucesso:** O estudante consegue concluir a tarefa sem dificuldades ou erros.

### **3.5. Teste de Regressão** (Garante que novas mudanças não quebrem funcionalidades antigas)

- **Objetivo:** Garantir que mudanças não quebrem funcionalidades existentes.
- **Cenário:** Se for alterada a lógica de busca de vagas, garantir que o cadastro de usuários e candidaturas ainda funcionam.
- **Critério de Sucesso:** Nenhuma funcionalidade antiga é impactada negativamente.

### **3.6. Teste de Desempenho** (Avalia tempo de resposta e escalabilidade)

- **Objetivo:** Avaliar o tempo de resposta e escalabilidade do sistema.
- **Cenário:** Medir o tempo de resposta ao criar muitos usuários.
- **Critério de Sucesso:** O tempo de resposta se mantém dentro dos limites aceitáveis.

### 4. **Cronograma de Testes**

| Fase | Teste | Início | Término |
| --- | --- | --- | --- |
| 1 | Teste de Unidade | 12/03/2025 | 13/03/2025 |
| 2 | Teste de Integração | 13/03/2025 | 15/03/2025 |
| 3 | Teste de Sistema | 19/03/2025 | 19/03/2025 |
| 4 | Teste de Aceitação | 20/03/2025 | 22/03/2025 |
| 5 | Teste de Regressão | 24/03/2025 | 25/03/2025 |
| 6 | Teste de Desempenho | 25/03/2025 | 26/03/2025 |

