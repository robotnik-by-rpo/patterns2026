from Src.Core.exception import arguments_exception, not_exist_exception
from fastapi.responses import JSONResponse
from fastapi import HTTPException, Request
from Src.Dtos.report_type_dto import report_type_enum
from fastapi import HTTPException, APIRouter, Response
from Src.Core.abstract_router import abstract_router
from Src.Logics.entity_factory import  entity_factory
from Src.Core.abc_data import unit
from Src.Logics.report_factory import report_factory
import json
from Src.Logics.observer import observer
from Src.Core.event_type import event_type


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
            observer.create(event_type.init_router_path(cls.__name__),
                            {"router": cls.__name__, "prefix": cls.__instance.prefix})
            return cls.__instance


    def _initing_paths(self):
        """Initing new paths for routers"""
        self.router.add_api_route("/get_report", self.get_report, methods=["GET"])
        self.router.add_api_route("/get", self.get_extensions, methods=["GET"])
        self.router.add_api_route("/get_default_report", self.get_default_report, methods=["GET"])

    async def get_default_report(self, request: Request, entity_type: str = "recipe", code: str = ""):
        """Format getting from settings.json"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path))

            entity = entity_factory().create(entity_type, code)
            report_impl = self.__factory.create_default()   
            result = report_impl.build(entity)

            observer.create(event_type.get_table_extension(entity_type, report_impl.mime_type),
                            {"domain": entity_type, "code": code, "format": report_impl.file_extension})

            if report_impl.is_binary:
                return Response(
                    content=result.binary[0],
                    media_type=report_impl.mime_type,
                    headers={
                        "Content-Disposition":
                            f'attachment; filename="report.{report_impl.file_extension}"'
                    }
                )
            return Response(content=result.text, media_type=report_impl.file_extension)
        except (arguments_exception, not_exist_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))

    async def get_report(self, request: Request, format: str = "TXT", entity_type: str = "recipe", code: str = ""):
        """Getting a report by endpoint /api/get_report"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path))

            fmt = report_type_enum.from_string(format)
            entity = entity_factory().create(entity_type, code)
            observer.create(event_type.get_table_extension(entity_type, format),
                            {"domain": entity_type, "code": code, "extension": format})

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

    async def get_extensions(self, request: Request):
        """Getting all formats report"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path))
            observer.create(event_type.get_extenstions())
            return JSONResponse(
                            content={"extensions": [type_.name for type_ in report_type_enum]},
                            media_type="application/json")
        except (arguments_exception, not_exist_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        
    