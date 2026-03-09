#!/usr/bin/env python3
"""
CSV Duplicate Cleaner

A command-line tool to remove duplicate entries from CSV files.
"""

import argparse
import pandas as pd
import sys
from pathlib import Path


def clean_csv_duplicates(input_path: str, output_path: str = None) -> str:
    """
    Clean duplicate entries from a CSV file.

    Args:
        input_path: Path to the input CSV file
        output_path: Path to save the cleaned CSV file. If None, appends '_cleaned' to input filename.

    Returns:
        Path to the output file

    Raises:
        FileNotFoundError: If input file doesn't exist
        pd.errors.EmptyDataError: If CSV file is empty
        Exception: For other pandas-related errors
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_path)

        # Check if file is empty
        if df.empty:
            raise pd.errors.EmptyDataError("The CSV file is empty")

        # Get original row count
        original_count = len(df)

        # Remove duplicate rows
        df_cleaned = df.drop_duplicates()

        # Get cleaned row count
        cleaned_count = len(df_cleaned)

        # Determine output path
        if output_path is None:
            input_file = Path(input_path)
            output_path = str(input_file.parent / f"{input_file.stem}_cleaned{input_file.suffix}")

        # Save the cleaned CSV
        df_cleaned.to_csv(output_path, index=False)

        print(f"Successfully cleaned CSV file!")
        print(f"   Original rows: {original_count}")
        print(f"   Cleaned rows: {cleaned_count}")
        print(f"   Duplicates removed: {original_count - cleaned_count}")
        print(f"   Output saved to: {output_path}")

        return output_path

    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        sys.exit(1)
    except pd.errors.EmptyDataError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        sys.exit(1)


def main():
    """Main entry point for the CSV cleaner CLI."""
    parser = argparse.ArgumentParser(
        description="Clean duplicate entries from CSV files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py data.csv
  python main.py input.csv -o cleaned_output.csv
  python main.py /path/to/file.csv --output /path/to/cleaned.csv
        """
    )

    parser.add_argument(
        'input_file',
        help='Path to the input CSV file'
    )

    parser.add_argument(
        '-o', '--output',
        help='Path for the output cleaned CSV file (optional)',
        default=None
    )

    args = parser.parse_args()

    # Clean the CSV file
    clean_csv_duplicates(args.input_file, args.output)


if __name__ == "__main__":
    main()