-- 3.Получить (в одном запросе) компаний с указанием их рейтинга (места) при ранжировании по средней стоимости звонка, общему количеству операторов, количеству номеров телефонов, количеству рабочих мест, средней стоимости звонка.
SELECT
    row_number() OVER (ORDER BY AVG(cl.paid) + COUNT(DISTINCT op) + COUNT(DISTINCT tc_pn) + COUNT(DISTINCT wp) DESC) AS num,
    tc.id,
    AVG(cl.paid) AS avg_call_log_cost,
    COUNT(DISTINCT op) AS count_operators,
    COUNT(DISTINCT tc_pn) AS count_tenant_company_phone_numbers,
    COUNT(DISTINCT wp) AS count_work_places
FROM
    call_center_project_tenantcompany AS tc
    JOIN call_center_project_tenantcompanyphonenumber AS tc_pn ON tc_pn.tenant_company_id = tc.id
    JOIN call_center_project_calllog AS cl ON cl.tenant_company_phone_number_id = tc_pn.id
    JOIN call_center_project_operator AS op ON op.tenant_company_id = tc.id
    JOIN call_center_project_workplace AS wp ON wp.tenant_company_id = tc.id
GROUP BY
    tc.id;