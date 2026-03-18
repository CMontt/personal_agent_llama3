import subprocess
from config.settings import ALLOWED_PROGRAMS

def open_program(program_name: str) -> str:
    program = ALLOWED_PROGRAMS.get(program_name.lower())
    if not program:
        return f"O programa '{program_name}' não está autorizado ou não existe na whitelist."

    try:
        subprocess.Popen(
            [program],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        return f"O programa '{program_name}' foi aberto com sucesso!"
    except Exception as e:
        return f"Falha ao abrir o programa '{program_name}': {e}"