//Queries

//50 primeiras regioes com mais crimes no total
MATCH (q:Quad)
WITH q
ORDER BY q.qtdCrimes DESC
LIMIT 50
RETURN q


// 50 regioes mais perigosas a noite 
MATCH (q:Quad)
SET q.qtdCrimesNoite = 0

MATCH (c:Crime {periodoOcorrencia: "A NOITE"})-[:Localizado]->(q:Quad)
SET q.qtdCrimesNoite = q.qtdCrimesNoite + 1

MATCH (q:Quad)
WITH q
ORDER BY q.qtdCrimesNoite DESC
LIMIT 50
RETURN q

