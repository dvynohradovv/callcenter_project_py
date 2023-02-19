-- 1.Создать триггер, который автоматически подсчитывает стоимость совершенного звонка и вносит ее в соответствующую таблицу.
CREATE
OR REPLACE FUNCTION calculate_paid() RETURNS TRIGGER AS $ $ BEGIN IF TG_OP = 'INSERT' THEN NEW.paid := NEW.duration * 0.01;

RETURN NEW;

END IF;

END;

$ $ LANGUAGE plpgsql;

CREATE
OR REPLACE TRIGGER call_log_calculate_paid BEFORE
INSERT
    ON call_center_project_calllog FOR EACH ROW EXECUTE PROCEDURE calculate_paid ();