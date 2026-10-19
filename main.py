from Src.Logics.storage_manager import storage_manager
from Src.Logics.report_factory import report_factory
from fastapi import FastAPI, Response, HTTPException
from Src.Models.technical_map_model import technical_map_model
from Src.Dtos.report_type_dto import report_type_enum
from Src.Core.exception import not_exist_exception
from Src.Core.exception import arguments_exception
from Src.Core.abc_data import unit
from Src.Logics.settings_manager import setting_manager
from Src.Logics.entity_factory import  entity_factory
import uvicorn


app = FastAPI()

setting_manager().load("settings.json") 
store = storage_manager()
store.convert()

factory = report_factory()


def _build_response(entity: unit, fmt: report_type_enum) -> Response:
    """Method for creating response"""
    report_impl = factory.create(fmt)
    result = report_impl.build(entity)

    if report_impl.is_binary:
        return Response(
            content=result.binary[0],
            media_type=report_impl.mime_type,
            headers={
                "Content-Disposition":
                    f'attachment; filename="report.{report_impl.file_extension}"'
            }
        )
    return Response(content=result.text, media_type=report_impl.mime_type)

@app.get("/api/get_report")
def get_report(format: str = "TXT", entity_type: str = "recipe", code: str = ""):
    """Getting a report by endpoint /api/get_report"""
    try:
        fmt = report_type_enum.from_string(format)
        entity = entity_factory().create(entity_type, code)
        return _build_response(entity, fmt)
    except (arguments_exception, not_exist_exception) as ex:
        raise HTTPException(status_code=400, detail=str(ex))


@app.get("/api/get_default_report")
def get_default_report(entity_type: str = "recipe", code: str = ""):
    """Format getting from settings.json"""
    try:
        entity = entity_factory().create(entity_type, code)
        report_impl = factory.create_default()   # ← берём из настроек
        result = report_impl.build(entity)

        if report_impl.is_binary:
            return Response(
                content=result.binary[0],
                media_type=report_impl.mime_type,
                headers={
                    "Content-Disposition":
                        f'attachment; filename="report.{report_impl.file_extension}"'
                }
            )
        return Response(content=result.text, media_type=report_impl.mime_type)
    except (arguments_exception, not_exist_exception) as ex:
        raise HTTPException(status_code=400, detail=str(ex))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)