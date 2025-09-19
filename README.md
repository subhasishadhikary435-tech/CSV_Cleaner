# CSV Cleaner Package

This ZIP contains two simple CSV cleaner scripts and a sample CSV to help you get started.

## Files
- `csv_cleaner_pandas.py` — Cleaner using pandas (recommended for most cases).
- `csv_cleaner_plain.py` — Cleaner using Python's `csv` module (no pandas required).
- `sample_input.csv` — A small messy sample CSV with common issues.
- `requirements.txt` — Python packages to install.
- `README.md` — This file.

## Quick usage

### Using pandas script (recommended)
1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Run the cleaner:
   ```
   python csv_cleaner_pandas.py sample_input.csv cleaned_pandas.csv
   ```
3. Open `cleaned_pandas.csv` to inspect results.

### Using plain Python script
   ```
   python csv_cleaner_plain.py sample_input.csv cleaned_plain.csv
   ```

## Notes & tips
- If you have a date column with mixed formats, pass `date_cols=['date']` in the pandas cleaner call or edit the script accordingly.
- For very large CSVs, use pandas chunking (`chunksize`) or process in a streaming way.
- If quoting is inconsistent, try opening the file in a spreadsheet to see patterns, or use tools like OpenRefine.

## License
Use this code freely. No warranty. If you publish a blog post using this, a link back is appreciated :)
