import pandas as pd
from pandas import DataFrame
from src.logger import get_logger

logger = get_logger("cleaner")

def clean_csv(input_path, output_path, plan):
    """
    Apply cleaning rules from 'plan' to the CSV at input_path
    and save the cleaned CSV to output_path.
    """
    
    logger.info(f"Loading CSV: {input_path}")
    df: DataFrame = pd.read_csv(input_path)

    logger.debug(f"Initial shape: {df.shape}")

    # Convert empty or whitespaces-only cells to NaN
    df = df.replace(r'^\s*$', pd.NA, regex=True)

    if plan.get("drop_missing"):
        logger.info("Dropping rows with missing values")
        df = df.dropna()

    if plan.get("fill_missing"):
        logger.info(f"Filling missing values with: {plan['fill_missing']}")
        df = df.fillna(plan["fill_missing"])

    if plan.get("strip_whitespace"):
        logger.info("Stripping whitespaces from string columns")
        df = df.apply(
            lambda col: col.map(
                lambda x: x.strip() if isinstance(x, str) else x
            )
        )

    if plan.get("dedupe"):
        df = df.drop_duplicates()

    df.to_csv(output_path, index=False)
