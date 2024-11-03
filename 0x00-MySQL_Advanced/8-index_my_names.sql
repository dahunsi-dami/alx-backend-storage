-- Creates an index idx_name_first on table names & the first letter of name.
-- import given table dump.
-- Only first letter of name must be indexed.
DROP INDEX IF EXISTS idx_name_first;

CREATE INDEX idx_name_first ON names(LEFT(name, 1));
