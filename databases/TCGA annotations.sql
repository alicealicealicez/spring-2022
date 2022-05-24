
DROP TABLE IF EXISTS TCGA_annotation;

CREATE TABLE TCGA_annotation (
	tcga_id int NOT NULL AUTO_INCREMENT,
	barcode varchar(200),
	patient varchar(100),
	sample varchar(100),
	shortLetterCode varchar(100),
	definition varchar(100),
	sample_submitter_id varchar(100),
	sample_type_id varchar(100),
	oct_embedded varchar(100),
	sample_id varchar(100),
	submitter_id varchar(100),
	state varchar(100),
	is_ffpe varchar(100),
	sample_type varchar(100),
	tissue_type varchar(100),
	days_to_collection varchar(100),
	initial_weight varchar(100),
	intermediate_dimension varchar(100),
	pathology_report_uuid varchar(100),
	shortest_dimension varchar(100),
	longest_dimension varchar(100),
	synchronous_malignancy varchar(100),
	ajcc_pathologic_stage varchar(100),
	days_to_diagnosis varchar(100),
	treatments varchar(1000),
	last_known_disease_status varchar(100),
	tissue_or_organ_of_origin varchar(100),
	days_to_last_follow_up varchar(100),
	age_at_diagnosis varchar(100),
	primary_diagnosis varchar(100),
	year_of_diagnosis varchar(100),
	prior_malignancy varchar(100),
	prior_treatment varchar(100),
	ajcc_staging_system_edition varchar(100),
	ajcc_pathologic_t varchar(100),
	morphology varchar(100),
	ajcc_pathologic_n varchar(100),
	ajcc_pathologic_m varchar(100),
	classification_of_tumor varchar(100),
	diagnosis_id varchar(100),
	site_of_resection_or_biopsy varchar(100),
	icd_10_code varchar(100),
	tumor_grade varchar(100),
	progression_or_recurrence varchar(100),
	cigarettes_per_day varchar(100),
	alcohol_history varchar(100),
	exposure_id varchar(100),
	years_smoked varchar(100),
	pack_years_smoked varchar(100),
	ethnicity varchar(100),
	vital_status varchar(100),
	gender varchar(100),
	race varchar(100),
	age_at_index varchar(100),
	days_to_birth varchar(100),
	year_of_birth varchar(100),
	demographic_id varchar(100),
	days_to_death varchar(100),
	year_of_death varchar(100),
	bcr_patient_barcode varchar(100),
	primary_site varchar(100),
	disease_type varchar(100),
	project_id varchar(100),
	name varchar(100),
	releasable varchar(100),
	released varchar(100),
	paper_patient varchar(100),
	paper_Sex varchar(100),
	TSS varchar(100), 
	Plate varchar(100),
	cancer_class varchar(100),
	S_id varchar(100),	
	paper_Age_at_diagnosis varchar(100),
	paper_T_stage varchar(100),
	paper_N_stage varchar(100),
	paper_Smoking_Status varchar(100),
	PRIMARY KEY(tcga_id)
	)engine = innodb;