# Grade Distribution Transformer
*Grade Distribution Transformer* is a python script that transforms `.xlsx` files created from SMC's grade distribtuion PDFs into usuable `.csv` and `.json` files.
This tool was created to allow me to easily transform and upload the data into a database.

## Prerequisites
Before you begin, ensure you have the following:
- You have installed the latest version of [python](https://www.python.org/downloads/).

## Installing *Grade Distribution Transformer*
To install *Grade Distribution Transformer* follow the steps:
```bash
git clone https://github.com/smcgrades/grade_distribution_transformer.git
```
```bash
cd grade_distribution_transformer
```
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
```bash
pip install pandas
```
```bash
pip install openpyxl
```
```bash
pip install fuzzywuzzy
```

## Using *Grade Distribution Transformer*
To use *Grade Distribution Transformer* follow these steps:
- Get the [SMC Grade Distribution PDFs](https://www.smc.edu/administration/institutional-research/grade-distribution.php) you want to transform.
- Go to [CloudConvert](https://cloudconvert.com/) and transform those PDFs into `.xlsx` files.
- Open the folder `grade_distribution_transformer` and create a `grades` folder.
- Place those converted `.xlsx` files into the 'grades' folder.
- Go to your IDE or terminal and run `python3 main.py` within the `grade_distribution_transformer` folder and follow the instructions.

## Additional Info
This script currently works for:
- Fall 2020
- Fall 2021
- Fall 2022
- Spring 2021
- Spring 2022
- Spring 2023

## Future Features
- Automate the process of converting PDFs into XLSX files using CloudConvert API.
- Make the script for the rest of the grade distribution PDFs available.

## License
Copyright &copy; 2023 Asarel Castellanos

This project is [MIT](https://github.com/smcgrades/grade_distribution_transformer/blob/main/LICENSE.txt) licensed.
