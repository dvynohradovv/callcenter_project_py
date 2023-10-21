-- 3.Получить общую продолжительность звонков, принятых операторами-мужчинами из определенной компании за указанный период. При выводе указать имя оператора и название компании, в которой он работает. Результат отсортировать в алфавитном порядке по именам операторов и в порядке возрастания общей продолжительности звонков.
SELECT
    SUM(cl.duration) AS duration_sum
FROM
    call_center_project_user AS op
    LEFT JOIN call_center_project_calllog AS cl ON cl.operator_id = op.id
WHERE
    op.type = 'Operator'
    AND op.tenant_company_id = '${tenant_company_id}'
    AND cl.start_time >= '${start_time}'
    AND cl.start_time <= '${start_time}';