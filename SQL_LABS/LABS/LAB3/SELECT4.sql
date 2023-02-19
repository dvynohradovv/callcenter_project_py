-- 4.Получить среднюю стоимость звонка для каждого оператора. При выводе указать имя оператора и название компании, в которой он работает. Результат отсортировать по названию компании, имени оператора и убыванию средней стоимости звонка.
SELECT
    AVG(cl.paid) AS avg_paid,
    op.first_name,
    op.last_name,
    tc.title
FROM
    operator AS op
    LEFT JOIN call_log AS cl ON cl.operator_id = op.id
    JOIN tenant_company AS tc On tc.id = op.tenant_company_id
GROUP BY
    op.first_name,
    op.last_name,
    tc.title
ORDER BY
    tc.title,
    op.first_name,
    avg_paid DESC