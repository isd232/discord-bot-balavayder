# import openai
#
#
# def chatgpt_response(prompt):
#     global prompt_response
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=1,
#         max_tokens=100
#     )
#     response_dict = response.get("choice")
#     if response_dict and len(response_dict) > 0:
#         prompt_response = response_dict[0]["text"]
#     return prompt_response