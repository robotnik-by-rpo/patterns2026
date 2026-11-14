from Src.Core.exception import arguments_exception, not_exist_exception
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from Src.Dtos.report_type_dto import report_type_enum
from fastapi import HTTPException, APIRouter, Response
from Src.Core.abstract_router import abstract_router
from Src.Logics.entity_factory import  entity_factory
from Src.Core.abc_data import unit
from Src.Logics.report_factory import report_factory
import json

class extension_router(abstract_router):
    __factory: report_factory = None


    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_extension_router__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.prefix = "" 
            cls.__instance.router = APIRouter(prefix=cls.__instance.prefix, tags=["extensions"])
            cls.__instance._initing_paths()
            cls.__instance.__factory = report_factory()
        return cls.__instance


    def _initing_paths(self):
        """Initing new paths for routers"""
        self.router.add_api_route("/get_report", self.get_report, methods=["GET"])
        self.router.add_api_route("/get", self.get_extensions, methods=["GET"])
        self.router.add_api_route("/get_default_report", self.get_default_report, methods=["GET"])

    def get_default_report(self, entity_type: str = "recipe", code: str = ""):
        """Format getting from settings.json"""
        try:
            entity = entity_factory().create(entity_type, code)
            report_impl = self.__factory.create_default()   
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

    def get_report(self, format: str = "TXT", entity_type: str = "recipe", code: str = ""):
        """Getting a report by endpoint /api/get_report"""
        try:
            fmt = report_type_enum.from_string(format)
            entity = entity_factory().create(entity_type, code)
            return self._build_response(entity, fmt)
        except (arguments_exception, not_exist_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        
    def _build_response(self, entity: unit, fmt: report_type_enum) -> Response:
        """Method for creating response"""
        report_impl = self.__factory.create(fmt)
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

    def get_extensions(self):
        """Getting all formats report"""
        try:
            return JSONResponse(
                            content={"extensions": [type_.name for type_ in report_type_enum]},
                            media_type="application/json")
        except (arguments_exception, not_exist_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        
    