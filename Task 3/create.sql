CREATE TABLE apps (
    PK SERIAL PRIMARY KEY,
    ID VARCHAR,
    TITLE VARCHAR,
    RATING FLOAT(2),
    LAST_UPDATE_DATE DATE
);