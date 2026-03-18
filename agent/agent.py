import ollama
import json 
from agent.tools_registery import TOOLS 
from config.settings import MODEL_NAME, MODEL_TEMPERATURES, NO_TOOL_RESULT

def run_agent(question: str, PROMPTS: dict) -> dict:
    try:    
        response = client.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": PROMPTS.get("system")},
                {"role": "user", "content": PROMPTS.get("tool_selection").format(
                    user_input=question
                )}
            ],
            format="json"
        )

        response_content = response.message.content
        data = json.loads(response_content)
        tool = data.get("tool")
        print(f"Tool: {tool}")
        
        if tool: 
            tool_input = data.get("input")
            tool_result = TOOLS[tool](tool_input)
        else:
            tool_result = NO_TOOL_RESULT

        final_response = client.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": PROMPTS.get("system")},
                {"role": "user", "content": PROMPTS.get("final").get(f"final_{tool if tool else 'generic'}").format(
                    question =question,
                    tool_result=tool_result
                )}
            ],
            options={
                "temperature": MODEL_TEMPERATURES.get(tool if tool else "generic")
            },
        )

        final_response = final_response.message.content

        return final_response 
    except Exception as e:
        return f"Error: {e}"

client = ollama.Client()