CREATE ROLE admin WITH SUPERUSER LOGIN PASSWORD 'your_password';

CREATE ROLE tenant_company WITH LOGIN PASSWORD 'your_password';
GRANT USAGE ON SCHEMA public TO tenant_company;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO tenant_company;
REVOKE SELECT, INSERT, UPDATE, DELETE ON public.user FROM tenant_company;

CREATE ROLE operator WITH LOGIN PASSWORD 'your_password';
GRANT USAGE ON SCHEMA public TO operator;
GRANT SELECT, INSERT, UPDATE, DELETE ON call_center_project_calllog TO operator;
