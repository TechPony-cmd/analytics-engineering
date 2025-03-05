with source as (

    select * from {{ ref('int_claims')}}

)
select
    provider_id, 
    diagnosis_code,
    insurance_type,
    count(*) as total_claims,
    sum(total_claim_amount) as total_claim_amounts,
    avg(total_claim_amount) as average_claim_amounts
from 
    source
group by 
    provider_id, diagnosis_code, insurance_type
order by 
    provider_id
