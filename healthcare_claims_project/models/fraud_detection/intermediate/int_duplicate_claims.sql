
with duplicate_claims as (
    select 
        claim_id,
        patient_id,
        provider_name,
        diagnosis_description,
        procedure_description,
        total_claim_amount,
        admission_date,
        discharge_date,
        count(*) OVER (PARTITION by claim_id, patient_id, provider_id, diagnosis_code, procedure_code, total_claim_amount, admission_date, discharge_date) as duplicate_count
    from 
        {{ ref('int_claims') }}
)

select * from duplicate_claims where duplicate_count > 1