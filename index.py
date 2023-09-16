import openai
openai.api_key = "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"

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text_1 = f"""
"""
prompt = f"""
What is India's capital?
"""
response = get_completion(prompt)
print("Completion for Text 1:")
print(response)