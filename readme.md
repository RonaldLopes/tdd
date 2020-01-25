# Trabalho de TDD para a disciplina de Produtos Intensivos de Software

Projeto baseado no modelo proposto no artigo presente no site Instructables (https://www.instructables.com/id/Positioning-System/), com o foco na detecção da posição de objetos utilizando um sensor ultrassônico e aplicando testes automatizados.

## Funcionamento do modelo

A presente aplicação foi desenvolvida com a linguagem Python, seu funcionamento te o foco de processar os dados brutos recebidos de sensores ultrassônicos conectados a um arduino onde o memso se conecta a um computador com uma instância da presente aplicação ativa.

O objetivo final é processar os dados brutos e retornar para o usuário a posição de cada objeto detectado.

## Calculo do posicionamento

Para o calculo do posicionamento, utiliza-se dados de temperatura e tempo de resposta dos sensores. Onde a tempratura serve como forma de correção da velocidade do som que se altera conforme a temperatura do seu meio de propagação, que no caso considera-se como sendo o ar. A imagem a seguir ilustra melhor o calculo da posição com base na distancia obtido entre cada sensor e os objetos:

![](Docs/calculo_posicionamento.png)

## Iniciando testes automatizados

Toda a documentação referente a parte de testes automatizados encontra-se no diretório "Docs", para rodar o ambiente de testes é necessário alguns requisitos:

* Python 3.5 ou superior
* Ambiente virtual (virtualenv)
* Instalar as dependencias presentes no arquivo requirements.txt

Para instalar as dependências utilize o comando:
> pip install -r requirements.txt

Para rodar os testes, acesse o diretório "Testes" utilize o comando "green" seguido do nome do arquivo referente ao codigo de teste.

OBS: Recomenda-se o uso da IDE Pycharm para executar e manipular o código, sua integração com a parte de testes automatizados é nativa e fornece os dados em uma forma simples de visualização.


