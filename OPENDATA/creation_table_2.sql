USE SIRENE ;
CREATE TABLE Nap73 (
NAP15 VARCHAR(3) COMMENT "Nomenclature d'activités et de produits",
NAP40 VARCHAR(3) COMMENT "Nomenclature d'activités et de produits",
NAP100 VARCHAR(2) COMMENT "Nomenclature d'activités et de produits",
NAP600 VARCHAR(5) COMMENT "Nomenclature d'activités et de produits",
LIB_NAP600 VARCHAR(100) COMMENT "Nomenclature d'activités et de produits",
LIB_NAP100 VARCHAR(100) COMMENT "Nomenclature d'activités et de produits",
LIB_NAP40 VARCHAR(100) COMMENT "Nomenclature d'activités et de produits",
LIB_NAP15 VARCHAR(100) COMMENT "Nomenclature d'activités et de produits");

CREATE TABLE Section_93(
Code VARCHAR(1) COMMENT "",
libelle VARCHAR(100));
SELECT * FROM Section_93;

CREATE TABLE Division_93(
Code VARCHAR(1) COMMENT "",
libelle VARCHAR(100));

CREATE TABLE Niveau_08(
NIV5 VARCHAR(6) COMMENT "",
NIV4 VARCHAR(5) COMMENT "",
NIV3 VARCHAR(4) COMMENT "",
libelle VARCHAR(100));
select * from Niveau_08 ;


USE SIRENE;

CREATE TABLE Niveau_93(
N_700 VARCHAR(5) COMMENT "",
N_220 VARCHAR(3) COMMENT "",
N_60 VARCHAR(2) COMMENT "",
N_31 VARCHAR(1) COMMENT "",
N_17 VARCHAR(1) COMMENT "");





DROP TABLE Section_93;






