# csv_cleaner_plain.py
import csv
import sys

def clean_csv_plain(input_path, output_path, delimiter=',', quotechar='"'):
    with open(input_path, newline='', encoding='utf-8') as fin:
        reader = csv.reader(fin, delimiter=delimiter, quotechar=quotechar)
        rows = []
        for r in reader:
            # skip empty rows
            if not any(cell.strip() for cell in r):
                continue
            # strip spaces
            rows.append([cell.strip() for cell in r])

    # Optional: fix header duplicates by appending _1, _2 ...
    if rows:
        header = rows[0]
        seen = {}
        new_header = []
        for h in header:
            h_clean = h.strip() or "column"
            if h_clean in seen:
                seen[h_clean] += 1
                h_clean = f"{h_clean}_{seen[h_clean]}"
            else:
                seen[h_clean] = 0
            new_header.append(h_clean)
        rows[0] = new_header

    with open(output_path, 'w', newline='', encoding='utf-8') as fout:
        writer = csv.writer(fout, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(rows)

if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv)>1 else "input.csv"
    output_path = sys.argv[2] if len(sys.argv)>2 else "cleaned.csv"
    clean_csv_plain(input_path, output_path)
    print("Saved cleaned file:", output_path)
