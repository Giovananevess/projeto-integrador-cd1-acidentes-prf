-- Total de acidentes
SELECT COUNT(*) AS total_acidentes
FROM acidentes_prf;

-- Total de mortos e feridos
SELECT
    SUM(mortos) AS total_mortos,
    SUM(feridos) AS total_feridos
FROM acidentes_prf;

-- Top 10 causas de acidentes
SELECT
    causa_acidente,
    COUNT(*) AS total
FROM acidentes_prf
GROUP BY causa_acidente
ORDER BY total DESC
LIMIT 10;

-- Top 10 rodovias
SELECT
    br,
    COUNT(*) AS total
FROM acidentes_prf
GROUP BY br
ORDER BY total DESC
LIMIT 10;

-- Acidentes por UF
SELECT
    uf,
    COUNT(*) AS total
FROM acidentes_prf
GROUP BY uf
ORDER BY total DESC;

-- Acidentes por fase do dia
SELECT
    fase_dia,
    COUNT(*) AS total
FROM acidentes_prf
GROUP BY fase_dia
ORDER BY total DESC;