# CSV Cleaner Tool

A command-line utility for cleaning and transforming CSV files using **Python** and **pandas**.
Designed as a practical data-handling project with configurable workflows and structured logging.

---

## Features

* Trim whitespace from string columns
* Remove duplicate rows
* Drop rows with missing values
* Fill missing values with a custom placeholder
* Convert empty or whitespace-only cells into proper missing values
* Configure behavior via CLI flags or JSON config file
* Structured logging to console and rotating log files
* Input/output path validation

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/murspi/csv-cleaner.git
cd csv-cleaner
pip install -r requirements.txt
```

---

## Usage

Basic usage:

```bash
python main.py --input sample.csv --output cleaned.csv
```

Using a configuration file:

```bash
python main.py \
  --input sample.csv \
  --output cleaned.csv \
  --config config.json
```

---

## CLI Options

| Flag                   | Description                                 |
| ---------------------- | ------------------------------------------- |
| `--drop-missing`       | Remove rows containing missing values       |
| `--fill-missing VALUE` | Replace missing values with specified value |
| `--strip-whitespace`   | Trim whitespace from string columns         |
| `--dedupe`             | Remove duplicate rows                       |
| `--config FILE`        | Load cleaning rules from JSON config        |

---

## Configuration Example

```json
{
  "strip_whitespace": true,
  "dedupe": true,
  "fill_missing": "NoData"
}
```

---

## Project Structure

```text
csv-cleaner/
│
├── main.py
├── requirements.txt
├── README.md
├── config.json
│
├── logs/
│   └── app.log
│
└── src/
    ├── cleaner.py
    ├── cli.py
    ├── config.py
    ├── validators.py
    └── logger.py
```
