# Data Dictionary

This document provides descriptions of the data fields used in the Social Impact Bond datasets.

## Current and Historic Projects

The main dataset containing information about deployed social impact bonds and related instruments.

| Field | Description | Data Type |
|-------|-------------|-----------|
| Project Name | The official name of the project | Text |
| Country | ISO country code where the project is implemented | Text |
| INDIGO Project Name | Original name as listed in the INDIGO dataset | Text |
| Start Date | Date when the project began | Date |
| End Date | Date when the project ended or is scheduled to end | Date |
| Status | Current status of the project (e.g., Active, Completed) | Text |
| Is SIB | Whether the project is a Social Impact Bond | Boolean |
| Is DIB | Whether the project is a Development Impact Bond | Boolean |
| Outcome Funder | Organization(s) funding the outcomes | Text |
| Service Provider | Organization(s) providing the intervention services | Text |
| Intermediary | Organization(s) acting as intermediaries | Text |
| Target Population | Description of the population served by the project | Text |
| Outcome Metrics | Metrics used to measure success | Text |
| Maximum Outcome Payment | Maximum possible payment for outcomes | Numeric |
| Currency | ISO currency code for financial values | Text |

## Outcome Funds

Dataset containing information about outcome funds.

| Field | Description | Data Type |
|-------|-------------|-----------|
| Fund Name | Name of the outcome fund | Text |
| Country | ISO country code where the fund operates | Text |
| Launch Date | Date when the fund was launched | Date |
| Size | Total size of the fund | Numeric |
| Currency | ISO currency code for financial values | Text |
| Number of Projects | Number of projects supported by the fund | Numeric |
| Fund Manager | Organization managing the fund | Text |
| Outcome Funder | Organization(s) funding the outcomes | Text |

## Pipeline Projects

Dataset containing information about projects in development.

| Field | Description | Data Type |
|-------|-------------|-----------|
| Project Name | The official name of the project | Text |
| Country | ISO country code where the project is planned | Text |
| Status | Current development status | Text |
| Expected Launch | Expected launch date | Date |
| Policy Area | Area of social policy addressed | Text |
| Target Population | Description of the population to be served | Text |
| Outcome Funder | Organization(s) planning to fund outcomes | Text |
| Service Provider | Organization(s) planning to provide services | Text |

## Organizations Lookup

Reference data for organizations involved in pay-for-success projects.

| Field | Description | Data Type |
|-------|-------------|-----------|
| Organization Name | Official name of the organization | Text |
| Organization Type | Type of organization (e.g., Government, NGO, Private) | Text |
| Country | ISO country code where the organization is based | Text |
| Website | Official website URL | Text |

## Notes on Data Fields

- **Boolean Fields**: True/False values indicating whether a project belongs to a specific category
- **ISO Country Codes**: Standard two-letter country codes (ISO 3166-1 alpha-2)
- **ISO Currency Codes**: Standard three-letter currency codes (ISO 4217)
- **Dates**: Formatted as YYYY-MM-DD where complete information is available

For more detailed information on the original data structure, please refer to the [Indigo Data Standard](https://github.com/INDIGO-Initiative/indigo-data-standard).
