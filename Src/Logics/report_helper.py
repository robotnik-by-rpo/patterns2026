from Src.Core.abc_data import unit
from Src.Core.exception import arguments_exception


def extract_table(source: unit) -> tuple[list[str], list[list]]:
    """
    Return (header, rows) for some object of unit..
    """
    if not (hasattr(source, "report_header") and hasattr(source, "report_rows")):
        raise arguments_exception(
            "source",
            f"{type(source).__name__} doesn't support report"
        )
    return source.report_header(), source.report_rows()