-- 8.Получить имена операторов, которые как минимум 2 раза принимали звонки на разные номера телефонов от одних и тех же персон.
SELECT
    op.first_name,
    op.last_name
FROM
    operator AS op
    JOIN call_log AS cl ON cl.operator_id = op.id
    JOIN caller_person AS cp ON cp.id = cl.caller_person_id
    JOIN tenant_company_phone_number AS tc_pn ON
WHERE
    
