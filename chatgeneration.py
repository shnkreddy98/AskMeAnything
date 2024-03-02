def generateText(client, user_text):

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}],
        stream=True,
    )

    # print("Generating Text...")

    response = []

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response.append(chunk.choices[0].delta.content)

    return response

