from pathlib import Path

#Base path
BASE_DIR = Path(__file__).resolve().parent.parent

#Important paths
PROMPTS_DIR = BASE_DIR / "prompts"
PROMPTS_FINAL_DIR = BASE_DIR / "prompts" / "final_answer"
CONTACTS_WPP_PATH = BASE_DIR / "data" / "contacts_wpp.json"

#Model params
MODEL_NAME = "llama3"
MODEL_TEMPERATURES = {
    "calculator": 0,
    "ddg_search": 0.3,
    "generic": 0.7,
    "g1_news": 0.3,
    "open_program": 0,
    "weather": 0.1,
    "pc_status": 0,
    "send_message_wpp": 0
}
MODEL_N_PREDICTIONS = 1024

#TOOL - No tool
NO_TOOL_RESULT = "No tool selected, answer without tools"

#TOOL - Weather
API_WEATHER_URL = "https://wttr.in/{city}?format=j1"

#TOOL - News
RSS_G1 = "https://g1.globo.com/rss/g1/" 
RSS_MAX_ARTICLES = 50

#TOOL - DuckDuckGo
DDG_MAX_RESULTS = 10
DDG_REGION = "pt-br"

#TOOL - Open Program
ALLOWED_PROGRAMS = {
    "calculator": "gnome-calculator",  

    "brave": "brave-browser",
    "edge": "microsoft-edge",
    "firefox": "firefox",

    "terminal": "gnome-terminal",

    "monitor": "gnome-system-monitor",
    "system monitor": "gnome-system-monitor",

    "obs": "obs",

    "spotify": "spotify",

    "vs code": "code",
    "vscode": "code", 
    "code": "code"
}

#TOOL - Send message whatsapp
WPP_USER_DATA_DIR = BASE_DIR / "firefox_whatsapp_profile"
WPP_CONTEXT_HEADLESS = True 
WPP_URL = "https://web.whatsapp.com/"