from Src.Core.abstract_report import abstract_report
from Src.Models.technical_map_model import technical_map_model
from Src.Core.validate import validate
from Src.Dtos.report_result_dto import report_result_dto
from Src.Core.exception import arguments_exception
from html import escape
from Src.Logics.report_helper import extract_table
from Src.Core.abc_data import unit

"""
Creating HTML report by technical map
"""
class html_report(abstract_report):
    __map_model: unit

    def build(self, source: unit):
        """Creating data for response"""        
        source = validate.validated_type(source, unit,
                                        "source", 
                                        "source must be unit",
                                        arguments_exception)
        self.__map_model = source
        header, rows = extract_table(self.__map_model)
        html = '<table border="1">\n  <tr>'
        html += "".join(f"<th>{escape(h)}</th>" for h in header)
        html += "</tr>\n"
        for row in rows:
            html += "  <tr>"
            html += "".join(f"<td>{escape(str(c))}</td>" for c in row)
            html += "</tr>\n"
        html += "</table>"

        result = report_result_dto()
        result.text = html
        return result


    @property
    def mime_type(self) -> str:
        """Getter for mime_type"""
        return "text/html"

    @property
    def file_extension(self) -> str:
        """Getter for file_extension"""
        return "html"

    @property
    def is_binary(self) -> bool:
        """Getter for is_binary"""
        return False