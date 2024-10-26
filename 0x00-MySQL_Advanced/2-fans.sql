-- Write script to rank country origins of bands,
-- ordered by the number of (non-unique) fans with these requirements:
-- import given table dump (URL given).
-- column names must be: origin and nb_fans
-- The script can be executed on any database.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
