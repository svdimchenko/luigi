import luigi
import csv
from openpyxl import Workbook
from pathlib import Path


class Csv2XlsReport(luigi.Task):
    data_dir: str = luigi.Parameter(default="data/")
    csv_filename: str = luigi.Parameter()
    report_file: str = luigi.Parameter()

    def run(self):
        wb = Workbook()
        ws = wb.active
        input_file = Path(self.data_dir) / self.csv_filename
        output_file = Path(self.data_dir) / self.report_file
        with open(input_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                ws.append(row)
        wb.save(output_file)


if __name__ == "__main__":
    luigi.build([Csv2XlsReport(csv_filename="source_file.csv", report_file="simple_report.xlsx")])
