# CSV Cleaner Tool

A command-line tool for cleaning and transforming CSV files.  
Built with Python and pandas as part of a data-handling learning project.

## ✨ Features

- Strip whitespace from string columns  
- Remove duplicate rows  
- Drop rows with missing values  
- Fill missing values with a custom placeholder  
- Convert empty/whitespace-only cells into proper missing values  
- Configurable via CLI flags or a JSON config file  
- Logging to both console and rotating log files  
- Clear validation of input/output paths  

## 🚀 Usage

python main.py --input sample.csv --output cleaned.csv
python main.py --input sample.csv --output cleaned.csv --config config.json

## CLI Flags

--drop-missing	Drop rows containing missing values
--fill-missing VALUE	Fill missing values with VALUE
--strip-whitespace	Strip whitespace from string columns
--dedupe	Remove duplicate rows
--config FILE	Load cleaning rules from JSON config

## 🛠 Config File Example

{
    "strip_whitespace": true,
    "dedupe": true,
    "fill_missing": "NoData"
}

## 📁 Project Structure

csv-cleaner/
│
├── main.py
├── requirements.txt
├── README.md
├── config.json
├── logs/
│   └── app.log
└── src/
    ├── cleaner.py
    ├── cli.py
    ├── config.py
    ├── validators.py
    └── logger.py


## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd csv-cleaner
pip install -r requirements.txt
