-- 1.Создать представление для отображения полной информации об операторах (с указанием названий компаний, в которых они работают), которые в текущий момент не имеют рабочего места.
DROP VIEW IF EXISTS operator_without_work_place;

CREATE VIEW operator_without_work_place AS
SELECT
    op.first_name,
    op.last_name,
    op.gender,
    op.email,
    op.phone_number,
    op.tenant_company_id,
    tc.title,
    op_wp.work_place_id
FROM
    operator AS op
    JOIN tenant_company AS tc ON tc.id = op.tenant_company_id
    LEFT JOIN operator_to_work_place AS op_wp ON op_wp.operator_id = op.id
WHERE
    op_wp.work_place_id IS NULL;

SELECT
    *
FROM
    operator_without_work_place;