-- Create Table
DROP TABLE IF EXISTS city_info;

CREATE TABLE IF NOT EXISTS city_info(
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    census_2020 NUMERIC NOT NULL,
    land_area_sq_mile_2020 NUMERIC NOT NULL
);

-- Copy Data
COPY INTO city_database.new_city_schema.city_info
FROM @city_database.new_city_schema.snowflake_ext_stage_yml
FILE_FORMAT = csv_format;
