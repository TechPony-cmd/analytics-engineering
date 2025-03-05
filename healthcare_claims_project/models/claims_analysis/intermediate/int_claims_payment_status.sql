select
    provider_id,
    payment_status,
	count(*) as claim_count,
	round(count(*) / sum(count(*)) over (partition by provider_id) * 100, 2) AS payment_percentage
from 
    {{ ref('int_claims') }}
group by 
    provider_id, payment_status
order by 
    provider_id
