import requests
import pandas as pd

def get_data(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(endpoint, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data for CEP {cep}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    


users_path = "01-bronze-raw/users.csv"
users_df = pd.read_csv(users_path)
# print(users_df.head())


cep_list = users_df['cep'].tolist()

cep_info_list = []

for cep in cep_list:
    cep_info = get_data(cep.replace("-", ""))
    cep_info_list.append(cep_info)

cep_info_df = pd.DataFrame(cep_info_list)

cep_info_df.to_csv("01-bronze-raw/cep_info.csv", index=False)
