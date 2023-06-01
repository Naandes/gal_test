<h1 align="center">Teste Técnico para Analista de BI</h1>

### Desafio

O desafio consiste em extrair um conjunto de informações sobre filmes, armazenar, modelar 2 kpis a sua escolha e montar uma visualização para os mesmos.

Algumas informações importantes
- A Api da The movieDB está descrita em: https://developers.themoviedb.org
- Para iniciar será necessário criar uma conta gratuita e obter um token para a mesma, como o descrito em https://developers.themoviedb.org/3/getting-started/introduction
- O principal endpoint para obter os dados para esse desafio é o https://developers.themoviedb.org/3/movies/get-movie-details, use outros se julgar necessário, Devem ser obtidos ao mesmo dados de 100 filmes
- O desafio deve ser feito em Python
- O armazenamento dos dados pode ser feito em arquivo ou banco de dados (Mysql Postgrs, Mongo), caso opte por um banco de dados, deve ser enviado anexo o acesso ao mesmo ou um script para criação do mesmo 
- Deve haver uma rotina que processa os dados obtidos, calcula os kpis e os armazena em um modelo de dados.
- A visualização pode ser da forma como preferir, usando alguma biblioteca do python ou algum software gratuito, a forma de visualizar o dado é mais importante do que a ferramenta utilizada
- Não será fornecida infraestrutura para esse desafio, o intuito do desafio é entender como executaria a atividade e não avaliar a infraestrutura utilizada, caso decida usar alguma infraestrutura terceira, escolha uma gratuita

## Projeto

### Rotina de execução
A rotina de execução está configurada por padrão acontecer a cada 2 dias, sendo configurável no arquivo main.py, modificando a linha 14 com a rotina que desejar.


### Banco de Dados
O banco de dados utilizado foi o postgreSQL, criando uma instância do mesmo no Google Cloud Plataform (GCP), as credenciais de acesso são:

```shell
    IP público: 34.172.41.112
    Nome da conexão: crypto-airlock-388421:us-central1:postgres
    user: postgres
    password: admin
    database: movies
```

### Extração dos Dados
Os dados foram obtidos por meio de uma API do TMDB, que permitiu a coleta dos filmes mais populares. Em seguida, foram coletados os detalhes desses filmes anteriormente armazenados. A quantidade de filmes pode ser modificada no arquivo extract.py, na linha 46, na função get_movies. O resultado é um arquivo CSV (tmdb_movies1.csv) e as informações coletadas são enviadas para o banco de dados que alimenta a visualização online do Looker Studio.

#### Iniciar a extração
1. Instale as dependências do projeto utilizando o seguinte comando abaixo:
```shell
    pip install -r requirements.txt
```
2. Criar um arquivo .env com a variável de ambiente:
```shell
    TOKEN=TOKEN-OBTIDO-NO-THE-MOVIE-DB
    HOST=YOUR-HOST-HERE
    DATABASE=YOUR-DATABASE-HERE
    USER=YOUR-USER-HERE
    PASSWORD=YOUR-PASSWORD-HERE
```
3. Execute o projeto utilizando o seguinte comando abaixo:
```shell
    python main.py
```
### Tratamento dos Dados
Durante o tratamento dos dados, foram considerados possíveis valores nulos e substituídos por valores padrão, dependendo do tipo de coluna. Para colunas numéricas, foi utilizado o valor 0; para colunas de texto, foi utilizado o termo "Nulo"; e para colunas de data, foi utilizado o valor 01/01/2015.

### Carregamento dos Dados
O carregamento dos dados é realizado por meio de uma conexão com um banco de dados PostgreSQL, que foi criado especificamente para o desafio e hospedado na plataforma Google Cloud. Esse banco de dados foi modelado com os dados obtidos da API. Quando os dados são coletados, eles são enviados para o banco de dados, caso o filme ainda não esteja registrado nele.

### Filtros
Os filtros contidos no relatório são de data de lançamento, o idioma do filme e a nota máxima dada ao filme.

### KPI 1
Esta KPI mostra os filmes selecionados de forma decrescente por popularidade, contendo voto máximo e a data de lançamento.

### KPI 2
Esta KPI informa a quantidade de filmes que foram lançados por semana.

### KPI 3
Esta KPI informa a quantidade de idiomas totais contidos em todos os filmes.

### KPI 4
Esta KPI informa a quantidade de votos totais dos filmes.

### KPI 5
Esta KPI informa a média da popularidade dos filmes.

### KPI 5
Esta KPI informa a quantidade da popularidade total dos filmes.

### Visualização dos Dados
[Google Data Studio](https://lookerstudio.google.com/reporting/f839e7c3-d133-4882-8ed5-d088aa488d54)

------------

Desenvolvido por [Marcos Fernandes](https://www.linkedin.com/in/marcos-victor-fernandes/)
