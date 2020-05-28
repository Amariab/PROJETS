USE SIRENE;

SELECT * FROM SIRENE.Section_08;
SELECT * FROM SIRENE.Niveau_08 ;
SELECT * FROM SIRENE.etab_marseille;
select * from SIRENE.Historique_table;
SELECT * FROM SIRENE.Etablissement;
SELECT COUNT(siret) from etab_marseille;

#nb d'étb par arrondissement
select codePostalEtablissement, count(*) as etablissement_par_arrondissement from etab_marseille group by codePostalEtablissement;

#nb d'etb pour un arrondissement donné :
SELECT COUNT(siret) FROM etab_marseille where codePostalEtablissement = 13001;

#récup données pour un arrondissement donné :
SELECT * FROM etab_marseille where `codePostalEtablissement` = 13001;

#nb d'etab pour un secteur donné et pour un arrondissement donné :
SELECT 
Libellé,
(select Count(siret)) as etb_secteur,
codePostalEtablissement
# siret, enseigne1Etablissement, enseigne2Etablissement, enseigne3Etablissement, Libellé
    FROM etab_marseille
        INNER JOIN Niveau_08 ON etab_marseille.activitePrincipaleEtablissement = Niveau_08.NIV5 
        INNER JOIN Section_08 ON  Niveau_08.NIV1 = Section_08.Code
WHERE 
Code = 'A' AND 
codePostalEtablissement = 13002
group by Libellé, Code ;

#recherche par code postal par code (libellé) et par secteur pour l'année 2008 :
select Libellé,Code, codePostalEtablissement, count(*) as etablissement_par_secteur_2008 from etab_marseille 
inner join Niveau_08 on etab_marseille.activitePrincipaleEtablissement = Niveau_08.NIV5
inner join Section_08 on Niveau_08.NIV1=Section_08.Code
where nomenclatureActivitePrincipaleEtablissement='NAFRev2' group by Libellé,Code, codePostalEtablissement ;

#moyenne
SELECT 
    libelleCommuneEtablissement,
    AVG(TIMESTAMPDIFF(YEAR, etab_marseille.dateCreationEtablissement,
        Historique_table.dateDebut)) AS duree
FROM
    etab_marseille
        INNER JOIN
    Historique_table
WHERE
    Historique_table.changementEtatAdministratifEtablissement = 1
        AND Historique_table.etatAdministratifEtablissement = 'F'
GROUP BY etab_marseille.libelleCommuneEtablissement limit 10;



