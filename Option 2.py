import openai_secret_manager
import openai
import random
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]
model_engine = "text-davinci-002"
prompt = "The following is a conversation with an AI assistant. The assistant can help you with a variety of tasks. To get started, please enter a command or ask a question."
fallback_responses = {
    "default": ["I'm sorry, I don't understand what you're asking. Please try again.", 
                "I'm not sure I understand. Can you please rephrase your question?", 
                "I'm sorry, I'm not capable of doing that."]
}
def generate_response(prompt, model, engine):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
def handle_input(user_input):
    ai_response = generate_response(prompt + user_input, model_engine, model_engine)
    if ai_response == "" or ai_response in fallback_responses["default"]:
        return random.choice(fallback_responses["default"])
    else:
        return ai_response
def chat():
    print("Hi, I'm an AI assistant. How can I assist you today?")
    while True:
        user_input = input(">> ")
        user_input = user_input.lower()
        if user_input == "quit":
            break
        bot_response = handle_input(user_input)
        print(bot_response)
chat()
