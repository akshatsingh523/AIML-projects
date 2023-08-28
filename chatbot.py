import os
import streamlit as st
from langchain import HuggingFaceHub,PromptTemplate,LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN']='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'

model_id='tiiuae/falcon-7b-instruct'

falcom_llm=HuggingFaceHub(
    repo_id=model_id,
    model_kwargs={"temperature":0.8,"max_new_tokens":2000}
)

template='''You are an AI assistant that provides helful answers to user queries.
{question}
'''

prompt=PromptTemplate(template=template,input_variables=['question'])

falcon_chain=LLMChain(llm=falcom_llm,prompt=prompt,verbose=True)

print(falcon_chain.run("What are the colors in the Rainbow?"))


st.title("Falcon AI Assistant")

user_question = st.text_input("Enter your question:")
generate_button = st.button("Generate Answer")

if generate_button:
    generated_answer = falcon_chain.run(user_question)
    st.write("Generated Answer:")
    st.write(generated_answer)



