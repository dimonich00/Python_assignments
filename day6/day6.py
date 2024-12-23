import os
import csv
import time
import argparse
from Bio import Entrez


def get_data(database, term, number):
    Entrez.email = "gabor@szabgab.com"

    handle = Entrez.esearch(db=database, term=term, retmax=number)
    search_result = Entrez.read(handle)
    handle.close()

    total_count = search_result["Count"]
    ids = search_result["IdList"]

    filenames = []

    for id in ids:
        handle = Entrez.efetch(
            db=database, id=id, rettype="fasta", retmode="text")
        data = handle.read()
        handle.close()

        filename = f"{database}_{id}.gb"
        with open(filename, "w") as file:
            file.write(data)
            filenames.append(filename)

    return filename, total_count


def write_summary(date, term, database, number, total_count):

    summary_file = "summary.csv"
    file_exists = os.path.exists(summary_file)

    with open(summary_file, "a", newline="") as csvfile:
        fieldnames = ["date", "database", "term",
                      "number_requested", "total_found"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write the header row
        writer.writerow({
            "date": date,
            "database": database,
            "term": term,
            "number_requested": number,
            "total_found": total_count
        })


def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI")
    parser.add_argument("--database", default="nucleotide")
    parser.add_argument("--term", required=True)
    parser.add_argument("--number", default=10)
    args = parser.parse_args()

    date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    filenames, total_count = get_data(args.database, args.term, args.number)

    print("date   , database   , term   , max   , total count   ")
    print(date, args.database, args.term, args.number, total_count)

    write_summary(date, args.term, args.database, args.number, total_count)


if __name__ == "__main__":
    main()
