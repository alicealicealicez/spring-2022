SELECT miRNA.name, t1.score, t2.score

SELECT *
FROM gene 
JOIN targets ON targets.gid = gene.gid
WHERE gene.name IN ("A1CF", "AACS")
INNER JOIN miRNA
ON miRNA.mid = targets.mid



SELECT miRNA.name, c.score as gene1_score, d.score as gene2_score
FROM miRNA 
LEFT JOIN (SELECT targets.score, targets.mid
		   FROM targets 
		   JOIN gene ON gene.gid = targets.gid
		   WHERE gene.name = "C14orf1") as c			
ON c.mid = miRNA.mid
LEFT JOIN (SELECT targets.score, targets.mid
		   FROM targets 
		   JOIN gene ON gene.gid = targets.gid
		   WHERE gene.name = "C14orf101") as d			
ON d.mid = miRNA.mid
WHERE d.score IS NOT NULL AND c.score IS NOT NULL




SELECT miRNA.name, c.score as gene1_score, d.score as gene2_score
FROM miRNA 
LEFT JOIN (SELECT targets.score, targets.mid
           FROM targets 
           JOIN gene ON gene.gid = targets.gid
           WHERE gene.name = "C14orf1") as c            
ON c.mid = miRNA.mid
LEFT JOIN (SELECT targets.score, targets.mid
           FROM targets 
           JOIN gene ON gene.gid = targets.gid
           WHERE gene.name = "C14orf101") as d           
ON d.mid = miRNA.mid
WHERE d.score IS NOT NULL AND c.score IS NOT NULL


