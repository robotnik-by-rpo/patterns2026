from Src.Core.abstract_report import abstract_report
from Src.Models.technical_map_model import technical_map_model
from Src.Core.validate import validate
from Src.Dtos.report_result_dto import report_result_dto
from Src.Core.exception import arguments_exception
from xml.sax.saxutils import escape
from Src.Core.abc_data import unit
from Src.Logics.report_helper import extract_table

"""
Creating XML report by technical map
"""
class xml_report(abstract_report):
    __map_model: unit

    def build(self, source: unit):
        source = validate.validated_type(source, unit,
                                        "source", 
                                        "source must be unit",
                                        arguments_exception)
        self.__map_model = source
  
        header, rows = extract_table(self.__map_model)
        data = '<?xml version="1.0" encoding="UTF-8"?>\n<report>\n'
        for row in rows:
            attrs = " ".join(
                f'{header[i].lower()}="{escape(str(row[i]))}"'
                for i in range(len(header))
            )
            data += f"  <row {attrs}/>\n"
        data += "</report>"

        result = report_result_dto()
        result.text = data
        return result