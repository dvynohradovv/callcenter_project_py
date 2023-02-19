ALTER TABLE
    call_center_project_office
ADD
    CONSTRAINT fk_office_address FOREIGN KEY (address_id) REFERENCES call_center_project_address (id) ON UPDATE CASCADE ON DELETE
SET
    NULL;

ALTER TABLE
    call_center_project_softwareversion
ADD
    CONSTRAINT fk_software_version_software FOREIGN KEY (software_id) REFERENCES call_center_project_software (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    call_center_project_workplace
ADD
    CONSTRAINT fk_work_place_office FOREIGN KEY (office_id) REFERENCES call_center_project_office (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_work_place_software_version FOREIGN KEY (software_version_id) REFERENCES call_center_project_softwareversion (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_work_place_tenant_company FOREIGN KEY (tenant_company_id) REFERENCES call_center_project_tenantcompany (id) ON UPDATE CASCADE ON DELETE
SET
    NULL;

ALTER TABLE
    call_center_project_tenantcompanyphonenumber
ADD
    CONSTRAINT fk_tenant_company_phone_number_tenant_company FOREIGN KEY (tenant_company_id) REFERENCES call_center_project_tenantcompany (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    call_center_project_user
ADD
    CONSTRAINT fk_user_tenant_company FOREIGN KEY (tenant_company_id) REFERENCES call_center_project_tenantcompany (id) ON UPDATE
SET
    NULL ON DELETE
SET
    NULL;

ALTER TABLE
    call_center_project_operatortoworkplace
ADD
    CONSTRAINT fk_operator_to_work_place_operator FOREIGN KEY (operator_id) REFERENCES call_center_project_user (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_operator_to_work_place_work_place FOREIGN KEY (work_place_id) REFERENCES call_center_project_workplace (id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE
    call_center_project_calllog
ADD
    CONSTRAINT fk_call_log_caller_person FOREIGN KEY (caller_person_id) REFERENCES call_center_project_callerperson (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_call_log_operator FOREIGN KEY (operator_id) REFERENCES call_center_project_user (id) ON UPDATE
SET
    NULL ON DELETE
SET
    NULL,
ADD
    CONSTRAINT fk_call_log_tenant_company_phone_number FOREIGN KEY (tenant_company_phone_number_id) REFERENCES call_center_project_tenantcompanyphonenumber (id) ON UPDATE CASCADE ON DELETE CASCADE,
ADD
    CONSTRAINT fk_call_log_address FOREIGN KEY (address_id) REFERENCES call_center_project_address(id) ON UPDATE
SET
    NULL ON DELETE
SET
    NULL;