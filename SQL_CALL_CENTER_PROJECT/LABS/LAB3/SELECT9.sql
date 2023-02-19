-- 9.Получить полную детальную информацию о компаниях, у которых номера телефонов начинаются с 555 и в номере присутствуют сочетания двух или трех четных цифр.
SELECT
    *
FROM
    tenant_company AS tc
    JOIN tenant_company_phone_number AS tc_pn ON tc_pn.tenant_company_id = tc.id
WHERE
    tc_pn.phone_number ~ '^555-\d{3}-\d{4}$'
    AND tc_pn.phone_number ~ '([02468]{2,3})';