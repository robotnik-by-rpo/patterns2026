from Src.Models.transaction_model import transaction_model
from Src.Dtos.osv_dto import osv_row_dto, osv_report_dto
from Src.Dtos.filter_dto import filter_dto
from Src.Logics.prototype import prototype
from Src.Logics.storage_manager import storage_manager
from datetime import datetime

"""
Service for building OSV report from transactions.
Builds turnover OSV for a period.
"""
class osv_service:
    __storage = storage_manager()

    def build(self, 
              start_date: datetime,
              end_date: datetime,
              filter_obj: filter_dto | None = None,
        ) -> osv_report_dto:
        """Method for collecting for period"""
        transactions = list(self.__storage.transactions.values())

        if filter_obj and filter_obj.filters:
            transactions = self.__apply_nomenclature_filter(transactions, filter_obj)

        opening_map = self.__sum_nomenclature([t for t in transactions 
                                               if t.period is not None and 
                                               t.period < start_date])
        
        period_tx = [t for t in transactions 
                     if t.period is not None and 
                     start_date <= t.period <= end_date]
        
        income_map, expense_map = self.__rev_nomenclature(period_tx)

        all_ids = set(opening_map) | set(income_map) | set(expense_map)

        rows: list[osv_row_dto] = []

        for nom_id in all_ids:
            opening = opening_map.get(nom_id, (0.0, ""))[0]
            name = (
                opening_map.get(nom_id)
                or income_map.get(nom_id)
                or expense_map.get(nom_id)
            )[1]
            income = income_map.get(nom_id, (0.0, ""))[0]
            expense = expense_map.get(nom_id, (0.0, ""))[0]
            rows.append(
                osv_row_dto(
                    id=nom_id,
                    name=name,
                    opening_balance=opening,
                    income=income,
                    expense=expense,
                    closing_balance=opening + income - expense,
                )
            )

        return osv_report_dto(rows)


    def __sum_nomenclature(self, 
                           ts: list[transaction_model]
    ) -> dict[str, tuple[float, str]]:
        """Method for summing value by nomenclature"""
        result: dict[str, tuple[float, str]] = {}

        for t in ts:
            nom = t.nomenclature
            prev, _ = result.get(nom.id, (0.0, nom.name))
            result[nom.id] = (prev + float(t.value), nom.name)

        return result
    
    def __rev_nomenclature(self, 
                           ts: list[transaction_model]
    ) -> tuple[dict[str, tuple[float, str]], dict[str, tuple[float, str]]]:
        """Method for getting income and expense"""
        income: dict[str, tuple[float, str]] = {}
        expense: dict[str, tuple[float, str]] = {}

        for t in ts:
            nom = t.nomenclature
            key = nom.id
            if t.value >= 0:
                prev, _ = income.get(key, (0.0, nom.name))
                income[key] = (prev + float(t.value), nom.name)
            else:
                prev, _ = expense.get(key, (0.0, nom.name))
                expense[key] = (prev + abs(float(t.value)), nom.name)
        return income, expense


    def __apply_nomenclature_filter(
        self, txs: list[transaction_model], filter_obj: filter_dto
    ) -> list[transaction_model]:
        """Filter by field nomenclature through prototype"""
        noms = list({t.nomenclature.id: t.nomenclature for t in txs}.values())
        filtered_ids = {
            n.id for n in prototype(noms).clone(filter_obj).data
        }
        return [t for t in txs if t.nomenclature.id in filtered_ids]