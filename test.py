# # from openai import OpenAI
# # # import os
# # import sys

# # openai_key = sys.argv[1]
# # print(openai_key)

# # client = OpenAI(organization=openai_key)

# # stream = client.chat.completions.create(
# #     model="gpt-4",
# #     messages=[{"role": "user", "content": "Say this is a test"}],
# #     stream=True,
# # )
# # for chunk in stream:
# #     if chunk.choices[0].delta.content is not None:
# #         print(chunk.choices[0].delta.content, end="")

# response = ['fd', 'df', 'df']
# print(" ".join(response))