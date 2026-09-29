# Gen ai Tokenization

text = " who is the pm of the India? "

import tiktoken
tokenzier =  tiktoken.encoding_for_model(model_name="gpt-4")
# Encode 
tokenIds = tokenzier.encode(text)

#Decode 
result = tokenzier.decode(tokenIds)
print(result)
print(tokenIds)
