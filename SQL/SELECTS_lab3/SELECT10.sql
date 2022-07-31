-- 10.Получить полную детальную информацию о рабочих местах (с указанием полного адреса, названий и версий ПО, названий компаний и имен операторов) для офисов, находящихся в указанном штате.
SELECT
    wp.room_number,
    swv.soft_version,
    sw.software_name,
    op.first_name,
    op.last_name,
    us_s.title,
    us_c.title,
    us_a.street,
    us_a.house,
    us_a.additional_info,
    of.flat
FROM
    work_place AS wp -- Tenant Company JOIN
    JOIN tenant_company AS tc ON tc.id = wp.tenant_company_id -- Software Join
    JOIN software_version AS swv ON swv.id = wp.software_version_id
    JOIN software AS sw ON sw.id = swv.software_id -- Operator Join
    JOIN operator_to_work_place AS op_wp ON op_wp.work_place_id = wp.id
    JOIN operator AS op ON op.id = op_wp.operator_id -- Office Join
    JOIN office AS of ON of.id = wp.office_id -- US address Join
    JOIN us_address AS us_a ON us_a.id = of.us_address_id
    JOIN us_city AS us_c ON us_c.id = us_a.us_city_id
    JOIN us_state AS us_s ON us_s.id = us_c.us_state_id
WHERE
    us_s.id = 8;