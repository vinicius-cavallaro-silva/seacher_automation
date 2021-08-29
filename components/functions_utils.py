import json

def create_json(resultados):
    #path_file_json =r"C:\Users\Usuário\Desktop\git_vini\searcher_web_sites\results.json"
    path_file_json ="..\\components\\results.json"

    print('Creating the File...')
    resultados_json = json.dumps(resultados)
    arquivo = open(path_file_json, "w")
    arquivo.write(resultados_json)
    arquivo.close()

if __name__ == '__main__':
    create_json(['abobrinha', 'Abacate'])