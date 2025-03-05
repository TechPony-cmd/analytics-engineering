# Healthcare Claims & Utilization - DBT Modelling

## Overview

This project focuses on building an end-to-end analytics solution for healthcare claims data, demonstrating advanced data engineering/ analytics engineering techniques with DBT, SQL, and data orchestration tools. All models in this project are designed to answer ASSUMED key questions that healthcare providers, insurers, and analysts would typically want to explore using claims data.

## Models Overview

The models are categorized under two main themes: 
	1. Claims Analysis e.g. How are providers getting reimbursed, and is there any variation in payment rates across different provider types or regions?

	2. Fraud Detection e.g. Which healthcare providers are potentially involved in suspicious or fraudulent activities based on claim patterns, payment discrepancies, and unusual trends? Are there any irregularities in the claims approval process that may suggest fraud?

The insights generated from these models can be used by healthcare organizations to improve decision-making, optimize resources, and detect anomalies.

## Project Structure

This project is divided into several sections based on the stages of the data pipeline:
	•	Staging Models: Raw data cleaning and initial transformation.
	•	Intermediate Models: Data transformations that prepare the data for analysis.
	•	Mart Models: Final models that provide actionable insights for end-users.
	
├── dags/               			# Airflow DAGs for pipeline orchestration  
├── healthcare_claims_project/      # DBT project with models, tests, and macros  
│   ├── models/          			# Staging and marts models & testing   
│   ├── seeds/           			# Mock seed data for claims  and flagged providers
├── requirements.txt     			# Dependencies  
├── dbt_project.yml     			 
├── packages.yml     				# Package Dependencies  
├── profiles.yml    				# database connection  
└── README.md            			# Project documentation 
└── seed_data_info.yml            	# column: description on seed data

Tech Stack
	•	DBT (Data modeling, transformation & testing)
	•	Airflow (Orchestration & scheduling, monitoring failure alerts)
	•	PostgreSQL (Data warehouse)
	•	SQL (Data modeling, performance tuning)


