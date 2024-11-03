-- This script creates a stored procedure `ComputeAverageWeightedScoreForUser` that
-- computes & store the average weighted score for a student.
-- Procedure `ComputeAverageScoreForUser` is taking 1 input:
-- user_id, a users.id value(you can assume `user_id` is linked to an existing `users`).
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weighted_sum FLOAT DEFAULT 0;
	DECLARE total_weight INT DEFAULT 0;

	SELECT SUM(c.score * p.weight) INTO weighted_sum
	FROM corrections c
	JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	SELECT SUM(p.weight) INTO total_weight
	FROM corrections c
	JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	IF total_weight > 0 THEN
		UPDATE users
		SET average_score = weighted_sum / total_weight
		WHERE id = user_id;
	ELSE
		UPDATE users
		SET average_score = 0
		WHERE id = user_id;
	END IF;
END //

DELIMITER ;
