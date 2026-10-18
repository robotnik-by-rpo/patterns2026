from Src.Core.abc_data import unit
from Src.Core.exception import arguments_exception
from Src.Core.abstract_reportable import abstract_reportable


def extract_table(source: unit) -> tuple[list[str], list[list]]:
    """
    Return (header, rows) for some object of unit..
    """
    if not isinstance(source, abstract_reportable):
        raise arguments_exception(
            "source",
            f"{type(source).__name__} doesn't support report"
        )
    return source.report_header(), source.report_rows()