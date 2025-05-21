# INDIGO Social Impact Bonds And Pay For Outcomes Dataset Analysis (May 22nd 2025)

[![Data Source: GO Lab](https://img.shields.io/badge/Data%20Source-GO%20Lab-blue)](https://golab.bsg.ox.ac.uk/)
[![Last Updated: May 2025](https://img.shields.io/badge/Last%20Updated-May%202025-green)](documentation/timestamps.md)

This repository contains a curated, redacted, and standardized data set based on the Government Outcome Labs project at Oxford University (UK). It is the leading international data resource tracking the growth and execution of social impact bonds (SIBs), development impact bonds (DIBs), outcome funds, and other pay-for-success instruments worldwide.

## Project Purpose

The data set supports research and AI-driven policy analysis on innovative development finance mechanisms that leverage private capital to address social and environmental challenges. It is designed to help policymakers, researchers, and practitioners understand the contours and evolution of these instruments, facilitating evidence-based decision-making.

## Repository Structure

| Directory | Description |
|-----------|-------------|
| [`edited-data/`](edited-data/) | Contains the primary curated datasets |
| [`documentation/`](documentation/) | Documentation files including changelog and sources |
| [`assistant-prompts/`](assistant-prompts/) | AI assistant prompts for data enrichment |
| [`archive/`](archive/) | Archived data and previous versions |
| [`reference/`](reference/) | Reference materials and supporting documents |

## Key Data Files

| File | Description | Path |
|------|-------------|------|
| Current & Historic Projects | Main dataset of all deployed projects | [`edited-data/pay-for-outcomes/deployed-and-historic/current-and-historic-projects.csv`](edited-data/pay-for-outcomes/deployed-and-historic/current-and-historic-projects.csv) |
| Outcome Funds | Dataset of outcome funds | [`edited-data/pay-for-outcomes/deployed-and-historic/outcomefunds.csv`](edited-data/pay-for-outcomes/deployed-and-historic/outcomefunds.csv) |
| Pipeline Projects | Dataset of projects in development | [`edited-data/pay-for-outcomes/pipeline/pipeline.csv`](edited-data/pay-for-outcomes/pipeline/pipeline.csv) |
| Organizations Lookup | Reference data for organizations | [`edited-data/pay-for-outcomes/lookup-data/organisations-lookup.csv`](edited-data/pay-for-outcomes/lookup-data/organisations-lookup.csv) |

## Key Features of the Data Set

- **Source**: Derived from the Government Outcome Labs' authoritative global impact bond data.
- **Redacted & Reformulated**: Non-essential rows, especially those related to contracting nuances, have been removed to focus on policy-relevant information.
- **Supplementary Data**: Added boolean columns to distinguish between historic and current bonds, and to clarify the type of instrument (SIB, DIB, etc.).
- **Standardization**: Country names and currencies are standardized to ISO codes for consistency and interoperability.
- **Data Streamlining**: Excludes interconnected Indigo project unique IDs and other elements not directly relevant to policy analysis.
- **Nomenclature Support**: Boolean flags for SIBs, DIBs, and regional naming variants to facilitate comparative research across jurisdictions.
- **Currency Handling**: USD conversions are excluded, enabling dynamic calculation as needed.
- **Character Set Correction**: All known encoding and import issues have been rectified.
- **Project Name Labeling**: Where project names previously concatenated original and translated values, these are now split into separate fields for clarity and improved labeling.

## Source Data Set Information

- [Impact Bond Dataset v2](https://golab.bsg.ox.ac.uk/knowledge-bank/indigo/impact-bond-dataset-v2/)
- [INDIGO Initiative GitHub Homepage](https://github.com/INDIGO-Initiative)
- [Indigo Data Standard](https://github.com/INDIGO-Initiative/indigo-data-standard)
- [Government Outcomes Lab (GO Lab)](https://golab.bsg.ox.ac.uk/)

## Documentation

| Document | Description |
|----------|-------------|
| [Data Dictionary](documentation/data-dictionary.md) | Descriptions of all data fields in the datasets |
| [Changelog](documentation/changelog.md) | Record of changes made to the datasets |
| [Data Sources](documentation/sources.md) | Original data source information |
| [Timestamps](documentation/timestamps.md) | Dataset update timestamps |

## Intended Use

This data set is intended for:
- Policymakers exploring the design and impact of pay-for-success instruments
- Researchers in development finance and social innovation
- AI tools for automated analysis and insight generation
- Comparative studies of outcome-based funding mechanisms

## Citation

If you use this data set, please cite the Government Outcome Labs, University of Oxford, and reference this repository.