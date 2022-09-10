-- 2.Получить полную детальную информацию об операторах, которые за указанный период приняли звонки с максимальной продолжительностью.
SELECT
    DISTINCT SUM(cl.duration) AS duration_sum,
    op.isdisabled,
    op.first_name,
    op.last_name,
    op.gender,
    op.email,
    op.phone_number,
    op.tenant_company_id
FROM
    operator AS op
    LEFT JOIN call_log AS cl ON cl.operator_id = op.id
    JOIN tenant_company AS tc On tc.id = op.tenant_company_id
WHERE
    AND op.tenant_company_id = 1
    AND cl.start_time >= '2000-12-12'
    AND cl.start_time <= '2020-12-12'
GROUP BY
    op.isdisabled,
    op.first_name,
    op.last_name,
    op.gender,
    op.email,
    op.phone_number,
    op.tenant_company_id;