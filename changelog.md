# Changelog Against Original INDIGO Dataset

By: Daniel Rosehill (danielrosehill.com)

- INDIGO dataset was imported from the GO Lab website on May 20th

Changes applied:

## Currency Standardisation (Data Standardisation)

Curencies were standardised on ISO 3166. 

Where currencies were stated in non-compliant terms ("Israeli New Shekels") they were replaced by their ISO values (ILS).

## Data Completions (Data Completion)

Data was completed for standardisation where incomplete.

For example, in `outcome-funds.csv` fund activity was reported as either `active` or left blank.

The blank values were replaced with `Not Stated`

## Column Consolidation

This redacted version of the INDIGO dataset was prepared to supply knowledge to an AI tool intended for policymakers exploring social impact bonds. 

Given the use case, certain columns were omitted which were felt to add unnecessary detail for the purpose of the analysis. 

These included, for example, a boolean column evaluating whether a particular project was a social investment prototype which was mostly unpopulated. These columns were  ommitted selectively and judiciously.

The objective of this streamlining of the data was to consolidate slightly the amount of information that AI tools would be exposed to in order to streamline the retrieval process while retaining the most important fields captured by the INDIGO project.

## FX Rate Handling And Non-USD Values

The INDIGO project tracking active outcome funds and impact bonds (both social impact bonds and development impact bonds) helpfully notes the original currency in which the funding was contracted. A range is also provided which exists because stakeholders may vary in how they calculate funding commitments and because the actual amount of capital deployed may not match that which was committed for various reasons.
  
The more useful and important figure for the purpose of policy evaluation is the *actual amount* of capital deployed, which was renamed `actual_investment_committed` (header rows were renamed solely for machine readability). It's vital that this field is interpreted together with the ISO currency identifier as projects vary considerably in their contracting currency.  
  
## Recalculation Of Non-USD Values (Data Removal, Data Addition)

The INDIGO project provides conversions to the US dollar. 

I added the column back with a date identifier for the purpose of transparency, while adding a blank value for dynamic USD rate conversion intended to allow for using the data with live FX rate ingestion and conversion.

## Separating Impact Bonds From Outcomes Funds (Data Additions)

In order to facilitate distinguishing between the various types of pay for outcomes project, I added three boolean values to the data set.

These are:

- `is_social_impact_bond`: To label SIBs  
- `is_development_impact_bond`: To label DIBs  
- `is_outcomes_fund`: To label outcomes funds 


In the first instance, and unless impact bonds are clearly identified as development impact bonds, they are listed as impact bonds. 

Outcome funds, on the other hand, are listed as outcomes funds. This distinction, it is hoped, will allow for analyzing the data more closely based on this important distinction.

## Bond Name (Data Addition)

I added a field called `bond_name` in order to capture the specific nomenclature used for the type of impact bond tract. My intention in doing so was to help aggregate a list of the variants of impact bonds that are being deployed around the world. Beyond the classic initial bifurcation dividing between social and development impact bonds, the latter involving sources from multilateral funders, an increasing number of more niche variants have arisen over the years, including among others the career impact bond, but also as in examples here, cataract bonds, ocean bonds, etc. These nomenclatures were manually written based on the descriptions of the bonds.

## Translated Project Names (Data Addition)

Many impact bonds are deployed in non-English speaking geographies.

To distinguish between approximate English translations and the official or original names for the projects, two additional columns were added. These are:

- `name_english_translation`: To capture the translated name for Projects which were translated into English from other languages

And:

- `name original language` 

In order to preserve the exact name of the bond as it appeared in the original language that the project was devised in.