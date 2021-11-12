# Projeto "Mapeamento da Criminalidade em SP"

# Equipe `Os Delegados` - `SSPD`
* Antonio Gabriel da Silva Fernandes - 231551
* Bruno Henrique Emidio Leite - 214017
* Lucas de Paula Soares - 201867

# Estrutura de Arquivos e Pastas

~~~
├── README.md  <- arquivo apresentando a proposta
│
├── data
│   ├── external       <- dados de terceiros em formato usado para entrada na transformação
│   ├── interim        <- dados intermediários, e.g., resultado de transformação
│   ├── processed      <- dados finais usados para a publicação
│   └── raw            <- dados originais sem modificações
│
├── notebooks          <- Jupyter notebooks ou equivalentes
│
├── slides             <- arquivo de slides em formato PDF
│
├── src                <- fonte em linguagem de programação  (e.g., Python)
│   └── README.md      <- instruções básicas de instalação/execução
│
└── assets             <- mídias usadas no projeto
~~~

## Resumo do Projeto
> O projeto visa agregar dados da Secretaria de Segurança Pública de São Paulo e da Prefeitura de São Paulo referentes a crimes ocorridos na cidade, iluminação pública e posição de postos policiais, com o objetivo de tornar possível a análise da correlação entre a ocorrência de crimes e a infraestrutura da cidade.

## Slides da Apresentação
> Link para apresentação da prévia: [apresentação](slides/previa_apresentacao.pdf)

## Modelo Conceitual Preliminar

> Coloque aqui a imagem do modelo conceitual preliminar em ER ou UML, como o exemplo a seguir:
> ![Modelo Conceitual](assets/modelo_conceitual.png)

## Modelos Lógicos Preliminares

> Modelo lógico relacional preliminar
~~~
Crimes(_ID_, DATA_OCORRENCIA, PERIODO_OCORRENCIA, HORA_OCORRENCIA, ANO_BO, LAT, LON, TIPO_CRIME, QUAD)
  TIPO_CRIME chave estrangeira -> Tipos_crimes(NOME)
  QUAD chave estrangeira -> Quads(ID)
Tipos_Crimes(_NOME_)
Quads(_ID_, LON_MIN, LON_MAX, LAT_MIN, LAT_MAX)
Postes_ilum(_ID_, LAT, LON, QUAD)
  QUAD chave estrangeira -> Quads(ID)
Postos(_ID_, CLASSE, TIPO, LAT, LON, QUAD)
  QUAD chave estrangeira -> Quads(ID)

~~~
