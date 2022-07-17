-- 2.Получить полную детальную информацию о звонках, совершенных в течение последних 6 месяцев, завершенных по инициативе оператора. Результат отсортировать в обратном хронологическом порядке.
SELECT
    cl.start_time,
    cl.duration,
    cl.caller_person_id,
    cl.caller_person_message,
    cl.tenant_company_phone_number_id,
    cl.operator_id,
    cl.operator_message,
    cl.disconnect_initiator,
    cl.response,
    cl.paid,
    cl.us_city_id,
    cl.additional_address
FROM
    call_log AS cl

WHERE
    cl.start_time >= CURRENT_TIMESTAMP - interval '6 months'
    AND cl.start_time <= CURRENT_TIMESTAMP
    AND cl.disconnect_initiator = 'Destination'
ORDER BY
    cl.start_time DESC;