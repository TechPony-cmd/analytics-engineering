select
    distinct 
        claim_id,
        insurance_type,
        diagnosis_description,
        diagnosis_code,
        CASE
            WHEN last_updated_date - claim_date <= 30 THEN '0-30 days'
            WHEN last_updated_date - claim_date <= 60 THEN '31-60 days'
            ELSE '60+ days'
        END AS aging_category
from
    {{ ref('int_claims') }}
where 
    payment_status != 'Paid'
