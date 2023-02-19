-- 6.Получить полную детальную информацию о звонках операторам определенной компании, совершенных за период от 5:00 до 10:00 текущего дня, для которых не указано либо сообщение звонящего, либо сообщение оператора.
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
    JOIN operator AS op ON op.id = cl.operator_id
WHERE
    op.tenant_company_id = 3
    AND cl.start_time >= CURRENT_DATE + interval '17:00:00'
    AND cl.start_time <= CURRENT_DATE + interval '22:00:00'
    AND (
        cl.caller_person_message = NULL
        OR cl.operator_message = NULL
    );