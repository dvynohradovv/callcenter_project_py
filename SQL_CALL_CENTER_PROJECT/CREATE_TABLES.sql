-- Location models
DROP TABLE IF EXISTS call_center_project_address CASCADE;

CREATE TABLE call_center_project_address (
    id BIGSERIAL PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    zip_code VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    street VARCHAR(100) NOT NULL,
    building VARCHAR(100) NOT NULL,
    additional_info VARCHAR(200) NOT NULL
);

-- Equipment models
DROP TABLE IF EXISTS call_center_project_office CASCADE;

CREATE TABLE call_center_project_office (
    id BIGSERIAL PRIMARY KEY,
    address_id BIGINT NULL,
    title VARCHAR(100),
    UNIQUE(address_id, title)
);

DROP TABLE IF EXISTS call_center_project_software CASCADE;

CREATE TABLE call_center_project_software (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    UNIQUE(title)
);

DROP TABLE IF EXISTS call_center_project_softwareversion CASCADE;

CREATE TABLE call_center_project_softwareversion (
    id BIGSERIAL PRIMARY KEY,
    version VARCHAR(100) NOT NULL,
    software_id BIGINT NOT NULL,
    UNIQUE(version, software_id)
);

DROP TABLE IF EXISTS call_center_project_workplace CASCADE;

CREATE TABLE call_center_project_workplace (
    id BIGSERIAL PRIMARY KEY,
    room_number VARCHAR(100) NOT NULL,
    office_id BIGINT NOT NULL,
    software_version_id BIGINT NOT NULL,
    tenant_company_id BIGINT NULL,
    UNIQUE(room_number, office_id)
);

-- Tenant company models
DROP TABLE IF EXISTS call_center_project_tenantcompany CASCADE;

CREATE TABLE call_center_project_tenantcompany (
    id BIGSERIAL PRIMARY KEY,
    isdisabled BOOLEAN DEFAULT false NULL,
    title VARCHAR(100) NOT NULL,
    category BUSINESS_CATEGORY DEFAULT 'Unknown' NULL,
    price_per_operator REAL CHECK(price_per_operator > 0.0) NOT NULL,
    UNIQUE(title)
);

DROP TABLE IF EXISTS call_center_project_tenantcompanyphonenumber CASCADE;

CREATE TABLE call_center_project_tenantcompanyphonenumber (
    id BIGSERIAL PRIMARY KEY,
    phone_number VARCHAR(100) NOT NULL,
    tenant_company_id BIGINT,
    description TEXT NOT NULL,
    isdisabled BOOLEAN DEFAULT false NULL,
    UNIQUE(phone_number)
);

-- Persons model
DROP TABLE IF EXISTS call_center_project_callerperson CASCADE;

CREATE TABLE call_center_project_callerperson (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(100) NULL,
    last_name VARCHAR(100) NULL,
    phone_number VARCHAR(100) NOT NULL,
    gender GENDER DEFAULT 'Unknown' NULL,
    email VARCHAR(100) NULL,
    UNIQUE(phone_number, email)
);

DROP TABLE IF EXISTS call_center_project_user CASCADE;

CREATE TABLE call_center_project_user (
    id BIGSERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP,
    is_superuser boolean NOT NULL,
    username VARCHAR(150) NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP NOT NULL,
    type VARCHAR(100) NOT NULL,
    isdisabled BOOLEAN NOT NULL,
    email VARCHAR(254) NOT NULL,
    gender VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100),
    tenant_company_id BIGINT,
    UNIQUE(username),
    UNIQUE(email)
);

DROP TABLE IF EXISTS call_center_project_operatortoworkplace CASCADE;

CREATE TABLE call_center_project_operatortoworkplace(
    work_place_id BIGINT NOT NULL,
    operator_id BIGINT NOT NULL,
    UNIQUE(operator_id),
    UNIQUE(work_place_id)
);

-- Call_log
DROP TABLE IF EXISTS call_center_project_calllog CASCADE;

CREATE TABLE call_center_project_calllog (
    id BIGSERIAL PRIMARY KEY,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NULL,
    duration smallint CHECK(duration > 0) NOT NULL,
    caller_person_id BIGINT NOT NULL,
    caller_person_message TEXT NULL,
    tenant_company_phone_number_id BIGINT NOT NULL,
    operator_id BIGINT NULL,
    operator_message TEXT NULL,
    disconnect_initiator DISCONNECT_INITIATOR NOT NULL,
    response RESPONSE NOT NULL,
    paid REAL CHECK(paid > 0.0) NOT NULL,
    address_id BIGINT NULL,
);