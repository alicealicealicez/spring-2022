explain
SELECT pg.Sample_id, gene, value, Molecular_Subtype 
from pcga_annotation pa
right join pcga_geneset pg on pg.sample_id = pa.Sample_id
group by pg.Sample_id 

SELECT * 
from pcga_annotation pa
inner join pcga_whole_slide pws on left(pws.Sample_id, 30) = LEFT(pa.Sample_id, 30)

SELECT * 
from TCGA_annotation ta
inner join tcga_filtered_geneset tfg on left(tfg.sample_id, 16) = LEFT(ta.barcode, 16)


SELECT * 
from TCGA_annotation ta 
inner join TCGA_whole_slide tws on left(tws.Sample_id, 16) = LEFT(ta.sample, 16)

SELECT ta.Module_1, ta.Module_2, ta.Module_3, ta.Module_4, ta.Module_5, ta.Module_6, ta.Module_7, ta.Module_8, ta.Module_9, tws.*
from TCGA_annotation ta 
inner join TCGA_whole_slide tws on left(tws.Sample_id, 16) = LEFT(ta.sample, 16)


SELECT ta.Module_1, ta.Module_2, ta.Module_3, ta.Module_4, ta.Module_5, ta.Module_6, ta.Module_7, ta.Module_8, ta.Module_9, tws.* 
from TCGA_annotation ta 
inner join TCGA_whole_slide tws on left(tws.Sample_id, 30) = LEFT(ta.Sample_id, 30)

SELECT * 
from pcga_annotation pa
right join pcga_geneset pg on pg.sample_id = pa.Sample_id
WHERE SampleType = 'Biopsy' AND Cohort = 'ValidationSet' AND Sex = 'Female'
