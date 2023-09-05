import requests, json

dataset = requests.get("http://dados.recife.pe.gov.br/api/3/action/datastore_search?resource_id=7c613836-9edd-4c0f-bc72-495008dd29c3&limit=300")
dataset = dataset.json()

database = {}
listData = []
totRecursos = 0

for escola in dataset["result"]["records"]:
    database["ESCOLA"] = escola["escola"]
    database["BAIRRO"] = escola["bairro"]
    database["QTD_ALUNOS"] = escola["qtd_alunos"]
    
    if escola["sala_recurso"][0] == "N":
        escola["sala_recurso"] = "NAO"
        totRecursos += 1 
   
    database["RECURSO"] = escola["sala_recurso"]
    listData.append(database.copy())
    
with open("database.json", "w") as f:
    json.dump(listData, f, indent=2)    

print(f"Encontramos informações de {len(listData)} escolas da Rede Municipal do Recife\n{totRecursos} Não possuem estrutura/recursos para investimentos em tecnologia ou infraestrutura.\n-> JSON gerado.")