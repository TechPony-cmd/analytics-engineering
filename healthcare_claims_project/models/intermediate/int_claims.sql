{{ config(
    materialized='incremental',
    unique_key='claim_id',
    incremental_strategy='merge' 
) }}

with new_claims as (
    select 
        *
    from 
        {{ ref('stg_claims') }}
    {% if is_incremental() %}
     -- filter for incremental loading to only get new or updated rows
        where last_updated_date > (select max(last_updated_date) from {{ this }})
    {% endif %}
)
select * from new_claims