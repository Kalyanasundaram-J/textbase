from textbase import bot, Message
from textbase.models import HuggingFace
from typing import List

# Load your HuggingFace API key
HuggingFace.api_key = "<API_KEY>"

# We can ignore this if we set a default value for this argument is class defenition
# Need to add this to ignore argument error. If we don't change the models file.
# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI. There are no specific prefixes for responses, so you can ask or talk about anything you like.
The AI will respond in a natural, conversational manner. Feel free to start the conversation with any question or topic, and let's have a
pleasant chat!
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):
    
    # Generate HuggingFace response. Uses the google/flan-t5-xxl model from Google by default.
    bot_response = HuggingFace.generate(
        system_prompt=SYSTEM_PROMPT,
        model="google/flan-t5-xxl",
        message_history=message_history, # Assuming history is the list of user messages
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }