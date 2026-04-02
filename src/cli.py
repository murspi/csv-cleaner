import argparse

def build_parser():
    parser = argparse.ArgumentParser(
        description="CSV Cleaner Tool - clean, validate and transform CSV files."
    )

    # Required arguments. 
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file."
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path where the cleaned CSV will be saved."
    )

    # Cleaning rule flags
    parser.add_argument(
        "--drop-missing",
        action="store_true",
        default=None,
        help="Drop rows containing missing values."
    )

    parser.add_argument(
        "--fill-missing",
        type=str,
        help="Fill missing values with the provided value."
    )

    parser.add_argument(
        "--strip-whitespace",
        action="store_true",
        default=None,
        help="Strip whitespace from string columns."
    )

    parser.add_argument(
        "--dedupe",
        action="store_true",
        default=None,
        help="Remove duplicate rows."
    )

    parser.add_argument(
        "--config",
        type=str,
        help="Path to a JSON config file defining cleaning rules."
    )

    parser.add_argument(
        "--uppercase",
        action="store_true",
        default=None,
        help="Make all text in CSV file uppercase"
    )

    return parser

def parse_args():
    parser = build_parser()
    return parser.parse_args()