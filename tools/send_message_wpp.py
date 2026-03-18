import time
from agent.runner import load_contacts
from playwright.sync_api import sync_playwright
from config.settings import CONTACTS_WPP_PATH, WPP_USER_DATA_DIR, WPP_CONTEXT_HEADLESS, WPP_URL

CONTEXT_PLAYWRIGHT = sync_playwright().start().firefox.launch_persistent_context(
                user_data_dir=WPP_USER_DATA_DIR,
                headless=WPP_CONTEXT_HEADLESS
            )
PAGE_WPP = CONTEXT_PLAYWRIGHT.pages[0]
PAGE_WPP.goto(WPP_URL)

CONTACTS = load_contacts(CONTACTS_WPP_PATH)

def send_message_wpp(input: dict) -> str:
    message = input.get("message")
    contact = input.get("contact")
    phone = CONTACTS.get(contact.lower())

    if not phone:
        return f"Contato '{contact}' não encontrado."
    
    try:
        search_box = PAGE_WPP.locator("input[role='textbox'][aria-label='Pesquisar ou começar uma nova conversa']")
        search_box.fill(contact)
        time.sleep(1) 

        first_result = PAGE_WPP.locator("div[role='gridcell']").first
        first_result.click()

        msg_box = PAGE_WPP.locator("footer div[contenteditable='true']")
        msg_box.fill(message)
        msg_box.press("Enter")

        time.sleep(1)
    except Exception as e:
        return f"Erro no envio da mensagem: {e}"

    return f"Mensagem enviada para {contact}"