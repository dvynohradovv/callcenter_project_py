-- 5.Получить информацию об общей стоимости и количестве звонков в офисы, находящиеся в трех указанных городах.
SELECT
    SUM(c_l.paid) AS callogs_sum_paid,
    COUNT(*) AS callogs_quantity
FROM
    call_log AS c_l
    JOIN operator_to_work_place AS op_wp ON op_wp.operator_id = c_l.operator_id
    JOIN work_place AS wp ON wp.id = op_wp.work_place_id
    JOIN office AS of ON of.id = wp.office_id
    JOIN us_address AS us_a ON us_a.id = of.us_address_id
    JOIN us_city AS us_c ON us_c.id = us_a.us_city_id
WHERE
    us_a.us_city_id = 379
    OR us_a.us_city_id = 168
    OR us_a.us_city_id = 1;