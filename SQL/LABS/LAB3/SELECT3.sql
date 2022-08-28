-- 3.Получить общую продолжительность звонков, принятых операторами-мужчинами из определенной компании за указанный период. При выводе указать имя оператора и название компании, в которой он работает. Результат отсортировать в алфавитном порядке по именам операторов и в порядке возрастания общей продолжительности звонков.
SELECT
    SUM(cl.duration) AS duration_sum,
    op.first_name,
    op.last_name,
    tc.title
FROM
    operator AS op
    LEFT JOIN call_log AS cl ON cl.operator_id = op.id
    JOIN tenant_company AS tc On tc.id = op.tenant_company_id
WHERE
    op.gender = 'Male'
    AND op.tenant_company_id = 1
    AND cl.start_time >= '2000-12-12'
    AND cl.start_time <= '2020-12-12'
GROUP BY
    op.first_name,
    op.last_name,
    tc.title
ORDER BY
    op.first_name,
    duration_sum;