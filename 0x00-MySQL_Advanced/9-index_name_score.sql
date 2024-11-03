-- Creates an index `idx_name_first_score` on table `names` and
-- the first letter of `name` and the `score`.
-- Import given table dump.
-- Only the first letter of `name` AND `score` must be indexed.
DROP INDEX IF EXISTS idx_name_first_score ON names;

CREATE INDEX idx_name_first_score ON names(name(1), score);
