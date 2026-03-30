import json
from pathlib import Path
from src.logger import get_logger

logger = get_logger("config")

def load_and_merge_config(args):
    """
    Load config.json (if provided) and merge it with CLI flags.
    CLI flags always override config file values.
    """

    # Load config file if provided
    config_data = {}
    if args.config:
        config_path = Path(args.config)
        logger.info(f"Loading config file: {config_path}")
        with open(config_path, "r") as f:
            config_data = json.load(f)

    # Convert CLI flags into a dictionary
    cli_data = {
        "drop_missing": args.drop_missing,
        "fill_missing": args.fill_missing,
        "strip_whitespace": args.strip_whitespace,
        "dedupe": args.dedupe
    }

    # Merge config + CLI (CLI overrides)
    final_plan = config_data.copy()

    for key, value in cli_data.items():
        if value is not None: # overrides only if user explicitly passed the flag
            final_plan[key] = value

    logger.debug(f"Merged cleaning plan: {final_plan}")
    return final_plan