# 🤖 Robô de Mensagens para WhatsApp (Grupos e Contatos)

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Plataforma](https://img.shields.io/badge/WhatsApp-Web-25D366?logo=whatsapp&logoColor=white)

Automação em **Python + Selenium** que envia **a mesma mensagem para vários grupos e contatos do WhatsApp** com um único comando.

Pensado para pessoas e empresas que precisam repetir o mesmo aviso, lembrete ou comunicado várias vezes ao dia: em vez de abrir cada conversa e digitar tudo de novo, basta rodar o script.

---

## 📑 Sumário

- [O problema que o projeto resolve](#-o-problema-que-o-projeto-resolve)
- [Funcionalidades](#-funcionalidades)
- [Como funciona](#-como-funciona)
- [Tecnologias](#-tecnologias)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Como usar](#-como-usar)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Solução de problemas](#-solução-de-problemas)
- [Boas práticas e avisos importantes](#-boas-práticas-e-avisos-importantes)
- [Roadmap](#-roadmap)
- [Contribuindo](#-contribuindo)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 🎯 O problema que o projeto resolve

Muitos negócios e equipes precisam enviar a mesma mensagem para vários grupos todos os dias:

- avisos de horário, promoções ou atualizações para grupos de clientes;
- lembretes e comunicados para grupos de trabalho;
- mensagens de bom dia, relatórios ou cobranças recorrentes.

Fazer isso manualmente é repetitivo, consome tempo e está sujeito a erros (esquecer um grupo, enviar para o lugar errado). Este robô automatiza o processo: **você define quem recebe e o que será enviado, e ele faz o resto.**

---

## ✨ Funcionalidades

- ✅ Envio da mesma mensagem para **uma lista de grupos e/ou contatos**
- ✅ Suporte a **mensagens com várias linhas**
- ✅ **Esperas inteligentes** (`WebDriverWait`) em vez de pausas fixas
- ✅ **Vários seletores de reserva**, para resistir a mudanças no HTML do WhatsApp Web
- ✅ **Atalho de busca como plano B** (`Ctrl + Alt + /`)
- ✅ **Tratamento de erros por contato**: se um envio falhar, o robô segue para o próximo
- ✅ **Diagnóstico automático**: em caso de falha, salva um screenshot e lista os campos encontrados na tela
- ✅ Não precisa baixar o ChromeDriver manualmente (o **Selenium Manager** cuida disso)

---

## ⚙️ Como funciona

```
┌────────────────────┐
│  Abre o WhatsApp   │
│  Web no Chrome     │
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Você escaneia o QR │
│ code e aperta ENTER│
└─────────┬──────────┘
          ▼
┌────────────────────────────────────┐
│  Para cada contato/grupo da lista: │
│  1. Pesquisa o nome                │
│  2. Abre a conversa                │
│  3. Digita e envia a mensagem      │
│  4. Fecha a conversa (ESC)         │
└─────────┬──────────────────────────┘
          ▼
┌────────────────────┐
│ Exibe o resultado  │
│ e encerra          │
└────────────────────┘
```

---

## 🛠 Tecnologias

| Tecnologia | Uso |
|---|---|
| [Python 3](https://www.python.org/) | Linguagem principal |
| [Selenium 4](https://www.selenium.dev/) | Automação do navegador |
| Google Chrome | Navegador controlado pelo robô |
| WhatsApp Web | Interface usada para o envio |

---

## 📋 Pré-requisitos

- **Python 3.9 ou superior**
- **Google Chrome** instalado e atualizado
- Uma conta de WhatsApp com acesso ao WhatsApp Web (celular por perto para ler o QR code)
- Conexão com a internet

---

## 📥 Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
```

**2. Crie e ative um ambiente virtual** (recomendado)

```powershell
# Windows (PowerShell)
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

**3. Instale as dependências**

```bash
pip install -r requirements.txt
```

> 💡 Não é necessário instalar o `webdriver_manager`. Desde o Selenium 4.6, o **Selenium Manager** baixa e gerencia o ChromeDriver automaticamente.

---

## 🔧 Configuração

Abra o arquivo `whatsappbot.py` e edite o bloco de configuração no topo:

```python
# ===================== CONFIGURAÇÃO =====================
contatos = ['Trabalhos', 'Clientes']
mensagem = "Olá, tudo bem?"
# ========================================================
```

| Variável | Descrição |
|---|---|
| `contatos` | Lista com os **nomes exatos** dos grupos/contatos, como aparecem no seu WhatsApp |
| `mensagem` | Texto que será enviado para todos da lista |

### Mensagem com várias linhas

Use `\n` para quebrar linha:

```python
mensagem = "Bom dia, pessoal!\nSegue o aviso de hoje:\nReunião às 15h."
```

> ⚠️ **Atenção:** o robô pesquisa pelo nome e seleciona o **primeiro resultado**. Use o nome completo e exato do grupo (acentos e maiúsculas incluídos) para evitar enviar para a conversa errada.

---

## ▶️ Como usar

1. Execute o script:

   ```bash
   python whatsappbot.py
   ```

2. O Chrome abrirá o WhatsApp Web. **Escaneie o QR code** com o seu celular  
   (*WhatsApp → Aparelhos conectados → Conectar um aparelho*).

3. Quando as suas conversas estiverem carregadas, volte ao terminal e aperte **ENTER**.

4. Acompanhe o progresso pelo terminal:

   ```
   Enviando para: Trabalhos...
     OK: mensagem enviada para Trabalhos
   Enviando para: Clientes...
     OK: mensagem enviada para Clientes
   Finalizado.
   ```

---

## 📁 Estrutura do projeto

```
.
├── whatsappbot.py      # Script principal do robô
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

---

## 🩺 Solução de problemas

| Erro | Causa provável | Solução |
|---|---|---|
| `'str' object has no attribute 'capabilities'` | Uso antigo do `webdriver.Chrome(caminho)` | Use `webdriver.Chrome()` ou `Service(...)`. Este projeto já usa a forma correta |
| `no attribute 'find_element_by_xpath'` | Método removido no Selenium 4 | Use `find_element(By.XPATH, ...)` |
| `TimeoutException` na etapa **busca** | O seletor da caixa de pesquisa mudou | Veja o diagnóstico no terminal e ajuste `SELETORES_BUSCA` |
| `TimeoutException` na etapa **mensagem** | A conversa não abriu (nome não encontrado) | Confira se o nome em `contatos` está idêntico ao do WhatsApp |
| Pede o QR code toda vez | O Chrome abre sempre com perfil limpo | Veja a dica abaixo para salvar a sessão |

### 💾 Dica: manter o login salvo

Para não escanear o QR code a cada execução, use um perfil fixo do Chrome. Adicione antes de criar o `driver`:

```python
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\caminho\para\perfil-chrome")
driver = webdriver.Chrome(options=options)
```

### 🔍 Diagnóstico automático

Se um envio falhar, o robô gera um arquivo `erro_<etapa>_<contato>.png` e imprime no terminal o HTML dos campos editáveis encontrados. Isso facilita encontrar o seletor correto caso o WhatsApp Web mude.

---

## ⚠️ Boas práticas e avisos importantes

- Este projeto **não é afiliado, associado ou endossado pelo WhatsApp/Meta**.
- O uso de automação no WhatsApp pode ir contra os **Termos de Serviço** da plataforma. Dependendo do volume e do comportamento, a conta pode sofrer **restrições ou banimento**.
- Para reduzir riscos:
  - envie **apenas para grupos e contatos que esperam receber** a mensagem;
  - **evite volume excessivo** e envios em massa para desconhecidos (spam);
  - mantenha **intervalos** entre os envios;
  - para uso comercial em larga escala, considere a **API oficial do WhatsApp Business**.
- Use por sua conta e risco. O autor não se responsabiliza por uso indevido.
- O WhatsApp Web muda seu HTML com frequência, então os seletores podem precisar de ajustes de tempos em tempos.

---

## 🗺 Roadmap

- [ ] Ler a lista de contatos e a mensagem de um arquivo externo (`.json`, `.csv` ou `.txt`)
- [ ] Agendamento automático de horários (várias vezes ao dia)
- [ ] Envio de imagens, documentos e arquivos
- [ ] Mensagens diferentes por contato/grupo
- [ ] Salvar sessão do WhatsApp automaticamente
- [ ] Registro de envios em arquivo de log
- [ ] Interface gráfica simples

---

## 🤝 Contribuindo

Contribuições são bem-vindas!

1. Faça um **fork** do projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça o commit: `git commit -m "Adiciona minha feature"`
4. Envie para a sua branch: `git push origin minha-feature`
5. Abra um **Pull Request**

---

## 👤 Autor

**Lucas Ângelo**

- GitHub: [@SEU-USUARIO](https://github.com/SEU-USUARIO)

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.