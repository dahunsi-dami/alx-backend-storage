-- Creates a store procedure ComputeAverageScoreForUser that
-- computes & store average score for a student.
-- An average score can be a decimal.
-- Procedure takes in 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an exising users)
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score FLOAT;

	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = user_id;

	UPDATE users
	SET average_score = avg_score
	WHERE id = user_id;
END //
DELIMITER ;
