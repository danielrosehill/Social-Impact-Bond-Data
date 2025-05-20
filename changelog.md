# Changelog Against Original INDIGO Dataset

- INDIGO dataset was imported from the GO Lab website on May 20th


Changes applied:

## Currency Standardisation

Curencies were standardised on ISO 3166. 

Where currencies were stated in non-compliant terms ("Israeli New Shekels") they were replaced by their ISO values (ILS).

## Data Completions

Data was completed for standardisation where incomplete.

For example, in `outcome-funds.csv` fund activity was reported as either `active` or left blank.

The blank values were replaced with `Not Stated`