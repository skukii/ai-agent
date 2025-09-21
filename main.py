import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    arguments = sys.argv
    
    user_prompt = arguments[1]

    if len(arguments)>2:
        if str(arguments[2]) == "--verbose":
            ver = True
    else:
        ver = False

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]  

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
    )
    if ver:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")




if __name__ == "__main__":
    main()
