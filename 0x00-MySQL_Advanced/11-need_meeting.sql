-- Create a view `need_meeting` to list all students that have a score
-- under 80 (strict) and no `last_meeting` or more than 1 month.
-- The view `need_meeting` should return all students name when:
-- they score are under (strict) to 80
-- AND no `last_meeting` date OR more than a month.
CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
	AND (last_meeting IS NULL OR last_meeting < CURDATE() - INTERVAL 1 MONTH);
