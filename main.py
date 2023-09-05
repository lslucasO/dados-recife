import requests

dataset = requests.get("http://dados.recife.pe.gov.br/pt_BR/api/3/action/datastore_search?resource_id=87fc9349-312c-4dcb-a311-1c97365bd9f5")
dataset = dataset.json()

database = {"EMPRESA": ""}
list_data = []


for empresa in dataset["result"]["records"]:
    if empresa["nome_fantasia"] not in "" and empresa["nome_fantasia"] not in database["EMPRESA"]:
        database["EMPRESA"] = empresa["nome_fantasia"]
        database["RUA"] = empresa["nome_logradouro"]
        database["COD_LOG"] = empresa["cod_logradouro"]
        list_data.append(database.copy())
    else:
        pass

    
print(list_data)