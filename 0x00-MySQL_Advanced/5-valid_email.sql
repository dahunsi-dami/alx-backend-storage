-- Creates a trigger to rest valid_email attribute+
-- only when the email has been changed.
DELIMITER //

CREATE TRIGGER reset_valid_email_before_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;

//

DELIMITER ;