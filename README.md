# openRiskScore
A python framework for risk scoring in both classic and federated/decentralized contexts

## Intro
openRiskScore is a Python powered library to support the development of statistical risk scoring and rating models in both traditional and decentralized (federated) contexts. The library uses popular machine learning frameworks as algorithmic backends and focuses on supporting high quality risk model development and maintenance.

Two major use cases for openRiskScore are credit risk scoring, and sustainability (ESG) scoring. It is envisaged that scoring activities can be either pursued by a standalone entity (operating on its own data) and in federation (independent entities sharing some data sets using federated learning principles, algorithms and tools). 

## Key Information
* Author: [Open Risk](http://www.openriskmanagement.com)
* License: Apache 2.0
* Code Documentation: [Read The Docs](Upcoming)
* Mathematical Documentation: [Open Risk Manual](https://www.openriskmanual.org/wiki/Category:SME_Credit_Risk)
* Development website: [Github](https://github.com/open-risk/openRiskScore)
* Discussions: [Gitter](https://gitter.im/open-risk/Lobby)

**NB: openRiskScore is still in active development. The alpha release will be available here**

### Standalone Mode

In *standalone mode* openRiskScore emulates a classic use case where a financial institution or other credit provider aims to develop a scoring system on the basis of data it has in its possession.  Use cases for the standalone mode are both as intended (standalone) scoring system and as a validation framework for federated applications.

### Federated Mode

The federated mode essentially facilitates the development of a *generic* (pooled) scorecard that applies ot a wide population (which is assumed homogeneous)

## Documentation

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
