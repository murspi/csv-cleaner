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

    if plan.get("uppercase"):
        logger.info("Converting all text to uppercase")
        df = df.apply(lambda col: col.map(lambda x: x.upper() if isinstance(x, str) else x))

    if "columns" in plan:
        for col_name, col_rules in plan["columns"].items():

            if col_name not in df.columns:
                logger.warning(f"Column '{col_name}' specified in config but not found in CSV.")
                continue

            logger.info(f"Applying column-specific rules to column {col_name}")

            col = df[col_name]

            if col_rules.get("strip_whitespace"):
                logger.info(f"- strip_whitespace on '{col_name}'")
                df[col_name] = col.map(lambda x: x.strip() if isinstance(x, str) else x)

            if col_rules.get("uppercase"):
                logger.info(f"- uppercase on '{col_name}'")
                df[col_name] = col.map(lambda x: x.upper() if isinstance(x, str) else x)

            if col_rules.get("fill_missing"):
                fill_value = col_rules["fill_missing"]
                logger.info(f" - fill_missing on '{col_name}' with '{fill_value}'")
                df[col_name] = col.fillna(fill_value)

            if col_rules.get("drop_missing"):
                logger.info(f" - drop_missing rows where '{col_name}' is null")
                df = df[df[col_name].notna()]

            if col_rules.get("dedupe"):
                logger.info(f"- dedupe based on '{col_name}'")
                df = df.drop_duplicates(subset=[col_name])

    df.to_csv(output_path, index=False)
            