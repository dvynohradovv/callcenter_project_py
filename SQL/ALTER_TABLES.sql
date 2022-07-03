ALTER TABLE
    us_city
ADD
    CONSTRAINT fk_us_city_us_state FOREIGN KEY (us_state_id) REFERENCES us_state (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    us_address
ADD
    CONSTRAINT fk_us_address_us_city FOREIGN KEY (us_city_id) REFERENCES us_city (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    office
ADD
    CONSTRAINT fk_office_us_address FOREIGN KEY (us_address_id) REFERENCES us_address (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    software_version
ADD
    CONSTRAINT fk_software_version_software FOREIGN KEY (software_id) REFERENCES software (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    work_place
ADD
    CONSTRAINT fk_work_place_office FOREIGN KEY (office_id) REFERENCES office (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_work_place_software_version FOREIGN KEY (software_version_id) REFERENCES software_version (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_work_place_tenant_company FOREIGN KEY (tenant_company_id) REFERENCES tenant_company (id) ON UPDATE CASCADE ON DELETE
SET
    NULL;

ALTER TABLE
    tenant_company_phone_number
ADD
    CONSTRAINT fk_tenant_company_phone_number_tenant_company FOREIGN KEY (tenant_company_id) REFERENCES tenant_company (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    operator
ADD
    CONSTRAINT fk_operator_tenant_company FOREIGN KEY (tenant_company_id) REFERENCES tenant_company (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    operator_to_work_place
ADD
    CONSTRAINT fk_operator_to_work_place_operator FOREIGN KEY (operator_id) REFERENCES operator (id) ON UPDATE CASCADE ON DELETE CASCADE,

ADD
    CONSTRAINT fk_operator_to_work_place_work_place FOREIGN KEY (work_place_id) REFERENCES tenant_company (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    call_log
ADD
    CONSTRAINT fk_call_log_caller_person FOREIGN KEY (caller_person_id) REFERENCES caller_person (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_call_log_operator FOREIGN KEY (operator_id) REFERENCES operator (id) ON UPDATE CASCADE ON DELETE
SET
    NULL,
ADD
    CONSTRAINT fk_call_log_tenant_company_phone_number FOREIGN KEY (tenant_company_phone_number_id) REFERENCES tenant_company_phone_number (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_call_log_us_city FOREIGN KEY (us_city_id) REFERENCES us_city(id) ON UPDATE CASCADE ON DELETE CASCADE;