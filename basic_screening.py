#Add os openai and pandas and dotenv
import os
from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv

#Create abstracts as a dataframe.
#N.b there is an abstracts file saved to play with, but for your uses, you will need to update it.
df = pd.read_csv('abstracts.csv')
abstracts = df['Abstract'].tolist()

# Set up the OpenAI API client
# You will need to create an API client and add your key with dotenv. Also, select the model that suits you best.
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

#This is the prompt I used, but you will need to update it to match your needs.
#The {abstract} section will be filled in with the abstract of a given paper.
prompt_template = """
Please evaluate the following academic paper abstract: 
{abstract}   
For inclusion, the research must:
a) be conducted within a university context. Research done entirely outside of a university is excluded, but if it's partially in a university and partially outside, it should be included.
b) take place in an environment where English is used as a medium of instruction (EMI) or be research about English as a medium of instruction.
c) Involve primary research. In other words, reject any secondary research or opinion type articles 
Please return one of the following plus your reasoning:
'Include' if it meets the criteria.
'Exclude' if it doesn't meet the criteria.
'Unclear' if the abstract doesn't provide enough information to make a determination.
"""

# Loop through abstracts and get GPT output
output = []
for abstract in abstracts:
    try:
        response = client.chat.completions.create(
            model="o4-mini",
            messages=[{"role": "user", "content": prompt_template.format(abstract=abstract)}]
        )
        result = response.choices[0].message.content
        output.append([abstract, result])
    except Exception as e:
        output.append([abstract, f"Error: {e}"])

print (output)
df2 = pd.DataFrame(output)
print(df2)
df2.to_csv('output.csv', index=False, mode='w')
