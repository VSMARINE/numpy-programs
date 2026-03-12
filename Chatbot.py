import google.generativeai as genai
print(genai.__version__)
genai.configure(api_key="AIzaSyDjfekJzefazGS8K8f3NyRzVoifeb4K5OQ")
model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()
while True:
    text=input("You: ")
    if text.lower() in ['exit','quit']:
        break
    response=chat.send_message(text)
    print("Bot:",response.text)

