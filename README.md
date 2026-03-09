# CSV Duplicate Cleaner

A simple Python command-line tool to remove duplicate entries from CSV files.

## Features

- Removes duplicate rows from CSV files
- Preserves the original file
- Provides statistics on duplicates removed
- Command-line interface with optional output path

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic usage (saves cleaned file with "_cleaned" suffix):

```bash
python main.py your_file.csv
```

### Specify custom output file:

```bash
python main.py input.csv -o cleaned_output.csv
```

### Using long option:

```bash
python main.py input.csv --output cleaned_output.csv
```

## Examples

```bash
# Clean a CSV file in the current directory
python main.py data.csv

# Clean a CSV file with a custom output path
python main.py messy_data.csv -o clean_data.csv

# Clean a CSV file from a different directory
python main.py /path/to/input.csv -o /path/to/output.csv
```

## Output

The tool will display:
- Number of original rows
- Number of rows after cleaning
- Number of duplicates removed
- Path where the cleaned file was saved

## Requirements

- Python 3.7+
- pandas library

## Error Handling

The tool handles common errors such as:
- File not found
- Empty CSV files
- Invalid CSV format
- Permission issues

## License

This project is open source and available under the MIT License.