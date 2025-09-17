# 🛠️ Projeto de Engenharia de Dados – Pipeline Bronze → Silver → Gold

Este projeto implementa um **pipeline de engenharia de dados** completo usando Python, Pandas, Postgres e Docker.  
Ele coleta dados crus (Bronze), normaliza e salva em formato eficiente (Silver), carrega em banco de dados e visualiza dados enriquecidos (Gold).


## 🏗️ Pipeline de Dados

1. **Bronze**  
   - Pasta `01-bronze-raw/` guarda os dados originais (CSV ou JSON).  
   - `get_data.py` busca informações adicionais na API ViaCEP usando CEP dos usuários.

2. **Silver**  
   - `normalize_data.py` limpa dados, converte listas para texto, remove duplicados e salva em formato **Parquet** na pasta `02-silver-validated`.

3. **Postgres (Carga)**  
   - `App.py` lê arquivos Parquet e grava no banco Postgres usando `db.py`.

4. **Gold**  
   - Consultas SQL na pasta `03-gold-enriched/`.  
   - `data-view.ipynb` roda SQL, analisa e plota gráficos.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**  
- **Pandas** para manipulação de dados  
- **psycopg2** para comunicação com Postgres  
- **SQLAlchemy** para consultas SQL no notebook  
- **Docker + Docker Compose** para subir Postgres  
- **Matplotlib** para visualizações  

---

## 🚀 Como Executar

### 1️⃣ Subir o Postgres com Docker
```bash
docker-compose up -d
Isso criará um container Postgres com usuário e senha postgres/postgres na porta 5432.

2️⃣ Coletar Dados (Bronze)
bash
Copiar código
python get_data.py
Isso lê users.csv e consulta API ViaCEP, gerando cep_info.csv em 01-bronze-raw.

3️⃣ Normalizar Dados (Silver)
bash
Copiar código
python normalize_data.py
Isso gera arquivos .parquet na pasta 02-silver-validated.

4️⃣ Carregar Dados no Postgres
bash
Copiar código
python App.py
Isso cria tabelas no Postgres e insere dados normalizados.

5️⃣ Analisar Dados (Gold)
Abra o notebook data-view.ipynb e execute para visualizar gráficos.

🗄️ Configuração do Banco de Dados
O arquivo docker-compose.yml cria um container Postgres com:

User: postgres

Password: postgres

Database: postgres

Porta: 5432

Volumes são persistentes (pgdata) para não perder dados.

📊 Visualização dos Dados
O notebook data-view.ipynb lê uma consulta SQL em 03-gold-enriched/query.sql, gera um DataFrame Pandas e plota gráficos como distribuição por ano de nascimento.

📂 Estrutura Bronze → Silver → Gold
mermaid
Copiar código
flowchart LR
A[01-bronze-raw] -->|normalize_data.py| B[02-silver-validated]
B -->|App.py + db.py| C[(Postgres DB)]
C -->|query.sql| D[03-gold-enriched / data-view.ipynb]
🔑 Principais Arquivos
get_data.py → coleta dados externos (ViaCEP)

normalize_data.py → normaliza arquivos crus

App.py → carrega dados no Postgres

db.py → abstrai operações SQL

data-view.ipynb → análises e gráficos

docker-compose.yml → sobe Postgres via Docker

📝 Licença
Este projeto é para fins educacionais e pode ser adaptado livremente.
