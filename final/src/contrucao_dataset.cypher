//Cria nós do tipo Quadrante
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/processed/quads.csv' AS line
CREATE (:Quad {id: line.ID})

CREATE INDEX FOR (n:Quad) ON (n.id)

LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/interim/adjacencias_quads.csv' AS line
MATCH (d:Quad {id: line.QUAD1})
MATCH (p:Quad {id: line.QUAD2})
CREATE (d)-[:Adjacente]->(p)



//cria os nós do tipo "Crime"
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/processed/crimes.csv' AS line
MATCH(d:Quad {id: line.QUAD})
CREATE (p:Crime {id: line.ID, ano_bo: apoc.convert.toInteger(line.ANO_BO), dataOcorrencia: line.DATA_OCORRENCIA, periodoOcorrencia: line.PERIODO_OCORRENCIA, tipoCrime: line.TIPO_CRIME})
CREATE (p)-[:Localizado]->(d)

CREATE INDEX FOR (n:Crime) ON (n.id)

//cria os nós do tipo "PostoPolicial"
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/processed/postos.csv' AS line
MATCH(d:Quad {id: line.QUAD})
CREATE (p:PostoPolicial {id: line.ID, classe: line.CLASSE, tipo: line.TIPO})
CREATE (p)-[:Localizado]->(d)

CREATE INDEX FOR (n:PostoPolicial) ON (n.id)

//cria os nós do tipo "Poste"
LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/lucasdpss/Projeto-MC536/main/final/data/processed/postes_ilum.csv' AS line
MATCH(d:Quad {id: line.QUAD})
CREATE (p:Poste {id: line.ID})
CREATE (p)-[:Localizado]->(d)

CREATE INDEX FOR (n:Poste) ON (n.id)


//Ajustar qtdPostos
MATCH (q:Quad)
SET q.qtdPostos = 0

MATCH (p:PostoPolicial)-[:Localizado]->(q:Quad)
SET q.qtdPostos = q.qtdPostos + 1

//Ajustar qtdCrimes
MATCH (q:Quad)
SET q.qtdCrimes = 0

MATCH (c:Crime)-[:Localizado]->(q:Quad)
SET q.qtdCrimes = q.qtdCrimes + 1

//Ajustar qtdPostes
MATCH (q:Quad)
SET q.qtdPostes = 0

MATCH (p:Poste)-[:Localizado]->(q:Quad)
SET q.qtdPostes = q.qtdPostes + 1


//Exportar dados
CALL apoc.export.csv.all("grafo.csv", {})
YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data
RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data


