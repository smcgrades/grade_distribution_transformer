# Grade Distribution Transformer

*Grade Distribution Transformer* is a python script that transforms `.xlsx` files created from SMC's grade distribtuion PDFs into usuable `.csv` and `.json` files.
This tool was created to allow me to easily transform and upload the data into a database.

## Prerequisites

Before you begin, ensure you have the following:

- You have installed the latest version of [python](https://www.python.org/downloads/).

## Setting Up *Grade Distribution Transformer*

To install and set up *Grade Distribution Transformer* follow the steps:

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

To use *Grade Distribution Transformer* type the following:

```bash
python3 main.py
```

- After the process is complete you should see folders for each `.xlsx` with the same name.

    - *All `.xlsx` files follow the same format of `[semester]_[year].xlsx`; so folders should be the same.*

- Within each folder should be three files:

    - `[semester]_[year]_.csv`
        - The csv file created from the original `.xlsx`.
    - `[semester]_[year]_cleaned.csv`
        - A new csv file where it has been cleaned.
    - `[semester]_[year].json`
        - The final `.json` file that has a list of all classes, no duplicates, and sections combined by their professor.

## Additional Info

This script currently works for:

- Fall 2016
- Fall 2017
- Fall 2018
- Fall 2020
- Fall 2021
- Fall 2022
- Spring 2017
- Spring 2019
- Spring 2021
- Spring 2022
- Spring 2023

## Notes

Currently Fall 2019, Spring 2018, and Spring 2020 aren't avaiable in `.xlsx`, `.csv`, or `.json`. This is because the process of converting them from PDF tables to `.xlsx` is a much more tedious process that I'll probably tackle at a different moment in time.

## Future Features

- Make the script for the rest of the grade distribution PDFs available.

## License

Copyright &copy; 2023 Asarel Castellanos

This project is [MIT](https://github.com/smcgrades/grade_distribution_transformer/blob/main/LICENSE.txt) licensed.
