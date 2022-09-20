import requests
import json
from requests.auth import HTTPDigestAuth
import pandas as pd

#Configuração
url = "https://imunizacao-es.saude.gov.br/desc-imunizacao/_search"
params = {'scroll':"2m", "size": "10000"}

user = "imunizacao_public"
password = "qlto5t&7r_@+#Tlstigi"

pesquisa_cidade = {
    "codigo" : "355060", #estabelecimento_municipio_codigo
    "cidade" : "SAO ROQUE", #estabelecimento_municipio_nome
    "uf" : "SP", #estabelecimento_uf
    "ibge" : "355060" #paciente_endereco_coIbgeMunicipio
}

body ={
    "query":{
        "match":{
            "estabelecimento_municipio_nome": pesquisa_cidade["cidade"],
        }
    }
}

#Requisição GET
res = requests.get(url, json=body, params = params, auth=(user, password))

#Status da Requisicao
print(res)
#Conteúdo do retorno
#print(res.text)
#print(res.content)

#Tratando o retorno e convertendo em  um objeto JSON
res_obj =  json.loads(res.text)
data = json.dumps(res_obj)

#Criando um DataFrame para manipular o arranjo com formato JSON
df = pd.read_json(data)

#Criando um DataFrame para manipular o arranjo com formato OBJETO
#df = pd.DataFrame(res_obj)

#print(df)

#Pesquisa no DF o indice
#print(df.loc["hits"])

#imprime o DataFrame inteiro
#print(df.to_string()) 

# se não especificar a quantidade o método retorna 5 linhas
print(df.head(10))

# Imprime todas os indices
for x in df.index:
  print(x)
print('\n')
# Imprime todas as colunas
for x in df.columns:
  print(x)

#nova_df = (df.loc["hits","hits"])
#nova_df.to_frame()

#print(nova_df.head(10))
