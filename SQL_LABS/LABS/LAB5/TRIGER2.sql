-- 3.Создать триггер, который запрещает приписывать оператору рабочее место, не принадлежащее компании, в которой работает этот оператор.
CREATE
OR REPLACE FUNCTION work_place_owner_check() RETURNS TRIGGER AS 
$$
DECLARE
    wp_company_id BIGINT;
    op_company_id BIGINT;
BEGIN
    SELECT work_place.tenant_company_id INTO wp_company_id
    FROM work_place
    WHERE work_place.id = NEW.work_place_id
    LIMIT 1;

    SELECT operator.tenant_company_id INTO op_company_id
    FROM operator
    WHERE operator.id = NEW.operator_id
    LIMIT 1;

    IF (wp_company_id != op_company_id) THEN
        RAISE EXCEPTION 'Operator tenant company is not a owner of this work place!';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER operator_to_work_place_work_place_owner_check
BEFORE INSERT OR UPDATE ON operator_to_work_place FOR EACH ROW
EXECUTE PROCEDURE work_place_owner_check ();