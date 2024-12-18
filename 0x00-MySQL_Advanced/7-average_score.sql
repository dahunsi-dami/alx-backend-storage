-- Creates a store procedure ComputeAverageScoreForUser that
-- computes & store average score for a student.
-- An average score can be a decimal.
-- Procedure takes in 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an exising users)
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;

	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	UPDATE users
	SET users.average_score = COALESCE(avg_score, 0)
	WHERE users.id = user_id;
END //

DELIMITER ;
