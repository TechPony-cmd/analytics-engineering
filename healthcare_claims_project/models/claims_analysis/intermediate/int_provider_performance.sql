with provider_performance as (

    select 
		provider_id,
		provider_name,
		provider_specialty,
		insurance_type,
		sum(case when claim_status = 'Approved' then 1 else 0 end) over (partition by provider_id) as approved_claims,
		sum(case when claim_status = 'Approved' then 1 else 0 end) over (partition by provider_id)/ count(*) over (partition by provider_id) as success_rate,
		avg(patient_responsibility) over(partition by provider_id) as average_patient_responsisbility
	from 
		{{ ref('int_claims') }}
		
)
select 
	distinct *
from 
	provider_performance

