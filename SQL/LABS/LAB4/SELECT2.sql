-- 3.Получить (в одном запросе) компаний с указанием их рейтинга (места) при ранжировании по средней стоимости звонка, общему количеству операторов, количеству номеров телефонов, количеству рабочих мест, средней стоимости звонка.
SELECT
    tc.id,
    AVG(cl.paid) AS avg_call_log_cost,
    COUNT(DISTINCT op) AS count_operators,
    COUNT(DISTINCT tc_pn) AS count_tenant_company_phone_numbers,
    COUNT(DISTINCT wp) AS count_work_places,
    AVG(cl.paid) + COUNT(DISTINCT op) + COUNT(DISTINCT tc_pn) + COUNT(DISTINCT wp) AS avg_total_raiting
FROM
    tenant_company AS tc
    JOIN tenant_company_phone_number AS tc_pn ON tc_pn.tenant_company_id = tc.id
    JOIN call_log AS cl ON cl.tenant_company_phone_number_id = tc_pn.id
    JOIN operator AS op ON op.tenant_company_id = tc.id
    JOIN work_place AS wp ON wp.tenant_company_id = tc.id
GROUP BY
    tc.id
ORDER BY
    avg_total_raiting DESC;