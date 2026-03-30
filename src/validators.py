from pathlib import Path
from src.logger import get_logger
import sys

logger = get_logger("validators")

def validate_path(args):
    """
    Validate input/output/config paths before running the cleaning pipeline
    """

    # Validate input file exists
    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"ERROR: Input file does not exist: {input_path}")
        sys.exit(1)

    # Validate input file is a CSV
    if input_path.suffix.lower() != ".csv":
        logger.error(f"ERROR: Input file must be a .csv file, got: {input_path.suffix}")
        sys.exit(1)

    # Validate output directory exists
    output_path = Path(args.output)
    output_dir = output_path.parent

    # Allow writing to current directory (".")
    if str(output_dir) not in (".", "") and not output_dir.exists():
        logger.error(f"ERROR: Output directory does not exist: {output_dir}")
        sys.exit(1)

    # Validate config exists (if provided)
    if args.config:
        config_path = Path(args.config)
        if not config_path.exists():
            logger.error(f"ERROR: Config file does not exist {config_path}")
            sys.exit(1)

logger.info("All paths validated successfully")