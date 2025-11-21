import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = 'OPENAI_KEY_REMOVED'

try:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, world!"}]
    )
    print("API key is valid. Response:", response.choices[0].message.content)
except openai.APIError as e:
    print(f"API key test failed: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")