DROP TYPE IF EXISTS GENDER CASCADE;

CREATE TYPE GENDER AS enum ('Unknown', 'Other', 'Male', 'Female');

DROP TYPE IF EXISTS DISCONNECT_INITIATOR CASCADE;

create type DISCONNECT_INITIATOR as enum ('Origination', 'Destination');

DROP TYPE IF EXISTS RESPONSE CASCADE;

create type RESPONSE as enum (
    'Forbidden',
    'Busy Here',
    'Request Terminated',
    'OK'
);

DROP TYPE IF EXISTS BUSINESS_CATEGORY CASCADE;

create type BUSINESS_CATEGORY as enum (
    'Unknown',
    'Other',
    'Production',
    'Commerce',
    'Service industry'
);

-- Location models
DROP TABLE IF EXISTS us_state CASCADE;

CREATE TABLE us_state (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    UNIQUE(title)
);

DROP TABLE IF EXISTS us_city CASCADE;

CREATE TABLE us_city (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    us_state_id BIGINT NOT NULL,
    UNIQUE (title, US_state_id)
);

DROP TABLE IF EXISTS us_address CASCADE;

CREATE TABLE us_address (
    id BIGSERIAL PRIMARY KEY,
    us_city_id BIGINT NOT NULL,
    street VARCHAR(100) NULL,
    house VARCHAR(15) NULL,
    additional_info TEXT NULL,
    UNIQUE(us_city_id, street, house)
);

-- Equipment models
DROP TABLE IF EXISTS office CASCADE;

CREATE TABLE office (
    id BIGSERIAL PRIMARY KEY,
    us_address_id BIGINT NOT NULL,
    title VARCHAR(30),
    flat VARCHAR(15),
    UNIQUE(us_address_id, title, flat)
);

DROP TABLE IF EXISTS software CASCADE;

CREATE TABLE software (
    id BIGSERIAL PRIMARY KEY,
    software_name VARCHAR(50) NOT NULL,
    UNIQUE(software_name)
);

DROP TABLE IF EXISTS software_version CASCADE;

CREATE TABLE software_version (
    id BIGSERIAL PRIMARY KEY,
    soft_version VARCHAR(50) NOT NULL,
    software_id BIGINT NOT NULL,
    UNIQUE(soft_version, software_id)
);

DROP TABLE IF EXISTS work_place CASCADE;

CREATE TABLE work_place (
    id BIGSERIAL PRIMARY KEY,
    room_number VARCHAR(15) NOT NULL,
    office_id BIGINT NOT NULL,
    software_version_id BIGINT NOT NULL,
    tenant_company_id BIGINT NULL,
    UNIQUE(room_number, office_id)
);

-- Tenant company models
DROP TABLE IF EXISTS tenant_company CASCADE;

CREATE TABLE tenant_company (
    id BIGSERIAL PRIMARY KEY,
    isdisabled BOOLEAN DEFAULT false NOT NULL,
    title VARCHAR(50) NOT NULL,
    category BUSINESS_CATEGORY DEFAULT 'Unknown' NOT NULL,
    price_per_operator money NOT NULL,
    UNIQUE(title)
);

DROP TABLE IF EXISTS tenant_company_phone_number CASCADE;

CREATE TABLE tenant_company_phone_number (
    id BIGSERIAL PRIMARY KEY,
    phone_number VARCHAR(30) NOT NULL,
    tenant_company_id BIGINT,
    description VARCHAR(150) NOT NULL,
    UNIQUE(phone_number)
);

-- Persons model
DROP TABLE IF EXISTS caller_person CASCADE;

CREATE TABLE caller_person (
    id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(30) NULL,
    last_name VARCHAR(30) NULL,
    phone_number VARCHAR(30) NOT NULL,
    gender GENDER DEFAULT 'Unknown' NOT NULL,
    email VARCHAR(50) NULL,
    UNIQUE(phone_number, email)
);

DROP TABLE IF EXISTS operator CASCADE;

CREATE TABLE operator (
    id BIGSERIAL PRIMARY KEY,
    isdisabled BOOLEAN DEFAULT false NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NULL,
    gender GENDER DEFAULT 'Unknown' NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone_number VARCHAR(30) NOT NULL,
    password VARCHAR(64) NOT NULL,
    tenant_company_id BIGINT NOT NULL,
    UNIQUE(phone_number),
    UNIQUE(email)
);

DROP TABLE IF EXISTS operator_to_work_place CASCADE;

CREATE TABLE operator_to_work_place(
    work_place_id BIGINT NOT NULL,
    operator_id BIGINT NOT NULL,
    UNIQUE(operator_id),
    UNIQUE(work_place_id)
);

-- Call_log
DROP TABLE IF EXISTS call_log CASCADE;

CREATE TABLE call_log (
    id BIGSERIAL PRIMARY KEY,
    start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    duration smallint CHECK(duration > 0) NOT NULL,
    caller_person_id BIGINT NOT NULL,
    caller_person_message TEXT NULL,
    tenant_company_phone_number_id BIGINT NOT NULL,
    operator_id BIGINT NULL,
    operator_message TEXT NULL,
    disconnect_initiator DISCONNECT_INITIATOR NOT NULL,
    response RESPONSE NOT NULL,
    paid REAL CHECK(paid > 0.0) NOT NULL,
    us_city_id BIGINT NULL,
    additional_address VARCHAR(50) NULL
);