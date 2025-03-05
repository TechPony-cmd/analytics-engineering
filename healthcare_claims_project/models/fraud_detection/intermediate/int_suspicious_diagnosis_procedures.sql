with diagnosis_procedure_counts as (
    select 
        claim_id,
        provider_name,
        diagnosis_description,
        procedure_description,
        count(claim_id) over(partition by diagnosis_code, procedure_code) as claim_count
    from 
        {{ ref('int_claims') }}

),
unusual_combinations as (

    select 
        claim_id,
        provider_name,
        diagnosis_description,
        procedure_description,
        percent_rank() OVER (order by claim_count asc) as rarity_score
    from 
        diagnosis_procedure_counts

)

select 
    *,
    case 
        when rarity_score < 0.05 then 'Rare Combination - Possible Fraud'
        else 'Common Combination'
    end as fraud_risk_level
from 
    unusual_combinations
order by 
    rarity_score asc