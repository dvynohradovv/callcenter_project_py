-- Подивитися операторів із зазначенням їхнього рейтингу (місця) при ранжуванні за середньою вартістю дзвінка, 
-- середньою тривалістю дзвінка та кількістю дзвінків.
SELECT
    row_number() OVER (
        ORDER BY
            AVG(cl.paid) + AVG(cl.duration) + COUNT(DISTINCT cl) DESC
    ) AS num,
    op.id,
    op.username,
    AVG(cl.paid) AS avg_call_log_cost,
    AVG(cl.duration) AS avg_call_log_duration,
    COUNT(DISTINCT cl) AS count_call_logs,
FROM
    call_center_project_operator AS op
    JOIN call_center_project_tenantcompany AS tc ON tc.id = op.tenant_company_id
    JOIN call_center_project_tenantcompanyphonenumber AS tc_pn ON tc_pn.tenant_company_id = tc.id
    JOIN call_center_project_calllog AS cl ON cl.tenant_company_phone_number_id = tc_pn.id
WHERE
    tenant_company_id = '${tenant_company_id}'
GROUP BY
    op.id,
    op.username;