-- Lists all bands w/ Glam rock as their main style,
-- ranked by their longevity:
-- import given table dump (URL given).
-- column names must be: band_name & lifespan (in years until 2022-
-- please, use 2022 instead of YEAR(CURDATE()))
-- You should use attributes formed & split for computing the lifespan.
-- The script can be executed on any database.
SELECT
	band_name,
	CASE
		WHEN split IS NULL THEN (2022 - formed)
		ELSE (split - formed)
	END AS lifespan
FROM
	metal_bands
WHERE
	style LIKE '%Glam rock%'
ORDER BY
	lifespan DESC;
