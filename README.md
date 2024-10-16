# openRiskScore

**openRiskScore** A Python framework for risk scoring in both classic and federated/decentralized contexts

![image](static/federated_models.png)

## Summary Information

* Author: [Open Risk](http://www.openriskmanagement.com)
* License: Apache 2.0
* Code Documentation: [Read The Docs](Upcoming)
* Mathematical Documentation: [Open Risk Manual](https://www.openriskmanual.org/wiki/Category:SME_Credit_Risk)
* Development website: [Github](https://github.com/open-risk/openRiskScore)
* Discussions: [Open Risk Commons](https://www.openriskcommons.org/c/open-source/openriskscore/16)

**NB: openRiskScore is still in active development. The alpha release will be available here**

## Introduction

openRiskScore aims to support the development of both expert based and statistical [risk scoring](https://www.openriskmanual.org/wiki/Risk_Score) and risk rating models. 

The library aims to wrap popular machine learning frameworks as algorithmic backends and focuses on supporting high quality risk model development and maintenance.

Two important use cases for openRiskScore are [credit risk scoring](https://www.openriskmanual.org/wiki/Category:Credit_Scoring_Models), and sustainability (ESG) ratings and scores. It is envisaged that scoring activities can be either pursued by a standalone entity (operating on its own data) or in federation (independent entities sharing some data sets using federated learning principles, algorithms and tools). 

### Standalone Mode
In *standalone mode* openRiskScore emulates a classic use case where, e.g., a financial institution or other credit provider aims to develop a risk scoring system on the basis of data it has in its possession.  Use cases for the standalone mode are both as intended (standalone) scoring system and as a validation framework for federated applications.

### Federated Mode
The federated mode essentially facilitates the development of a *generic* (pooled) scorecard that applies to a wide population (which is assumed homogeneous)

## Documentation

* [Project Finance Scorecard](docs/ProjectFinanceScorecard.md). Description of the Standardized Specialized Lending Scorecard for Project Finance
* [Scorecard Characteristics](docs/ScorecardCharacteristics.xlsx). Documentation of the definitions of the scorecard
* [Specification Reference](docs/SpecificationReference.md). This document excerpts the relevant segments of the EBA official reference that defines the standardized credit scorecard for project finance exposures

## Further Documentation and Reading

### Credit Scoring
* [How to Build a Credit Scorecard](https://www.openriskmanual.org/wiki/How_to_Build_a_Credit_Scorecard)
* [How to Build an SME Credit Scorecard](https://www.openriskmanual.org/wiki/How_to_Build_an_SME_Credit_Scorecard)
* [Credit Scoring with Python](https://www.openriskmanual.org/wiki/Credit_Scoring_with_Python)

### ESG Scoring
* [List of ESG Factos](https://www.openriskmanual.org/wiki/List_of_ESG_Factors)

### Semantic Documentation of Risk Models
* [Risk Model Ontology](https://www.openriskmanual.org/wiki/Risk_Model_Ontology)
* [Embedding PMML in DOAM](https://www.openriskmanagement.com/towards-semantic-description-of-machine-learning-models/)

## Learning Modules at the Open Risk Academy
* [Exploratory Risk Data Analysis using Pandas, Seaborn and Statsmodels](https://www.openriskacademy.com/course/view.php?id=48)
* [Analysis of Credit Migration using Python TransitionMatrix](https://www.openriskacademy.com/course/view.php?id=38)

## White Papers on Federated Risk Analysis

* [White Paper: Federated Credit Systems, Part I: Unbundling The Credit Provision Business Model](https://www.openriskmanagement.com/white_paper_federated_credit_part_i_systems_unbundling_the_credit_provision_business_model/)
* [White Paper: Federated Credit Systems, Part II: Techniques for Federated Data Analysis](https://www.openriskmanagement.com/white_paper_federated_credit_systems_part_ii_techniques_for_federated_data_analysis/)