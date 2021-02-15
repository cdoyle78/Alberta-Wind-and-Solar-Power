# Alberta-Wind-and-Solar-Power

All data downloaded from http://ets.aeso.ca/

Pool price data can only be downloaded in 1 year increments. FormatAESOPoolPrice.py combines the yearly download files (csv) into a continous time series. AESO also uses a 1 to 24 hour time periods. Pandas Datetime requires 0-23 hour format. This script subtracts one hour and outputs a datetime friendly CSV.

Note: The additional hour at daylight savings is removed to leave a 24 hour day.

Metered volume data can only be downloaded in 1 month increments in the form of daily records. FormatMeteredVolume.py combines month long files, and extracts the data for wind and solar generators outputting individual csv time series files for each generator.

AB_WindSolarPower.ipynb reads the conditioned csv outputs above into dataframes and generates the plots in a Jupyter notebook.
