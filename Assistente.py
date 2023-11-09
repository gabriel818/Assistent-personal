from openai import OpenAI
client = OpenAI(
    api_key= "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"
)


def enviar_mensagem(mensagem):
    chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {'role': 'user', 'content': mensagem},

        ],


    )

    return chat_completion #["choices"][0]["message"],

print(enviar_mensagem("olá"))