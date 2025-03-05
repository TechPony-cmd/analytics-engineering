with provider_claims as (

    select 
        a.provider_id,
        a.provider_name,
        count(*) over(partition by a.provider_id) as total_claims,
        sum(case when a.payment_status = 'Denied' then 1 else 0 end) over(partition by a.provider_id) as rejected_claims,
        sum(case when a.payment_status = 'Under Review' then 1 else 0 end) over(partition by a.provider_id) as under_review_claims,
        sum(case when a.total_claim_amount > 10000 then 1 else 0 end) over(partition by a.provider_id) as high_value_claims,
        sum(case when a.insurance_paid_amount = 0 AND a.patient_responsibility = 0 then 1 else 0 end) over(partition by a.provider_id) as unpaid_claims,
        sum(case when a.payment_status = 'Denied' AND a.insurance_paid_amount > 0 then 1 else 0 end) over(partition by a.provider_id) as suspicious_payment,
        sum(case when b.provider_id is not null then 1 else 0 end) over(partition by a.provider_id) as flagged_provider
    from 
        {{ ref('int_claims') }} a
    left join
         {{ ref('flagged_providers') }} b on a.provider_id=b.provider_id
 
)
select 
    distinct 
        provider_id, 
        provider_name,
    case 
        when (rejected_claims / NULLIF(total_claims, 0)) > 0.2 then 'High Rejection Rate'
        when (under_review_claims / NULLIF(total_claims, 0)) > 0.7 then 'High Under Review Rate'
        when high_value_claims > 5 then 'High Number of Large Claims'
        else 'Normal'
    end as provider_risk_category,
    case 
        when (high_value_claims + unpaid_claims + suspicious_payment + flagged_provider) >= 2 then 'High Risk'
        when (high_value_claims + unpaid_claims + suspicious_payment + flagged_provider) = 1 then 'Medium Risk'
        else 'Low Risk'
    end as fraud_risk_level,
    high_value_claims,
    rejected_claims,
    unpaid_claims,
    suspicious_payment,
    flagged_provider,
    total_claims
from 
    provider_claims
order by 
    provider_id
