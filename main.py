from Src.Logics.storage_manager import storage_manager
from Src.Logics.report_factory import report_factory
from fastapi import FastAPI, Response, HTTPException
from Src.Models.technical_map_model import technical_map_model
from Src.Dtos.report_type_dto import report_type_enum
from Src.Core.exception import not_exist_exception
from Src.Core.exception import arguments_exception
from Src.Core.abc_data import unit
from Src.Logics.settings_manager import setting_manager
import uvicorn


app = FastAPI()

setting_manager().load("settings.json") 
store = storage_manager()
store.convert()

factory = report_factory()


def _find_entity(entity_type: str, code: str) -> unit:
    """Returning unit (technical map / nomenclature / unit of measurement)"""
    t = entity_type.strip().lower()

    if t in ("recipe", "technical_map"):
        tm = technical_map_model.create_technical_map()
        if code in ("", "*", "all", tm.id, tm.name):
            return tm
        raise not_exist_exception("code", f"recipe '{code}' not found")

    if t == "nomenclature":
        for _, items in store.nomenclatures.items():
            if code in items:
                return items[code]
        raise not_exist_exception("code", f"nomenclature '{code}' not found")

    if t in ("unit", "unit_of_measurement"):
        for _, items in store.units_of_measurement.items():
            if code in items:
                return items[code]
        raise not_exist_exception("code", f"unit '{code}' not found")

    raise arguments_exception("type", f"unknown type: {entity_type}")


def _build_response(report, source: unit, fmt: report_type_enum) -> Response:
    result = report.build(source)

    if fmt in (report_type_enum.CSV, report_type_enum.MD):
        ext = "csv" if fmt is report_type_enum.CSV else "md"
        mime = "text/csv; charset=utf-8" if fmt is report_type_enum.CSV \
               else "text/markdown; charset=utf-8"
        return Response(
            content=result.binary[0] if result.binary else result.text.encode("utf-8"),
            media_type=mime,
            headers={"Content-Disposition": f'attachment; filename="report.{ext}"'},
        )

    mime = {
        report_type_enum.TXT:  "text/plain; charset=utf-8",
        report_type_enum.XML:  "application/xml; charset=utf-8",
        report_type_enum.HTML: "text/html; charset=utf-8",
    }[fmt]
    return Response(content=result.text, media_type=mime)


@app.get("/api/get_report")
def get_report(format: str = "TXT", type: str = "recipe", code: str = ""):
    try:
        fmt = report_factory.parse_format(format)
        source = _find_entity(type, code)
        report = factory.create(fmt)
        return _build_response(report, source, fmt)
    except (arguments_exception, not_exist_exception) as ex:
        raise HTTPException(status_code=400, detail=str(ex))


@app.get("/api/get_default_report")
def get_default_report(type: str = "recipe", code: str = ""):
    """Format getting from settings.json"""
    try:
        source = _find_entity(type, code)
        report = factory.create_default()
        fmt = report_factory.parse_format(factory.settings.response_format)
        return _build_response(report, source, fmt)
    except (arguments_exception, not_exist_exception) as ex:
        raise HTTPException(status_code=400, detail=str(ex))    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)