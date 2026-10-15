from Src.Core.abstract_report_factory import abstract_report_factory
from Src.Core.abstract_report import abstract_report
from Src.Dtos.report_type_dto import report_type_enum
from Src.Logics.text_report import text_report
from Src.Core.exception import arguments_exception
from Src.Logics.settings_manager import setting_manager
from Src.Models.settings_model import settings_model
from Src.Core.validate import validate
from Src.Logics.csv_report import csv_report
from Src.Logics.html_report import html_report
from Src.Logics.xml_report import xml_report
from Src.Logics.md_report import md_report

"""
Implementation factory for building reports
"""
class report_factory(abstract_report_factory):
    # type report and his implementation
    __mapping: dict[report_type_enum, abstract_report] = {}


    __FORMAT_ALIASES: dict[str, report_type_enum] = {
        "TXT":      report_type_enum.TXT,
        "CSV":      report_type_enum.CSV,
        "MD":       report_type_enum.MD,
        "MARKDOWN": report_type_enum.MD,
        "XML":      report_type_enum.XML,
        "HTML":     report_type_enum.HTML,
    }

    def __init__(self):
        self.__settings = setting_manager().settings
        if not self.__mapping:                 
            self.__mapping[report_type_enum.TXT] = text_report()
            self.__mapping[report_type_enum.CSV] = csv_report()
            self.__mapping[report_type_enum.MD] = md_report()
            self.__mapping[report_type_enum.XML] = xml_report()
            self.__mapping[report_type_enum.HTML] = html_report()

    def create(self, report_type: report_type_enum) -> abstract_report:
        if report_type not in self.__mapping.keys():
            raise arguments_exception("report type","report type didn't generete")
        return self.__mapping[report_type]
    
    @property
    def settings(self) -> settings_model:
        """Getter for settings"""
        return  self.__settings
    
    @settings.setter
    def settings(self, new_settings: settings_model):
        """Setter for settings"""
        self.__settings = validate.validated_null_value(new_settings,
                                                        "new settings",
                                                        "new settings must be not None",
                                                        arguments_exception)
    @classmethod
    def parse_format(cls, fmt: str) -> report_type_enum:
        key = str(fmt).strip().upper()
        if key not in cls.__FORMAT_ALIASES:
            raise arguments_exception("format", f"unsupported format: {fmt}")
        return cls.__FORMAT_ALIASES[key]

    def create_default(self):
        fmt_str = self.settings.response_format
        return self.create(self.parse_format(fmt_str))