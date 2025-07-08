from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"  # OpenRouter's OpenAI-compatible endpoint
)

def main():
    print("🤖 Miko AI (type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct:free",  # free model (change if you want other models)
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content
        print(f"Miko: {reply}")

if __name__ == "__main__":
    main()
