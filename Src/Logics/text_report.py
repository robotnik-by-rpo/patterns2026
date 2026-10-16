from Src.Core.abstract_report import abstract_report
from Src.Models.technical_map_model import technical_map_model
from Src.Core.validate import validate
from Src.Dtos.report_result_dto import report_result_dto
from Src.Core.exception import arguments_exception
from Src.Core.abc_data import unit
from Src.Logics.report_helper import extract_table

"""
Creating text report by technical map
"""
class text_report(abstract_report):
    __map_model: unit
    mime_type = "text/plain"
    file_extension = "txt"
    is_binary = False

    def build(self, source: unit):
        """Creating data for response"""
        source = validate.validated_type(source, unit,
                                 "source", "source must be unit",
                                 arguments_exception)
        self.__map_model = source

        header, rows = extract_table(self.__map_model)
        lines = [" | ".join(header)]
        for row in rows:
            lines.append(" | ".join(str(x) for x in row))

        result = report_result_dto()
        result.text = "\n".join(lines)
        return result