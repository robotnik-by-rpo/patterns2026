from Src.Logics.prototype import prototype
from Src.Dtos.osv_dto import osv_row_dto, osv_report_dto

"""
Service for osv transaction
"""
class osv_service:
    def build(self, proto: prototype) -> osv_report_dto:
        rows: list[osv_row_dto] = []
        for obj in proto.data:
            h = sum(ord(c) for c in obj.id)
            opening = h % 100
            income = (h * 2) % 100
            expense = (h * 3) % 100
            rows.append(
                osv_row_dto(
                    id=obj.id,
                    name=getattr(obj, "name", ""),
                    opening_balance=opening,
                    income=income,
                    expense=expense,
                    closing_balance=opening + income - expense,
                )
            )
        return osv_report_dto(rows)