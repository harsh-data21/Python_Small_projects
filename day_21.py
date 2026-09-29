# Gen ai Tokenization

text = " who is the pm of the India? "

import tiktoken
tokenzier =  tiktoken.encoding_for_model(model_name="gpt-4")
tokenIds = tokenzier.encode(text)
print(tokenIds)