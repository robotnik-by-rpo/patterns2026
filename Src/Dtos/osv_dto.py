"""
Class row for osv report
"""
class osv_row_dto:
    def __init__(
        self,
        id: str,
        name: str,
        opening_balance: float,
        income: float,
        expense: float,
        closing_balance: float,
    ):
        self.id = id
        self.name = name
        self.opening_balance = opening_balance
        self.income = income
        self.expense = expense
        self.closing_balance = closing_balance

"""
OSV report as list of rows
"""
class osv_report_dto:
    def __init__(self, rows: list[osv_row_dto] | None = None):
        self.rows = rows or []