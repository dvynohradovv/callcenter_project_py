-- 2.Получить полную детальную информацию об операторах, которые за указанный период приняли звонки с максимальной продолжительностью.
SELECT
    MAX(cl.duration) AS max_duration,
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
    op.type = 'Operator'
    op.tenant_company_id = '${tenant_company_id}'
    cl.start_time >= '${start_time}'
    AND cl.start_time <= '${start_time}'
GROUP BY
    op.first_name,
    op.last_name,
    op.username,
    op.email,
    op.gender,
    op.phone_number,
    op.last_login,
    wp.id,
    op.isdisabled;