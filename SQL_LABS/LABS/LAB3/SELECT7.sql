-- 7.Получить полную информацию об операторах, для которых средняя стоимость звонков, принятых ими на прошлой неделе, находится в указанном диапазоне значений.
SELECT
    AVG(cl.paid) AS avg_cl_paid,
    op.isdisabled,
    op.first_name,
    op.last_name,
    op.gender,
    op.email,
    op.phone_number,
    op.tenant_company_id
FROM
    operator AS op
    JOIN call_log AS cl ON cl.operator_id = op.id
WHERE
    (
        cl.start_time >= CURRENT_TIMESTAMP - interval '1 week'
        AND cl.start_time <= CURRENT_TIMESTAMP
    )
GROUP BY
    op.isdisabled,
    op.first_name,
    op.last_name,
    op.gender,
    op.email,
    op.phone_number,
    op.tenant_company_id
HAVING
    AVG(cl.paid) >= 1
    AND AVG(cl.paid) <= 1000