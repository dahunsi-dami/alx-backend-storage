-- Creates a function `SafeDiv` that divides & returns the first by
-- the 2nd number or returns 0 if 2nd number is equal to 0.
-- You must creates a function.
-- The function `SafeDiv` takes 2 arguments:
-- a, INT
-- b, INT
-- And returns a / b or 0 if b == 0
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF;
END //

DELIMITER ;
