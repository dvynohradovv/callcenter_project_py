-- 2.Создать функцию для отображения информации о полной детальной информации обо всех операторах указанной компании (идентификатор компании передать в качестве параметра функции): имя, пол, контактные данные, рабочее место (если нет рабочего места, вывести прочерк), общее количество принятых звонков, средняя, максимальная и минимальная стоимость звонка, средняя, максимальная и минимальная длительность звонка, доля общей стоимости принятых оператором звонков в общей стоимости звонков, принятых всеми операторами компании, в которой он работает.
-- 2.Создать функцию для отображения информации о полной детальной информации обо всех операторах указанной компании (идентификатор компании передать в качестве параметра функции): имя, пол, контактные данные, рабочее место (если нет рабочего места, вывести прочерк), общее количество принятых звонков, средняя, максимальная и минимальная стоимость звонка, средняя, максимальная и минимальная длительность звонка, доля общей стоимости принятых оператором звонков в общей стоимости звонков, принятых всеми операторами компании, в которой он работает.
CREATE OR REPLACE FUNCTION operatorsInfo (company_id BIGINT)
RETURNS TABLE (
    isdisabled BOOLEAN,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    gender GENDER,
    email VARCHAR(50),
    phone_number VARCHAR(30),
    tenant_company_id BIGINT,
	room_number VARCHAR(30),
	office_id BIGINT,
	software_version_id BIGINT,
	count_call_log BIGINT,
	avg_paid DOUBLE PRECISION,
	max_paid REAL,
	min_paid REAL,
	avg_duration NUMERIC,
	max_duration SMALLINT,
	min_duration SMALLINT,
	total DOUBLE PRECISION
) AS $$
DECLARE
    all_call_log REAL;
BEGIN
    SELECT SUM(call_log.paid) INTO all_call_log
    FROM call_log
    JOIN operator ON operator.tenant_company_id = company_id
    WHERE operator.tenant_company_id = company_id;

    RETURN QUERY (SELECT
        op.isdisabled,
        op.first_name,
        op.last_name,
        op.gender,
        op.email,
        op.phone_number,
        op.tenant_company_id,
        wp.room_number,
        wp.office_id,
        wp.software_version_id,
        COUNT(cl),
        AVG(cl.paid),
        MAX(cl.paid),
        MIN(cl.paid),
        AVG(cl.duration),
        MAX(cl.duration),
        MIN(cl.duration),
        ((100 * SUM(cl.paid)) / all_call_log)
    FROM
        operator AS op
        JOIN call_log AS cl ON cl.operator_id = op.id
        JOIN operator_to_work_place AS op_wp ON op_wp.operator_id = op.id
        JOIN work_place AS wp ON wp.id = op_wp.work_place_id
    WHERE
        op.tenant_company_id = company_id
    GROUP BY
        op.isdisabled,
        op.first_name,
        op.last_name,
        op.gender,
        op.email,
        op.phone_number,
        op.tenant_company_id,
        wp.room_number,
        wp.office_id,
        wp.software_version_id);
END;
$$ LANGUAGE plpgsql;
