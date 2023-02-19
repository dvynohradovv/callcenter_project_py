-- 7.Получить полную информацию об операторах, для которых средняя стоимость звонков, принятых ими на прошлой неделе, находится в указанном диапазоне значений.
SELECT
    AVG(cl.paid) AS avg_cl_paid,
    op.first_name,
    op.last_name,
    op.username,
    op.email,
    op.gender,
    op.phone_number,
    op.last_login,
    wp.id,
    op.isdisabled,
FROM
    call_center_project_user AS op
    JOIN call_center_project_calllog AS cl ON cl.operator_id = op.id
    JOIN call_center_project_tenantcompany AS tc On tc.id = op.tenant_company_id
    JOIN call_center_project_operatortoworkplace AS op_wp On op_wp.operator_id = op.id
    JOIN call_center_project_workplace AS wp On wp.id = op_wp.work_place_id
WHERE
    (
        op.tenant_company_id = '${tenant_company_id}'
        AND op.type = 'operator'
        AND cl.start_time >= CURRENT_TIMESTAMP - interval '1 week'
        AND cl.start_time <= CURRENT_TIMESTAMP
    )
GROUP BY
    op.first_name,
    op.last_name,
    op.username,
    op.email,
    op.gender,
    op.phone_number,
    op.last_login,
    wp.id,
    op.isdisabled,
HAVING
    AVG(cl.paid) >= '${paid_from}'
    AND AVG(cl.paid) <= '${paid_to}';