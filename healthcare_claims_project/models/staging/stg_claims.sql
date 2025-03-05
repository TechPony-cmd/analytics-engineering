with source as (

    select * from {{ ref('healthcare_claims') }}

)
select 
	claim_id,
    claim_date,
    patient_id,
    patient_age,
    patient_gender, 
    patient_zipcode,
    provider_id,
    provider_name,
    provider_specialty,
    provider_zipcode,
    diagnosis_code,
    diagnosis_description,
    procedure_code,
    procedure_description,
    coalesce(total_claim_amount,0.0) as total_claim_amount,	
    coalesce(insurance_paid_amount, 0.0) as insurance_paid_amount,
    patient_responsibility,	
    claim_status,
    insurance_type,
    case 
        when payment_status = 'Pending' then 'Under Review' 
        when payment_status = 'Rejected' then 'Denied' 
        when payment_status = 'Approved' then 'Paid'
        else null
    end as payment_status,
    admission_date,
    discharge_date,
    current_date as last_updated_date
from 
	source


