//Cria nós do tipo Pr
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/processed/quads.csv' AS line
CREATE (:Pr {id: line.ID})

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/interim/adjacencias_quads.csv' AS line
MATCH (d:Pr {id: line.QUAD1})
MATCH (p:Pr {id: line.QUAD2})
CREATE (d)-[:Adjacente]->(p)



//Projeta os nós do tipo "Crime" em "Pr" 
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/processed/crimes.csv' AS line
MATCH(d:Pr {id: line.QUAD})
WHERE line.TIPO_CRIME = "HOMICÍDIO"
CREATE (p:Pr {id: line.ID})
CREATE (p)-[:Adjacente]->(d)
CREATE (d)-[:Adjacente]->(p)

CREATE INDEX FOR (n:Pr) ON (n.id)


