-- Creates a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and
-- store the average weighted score for all students.
-- Procedure `ComputeAverageWeightedScoreForUsers` is not taking any input.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE userId INT;
	DECLARE weighted_sum FLOAT;
	DECLARE total_weight INT;

	DECLARE user_cursor CURSOR FOR
		SELECT id FROM users;

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	OPEN user_cursor;

	read_loop: LOOP
		FETCH user_cursor INTO userId;

		IF done THEN
			LEAVE read_loop;
		END IF;

		SET weighted_sum = 0;
		SET total_weight = 0;

		SELECT SUM(c.score * p.weight) INTO weighted_sum
		FROM corrections c
		JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = userId;

		SELECT SUM(p.weight) INTO total_weight
		FROM corrections c
		JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = userId;

		IF total_weight > 0 THEN
			UPDATE users
			SET average_score = weighted_sum / total_weight
			WHERE id = userId;
		ELSE
			UPDATE users
			SET average_score = 0
			WHERE id = userId;
		END IF;
	END LOOP;

	CLOSE user_cursor;
END //

DELIMITER ;
