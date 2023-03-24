#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai



openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE") 
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

question = input("Ask a question: ")
response = openai.ChatCompletion.create(
    engine="webxt-binglivesite-debug_robot-001", # engine = "deployment_name".
    # messages=[
    #     {"role": "system", "content": "You are a helpful assistant."},
    #     {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
    #     {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
    #     {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    # ]
    
    messages=[
        {"role": "system", "content": "Provide some context and/or instructions to the model."},
        {"role": "user", "content": "Example question goes here."},
        {"role": "assistant", "content": "Example answer goes here."},
        {"role": "user", "content": question}
    ]
)

#print(response)
print("The answer is: " + response['choices'][0]['message']['content'])

