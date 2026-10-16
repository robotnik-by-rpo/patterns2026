from Src.Core.abstract_report import abstract_report
from Src.Models.technical_map_model import technical_map_model
from Src.Core.validate import validate
from Src.Dtos.report_result_dto import report_result_dto
from Src.Core.exception import arguments_exception
from Src.Logics.report_helper import extract_table
from Src.Core.abc_data import unit

"""
Creating Markdown report by technical map
"""
class md_report(abstract_report):
    __map_model: unit
    mime_type = "text/markdown"
    file_extension = "md"
    is_binary = True
    def build(self, source: unit):
        """Creating data for response"""
        source = validate.validated_type(source, unit,
                                        "source", 
                                        "source must be unit",
                                        arguments_exception)
        self.__map_model = source
        
        header, rows = extract_table(self.__map_model)
        table = "| " + " | ".join(header) + " |\n"
        table += "|" + "|".join(["---"] * len(header)) + "|\n"
        for row in rows:
            table += "| " + " | ".join(str(x) for x in row) + " |\n"

        result = report_result_dto()
        result.binary = [table.encode("utf-8")]        
        return result