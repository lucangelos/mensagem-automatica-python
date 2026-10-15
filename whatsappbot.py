from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ===================== CONFIGURAÇÃO =====================
contatos = ['Trabalhos', 'Clientes']
mensagem = "Olá, tudo bem?"
# ========================================================

# Vários seletores possíveis (o WhatsApp muda o HTML com frequência)
SELETORES_BUSCA = [
    '//div[@id="side"]//div[@contenteditable="true"]',
    '//div[@contenteditable="true"][@data-tab="3"]',
    '//input[@role="textbox"]',
    '//input[@type="text"]',
    '//*[@contenteditable="true"][contains(@aria-label,"esquis")]',
    '//*[@contenteditable="true"][contains(@aria-label,"earch")]',
]

SELETORES_MENSAGEM = [
    '//footer//div[@contenteditable="true"]',
    '//div[@contenteditable="true"][@data-tab="10"]',
    '//*[@contenteditable="true"][contains(@aria-label,"ensagem")]',
    '//*[@contenteditable="true"][contains(@aria-label,"essage")]',
]

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://web.whatsapp.com/')

print("Escaneie o QR code no navegador que abriu.")
input("Quando as suas conversas estiverem carregadas, aperte ENTER aqui... ")


def achar_elemento(seletores, segundos_por_seletor=5):
    """Tenta cada seletor da lista e devolve o primeiro elemento clicável."""
    for xpath in seletores:
        try:
            return WebDriverWait(driver, segundos_por_seletor).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
        except TimeoutException:
            continue
    return None


def diagnostico(etapa):
    """Mostra o que existe na tela para ajudar a achar o seletor certo."""
    print(f"\n--- DIAGNÓSTICO ({etapa}) ---")
    driver.save_screenshot(f"erro_{etapa}.png")
    print(f"Screenshot salvo: erro_{etapa}.png")
    elementos = driver.find_elements(
        By.XPATH, '//*[@contenteditable="true"] | //input'
    )
    print(f"Campos editáveis encontrados: {len(elementos)}")
    for el in elementos:
        try:
            html = driver.execute_script(
                "return arguments[0].outerHTML.substring(0, 300);", el
            )
            print(" ->", html)
        except Exception:
            pass
    print("--- FIM DO DIAGNÓSTICO ---\n")


def buscar_contato(contato):
    """Pesquisa o contato/grupo e abre a conversa."""
    campo = achar_elemento(SELETORES_BUSCA)

    if campo is None:
        # Plano B: atalho do próprio WhatsApp Web para focar a busca
        driver.find_element(By.TAG_NAME, 'body').send_keys(
            Keys.CONTROL + Keys.ALT + '/'
        )
        time.sleep(1)
        campo = driver.switch_to.active_element

    campo.click()
    campo.send_keys(Keys.CONTROL + "a")
    campo.send_keys(Keys.BACKSPACE)
    campo.send_keys(contato)
    time.sleep(2)  # tempo para a lista de resultados atualizar
    campo.send_keys(Keys.ENTER)
    time.sleep(2)


def enviar_mensagem(texto):
    """Digita e envia a mensagem na conversa aberta."""
    campo = achar_elemento(SELETORES_MENSAGEM, segundos_por_seletor=8)
    if campo is None:
        raise RuntimeError("caixa_de_mensagem_nao_encontrada")

    campo.click()

    # Suporta várias linhas (SHIFT+ENTER quebra a linha sem enviar)
    linhas = texto.split("\n")
    for i, linha in enumerate(linhas):
        campo.send_keys(linha)
        if i < len(linhas) - 1:
            campo.send_keys(Keys.SHIFT + Keys.ENTER)

    campo.send_keys(Keys.ENTER)
    time.sleep(2)  # garante que a mensagem foi enviada


for contato in contatos:
    etapa = "busca"
    try:
        print(f"Enviando para: {contato}...")
        buscar_contato(contato)
        etapa = "mensagem"
        enviar_mensagem(mensagem)

        # ESC fecha a conversa, evitando enviar para o chat errado
        # caso o próximo contato não seja encontrado
        driver.switch_to.active_element.send_keys(Keys.ESCAPE)
        time.sleep(1)
        print(f"  OK: mensagem enviada para {contato}")
    except Exception as erro:
        print(f"  ERRO na etapa '{etapa}' para {contato}: {type(erro).__name__} {erro}")
        diagnostico(f"{etapa}_{contato}")

print("Finalizado.")
time.sleep(5)
driver.quit()