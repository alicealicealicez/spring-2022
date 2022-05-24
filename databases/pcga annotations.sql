DROP TABLE IF EXISTS PCGA_annotation;

CREATE TABLE PCGA_annotation (
	Sample_id varchar(100) NOT NULL,
	SampleType varchar(100),
	Cohort varchar(100),
	Batch int,
	Total_PE_Reads int,
	Percent_Uniquely_Aligned int,
	Median_TIN double,
	Patient int,
	Location_Code varchar (100),
	Location_Name varchar (100),
	Location_Desc varchar (100),
	Time int,
	Dysplasia_Grade varchar (100),
	Histology_Code varchar(100),
	Complete_Histology_at_Site varchar (100),
	Complete_Previous_Histology_at_Site varchar (100),
	Complete_Later_Histology_at_Site varchar (100),
	Molecular_Subtype varchar (100),
	Molecular_Subtype_BrushPrediction varchar (100),
	Progression_Status varchar (100),
	Age_at_Baseline double,
	Race varchar (100),
	Sex varchar (100),
	Genomic_Smoking_Status varchar (100),
	Previous_LC_History varchar (100),
	Previous_LC_History_Detail varchar (100),
	Asbestos_Exp varchar (100),
	HighRisk_LC_Job varchar (100),
	COPD_Status varchar (100),
	COPD_GOLD varchar (100),
	COPD_FEV_FVC_Ratio varchar(100),
	COPD_FEV_Prct_Pred varchar(100),
	TCGA_Subtype varchar (100),
	Module_6 double,
	Module_1 double,
	Module_5 double,
	Module_8 double,
	Module_3 double,
	Module_2 double,
	Module_9 double,
	Module_7 double,
	Module_4 double,
	AnalyteRNAIsolationNames varchar (100),
	FASTQ1 varchar (100),
	FASTQ2 varchar (100),
	PRIMARY KEY(Sample_id)
	)engine = innodb;




LOAD DATA LOCAL INFILE 'samples_annotation_v3.txt' INTO TABLE PCGA_annotation;



