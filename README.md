![build](https://github.com/Marcelo-Scarton/DesafioMeli/actions/workflows/build.yml/badge.svg)
![deploy simian lambda](https://github.com/Marcelo-Scarton/DesafioMeli/actions/workflows/deploy_simian.yml/badge.svg)
![deploy stats lambda](https://github.com/Marcelo-Scarton/DesafioMeli/actions/workflows/deploy_stats.yml/badge.svg)
[![codecov](https://codecov.io/gh/Marcelo-Scarton/DesafioMeli/branch/main/graph/badge.svg?token=T6SOKX1JDH)](https://codecov.io/gh/Marcelo-Scarton/DesafioMeli)
# Desafio Meli Símios
## Algoritmo
O algortimo da aplicação é baseado na ideia de um caça-palavras. Antes de processar a matriz enviada, sua validade é verificada em alguns quesitos, como se a mesma é uma **matriz quadrada**, ou seja, **NxN**, se a matriz contém apenas caracteres **'A'**, **'T'**, **'C'** ou **'G'**, ressaltando que a validação é **case sensitive**, e por fim é validado também se a matriz **não está vazia**. Caso a matriz seja inválida, é retornado **400**. Sendo uma matriz válida, o algoritmo tentará achar uma **sequência de 4 caracteres iguais** nas linhas **horizontais**, **verticais** e **diagonais** da matriz. Caso pelo menos uma sequência seja encontrada, o DNA identificado é de um **símio**, retornando então **200**, caso contrário, ou seja, não seja encontrada nenhuma sequência de 4 carateres iguais, o DNA identificado é de um **humano**, retornando então **403**. Após o DNA válido ser verificado, o mesmo é armazenado no banco de dados com seu respectivo tipo, humano ou símio.
## Arquitetura
A arquitetura construída para a aplicação foi baseada em um modelo **Serverless**, fazendo uso de recursos da **AWS**. Foi criada uma **API REST** via **API Gateway**, uma **Lambda** para cada endpoint da API e o **DynamoDB** para armazenar e consultar os DNAs verificados. O modelo construído é baseado no seguinte diagrama:
![diagrama-aws](diagram.png)
## CI/CD
A implementação da **pipeline de CI/CD** foi feita a partir do **Github Actions**.
- O workflow de **CI**, chamado de **build**, é disparado toda vez que um  **Pull request** é aberto para a branch **main**. Nesse fluxo, é realizada a **instalação das dependências do projeto**, é feito o **Lint do código**, a **configuração das credenciais da AWS** para os testes, ressaltando que elas estão amazenadas nos secrets do Github, os **testes** são realizados e por fim é feita uma integração com o **[codecov](https://about.codecov.io/)**, no qual são gerados relatórios a partir do coverage resultante dos testes, além de também gerar a badge de coverage.
- O workflow de **CD** é separado em dois, **deploy simian lambda** e **deploy stats lambda**. Cada um deles é disparado apenas a partir de um **push na branch main**, oriundo do **merge de outra branch** com um **Pull request** aprovado, caso o respectivo código da lambda a qual se refere, **[simian lambda](src/simian_lambda/lambda_function.py)** ou **[stats lambda](src/stats_lambda/lambda_function.py)**, tenha sido alterado. Sendo assim, sempre que houver uma alteração no código de alguma das Lambdas, será feito o deploy e a publicação da alteração na AWS.
## Como utilizar
- **URL Base**: **https://2wak4je6ne.execute-api.us-east-1.amazonaws.com/desafio2**
- **Endpoints**: **/simian** e **/stats**
- **Header**: **x-api-key**
Apenas para que a api não ficasse totalmente exposta, foi definida uma chave que deve ser passada no header das requisições como **x-api-key**. É importante ressaltar que por conta do **cold start** das Lambdas, a primeira requisição a um dos endpoints, depois de um intervalo de 5 a 7 minutos desde a última requisição feita, irá demorar um pouco mais do que as subsequentes. Logo abaixo estão os exemplos de request e response para cada endpoint.
### POST /simian
- **curl**
```
curl -i --request POST 'https://2wak4je6ne.execute-api.us-east-1.amazonaws.com/desafio2/simian' \
--header 'x-api-key: hqQD4DjAlNPjweDuceV46vmubvFToW52DSarcvh7' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dna": ["AAAA", "TTTT", "CCCC", "GGGG"]
}'
```
**Significado do código de status da resposta HTTP**
- **200**: O DNA é de um **Símio**.
- **403**: O DNA é de um **Humano**.
- **400**: O DNA é inválido.