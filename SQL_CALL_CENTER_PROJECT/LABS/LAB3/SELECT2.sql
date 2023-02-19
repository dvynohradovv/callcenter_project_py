-- 2.Получить полную детальную информацию о звонках, совершенных в течение последних 6 месяцев, завершенных по инициативе оператора. Результат отсортировать в обратном хронологическом порядке.
SELECT
    cl.start_time,
    cl.duration,
    cp.first_name,
    cp.last_name,
    cp.phone_number,
    cl.caller_person_message,
    tc_pn.phone_number,
    op.username,
    op.first_name,
    op.last_name,
    cl.operator_message,
    cl.disconnect_initiator,
    cl.response,
    cl.paid
FROM
    call_center_project_calllog AS cl
    LEFT JOIN call_center_project_user AS op ON op.id = cl.operator_id
    LEFT JOIN call_center_project_callerperson AS cp ON cp.id = cl.caller_person_id
    LEFT JOIN call_center_project_tenantcompanyphonenumber AS tc_pn ON tc_pn.id = cl.tenant_company_phone_number_id
WHERE
    op.tenant_company_id = '${tenant_company_id}'
    AND cl.start_time >= CURRENT_TIMESTAMP - interval '6 months'
    AND cl.start_time <= CURRENT_TIMESTAMP
    AND cl.disconnect_initiator = 'Destination'
ORDER BY
    cl.start_time DESC;