# Healthcare Claims & Utilization - DBT Modelling

## Overview

This project focuses on building an end-to-end analytics solution for healthcare claims data, demonstrating advanced data engineering/ analytics engineering techniques with DBT, SQL, and data orchestration tools. All models in this project are designed to answer ASSUMED key questions that healthcare providers, insurers, and analysts would typically want to explore using claims data.

## Models Overview

* Staging Models: Raw data cleaning and initial transformation.
* Intermediate Models: Data transformations that prepare the data for analysis.
* Mart Models: Final models that provide actionable insights for end-users.

* DBT Best Practices:
	* Incremental Loading 
	* Testing & Validations using DBT tests
	* Window functions (PERCENT_RANK(), COUNT() OVER())
	* Aggregate functions (SUM(), AVG())
	* Conditional logic (CASE WHEN)
	
The models are categorized under two main themes: 

1. Claims Analysis 
* claims_aging model: identifies claims that have not been paid within a certain number of days.
* claims_payment_status model: tracks the count and percentage of claims paid, denied, or under review by various categories (e.g., provider, diagnosis, payment status).
* claims_summary: aggregates data to generate a summary of claims for analysis, such as total claim amounts by provider, diagnosis, or insurance type.
* provider_performance model: Evaluates the performance of healthcare providers in terms of claim approval, treatment outcomes, and patient responsibility.

2. Fraud Detection 
* duplicate_claims model: Identify duplicate claims submitted multiple times and stale claims that are being resubmitted after long periods
* suspicious_diagnosis_procedures model: Detect uncommon or high-risk diagnosis and procedure combinations that could indicate fraudulent claims.
* suspicious_providers: Detect healthcare providers with unusual claim patterns. Identify providers with high volumes of rejected claims or large claims exceeding industry averages.

## Project Structure

	├── dags/               			# Airflow DAGs for pipeline orchestration  
	├── healthcare_claims_project/      # DBT project with models, tests, and macros  
	│   ├── models/          			# Staging and marts models & testing   
	│   ├── seeds/           			# Mock seed data for claims  and flagged providers
	├── requirements.txt     			# Dependencies  
	├── dbt_project.yml     			 
	├── packages.yml     				# Package Dependencies  
	├── profiles.yml    				# database connection  
	└── README.md            			# Project documentation 

### Tech Stack

* DBT (Data modeling, transformation & testing)
* Airflow (Orchestration & scheduling, monitoring failure alerts)
* PostgreSQL (Data warehouse)
* SQL (Data modeling, performance tuning)

### Data - column:description
Please note that the data used for this analysis is mock data.

```
healthcare_claims data:
  	claim_id: Unique identifier for each claim
	claim_date: Date claim was submitted
	claim_status: status of claim (Approved, Denied, Pending)
	patient_id: Unique identifier assigned to the patient receiving medical services
	patient_age: age of patient
	patient_gender: gender of patient
	patient_zipcode: ZIP code of patient
	provider_id: Unique identifier for the healthcare provider or facility
	provider_name: Name of the healthcare provider or facility
	provider_specialty: The medical specialty of the provider (e.g.,General Surgery, Dermatology)
	provider_zipcode:	ZIP code of the provider’s location, useful for geographic analysis
	diagnosis_code: ICD-10 code representing the primary diagnosis for the claim
	diagnosis_description: Description of the diagnosis code (e.g., Type 2 Diabetes Mellitus)
	procedure_code: CPT (Current Procedural Terminology) code representing the medical procedure performed
	procedure_description: Description of the procedure performed (e.g., MRI Brain Scan)
	total_claim_amount: The total amount billed by the provider for the service
	insurance_paid_amount: The portion of the total claim amount covered by the insurance company
	patient_responsibility: The remaining balance the patient is responsible for (copay, deductible, coinsurance)
	insurance_type: The type of insurance coverage (HMO, PPO, Medicaid, Medicare, Employer-sponsored)
	payment_status: Status of the claim payment: Paid, Denied, Pending
	admission_date: Date the patient was admitted for treatment (relevant for inpatient claims)
	discharge_date: Date the patient was discharged from the facility (if applicable)

	flagged_providers:
		provider_id: Unique identifier for the healthcare provider or facility
		provider_name: Name of the healthcare provider or facility
		fraud_reason: reasons behind provider being flagged
  ```
