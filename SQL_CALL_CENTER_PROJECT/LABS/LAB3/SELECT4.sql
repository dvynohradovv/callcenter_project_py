-- 4.Получить среднюю стоимость звонка для каждого оператора. При выводе указать имя оператора и название компании, в которой он работает. Результат отсортировать по названию компании, имени оператора и убыванию средней стоимости звонка.
SELECT
    AVG(cl.paid) AS avg_paid
FROM
    call_center_project_user AS op
    LEFT JOIN call_center_project_calllog AS cl ON cl.operator_id = op.id
    JOIN call_center_project_tenantcompany AS tc On tc.id = op.tenant_company_id
WHERE
    op.tenant_company_id = '${tenant_company_id}';