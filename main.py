from src.cli import build_parser
from src.validators import validate_path
from src.config import load_and_merge_config
from src.cleaner import clean_csv
from src.logger import get_logger

def main():
    logger = get_logger("main")

    logger.info("Starting CSV Cleaner Tool")

    # Parse CLI arguments
    parser = build_parser()
    args = parser.parse_args()

    logger.debug(f"Parsed arguments: {args}")

    # Validate paths
    validate_path(args)
    logger.info("Path validation passed")

    # Merge config + CLI flags into a final cleaning plan
    plan = load_and_merge_config(args)
    logger.debug(f"Final cleaning plan {plan}")

    # Run the cleaning pipeline
    clean_csv(args.input, args.output, plan)

    logger.info("CSV cleaned successfully!")

if __name__ == "__main__":
    main()