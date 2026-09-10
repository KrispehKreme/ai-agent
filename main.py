'''This is the main entry point for the AI agent application.'''
import argparse
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
    raise RuntimeError("Cannot find API key")

MAX_ITERATIONS = 20

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(MAX_ITERATIONS):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
            temperature=0,
        )

        usage = response.usage
        if usage is None:
            raise RuntimeError("No usage data returned. The API request likely failed")

        if args.verbose:
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Response tokens: {usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print("Final response:")
            print(message.content)
            return

        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if not result_message["content"]:
                raise Exception(f"Fatal: no content from tool call {tool_call.function.name}")
            if args.verbose:
                print(f"-> {result_message['content']}")
            messages.append(result_message)

    print(f"Error: Maximum iterations ({MAX_ITERATIONS}) reached without a final response.")
    sys.exit(1)

if __name__ == "__main__":
    main()
