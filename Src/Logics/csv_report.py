from Src.Core.abstract_report import abstract_report
from Src.Models.technical_map_model import technical_map_model
from Src.Core.validate import validate
from Src.Dtos.report_result_dto import report_result_dto
from Src.Core.exception import arguments_exception
import csv
from io import StringIO
from Src.Core.abc_data import unit
from Src.Logics.report_helper import extract_table

"""
Creating CSV report by technical map
"""
class csv_report(abstract_report):
    __map_model: unit
    mime_type = "text/csv"
    file_extension = "csv"
    is_binary = True

    def build(self, source: unit):
        """Creating data for response"""
        source = validate.validated_type(source, unit,
                                        "source", 
                                        "source must be unit",
                                        arguments_exception)
        self.__map_model = source
        header, rows = extract_table(self.__map_model)
        buffer = StringIO()
        writer = csv.writer(buffer)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)

        result = report_result_dto()
        result.binary = [buffer.getvalue().encode("utf-8-sig")]
        return result