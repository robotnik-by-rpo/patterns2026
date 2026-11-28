from fastapi import HTTPException, APIRouter, Request, Response, Body
from Src.Core.exception import arguments_exception, not_exist_exception, operation_exception
from Src.Core.abstract_router import abstract_router
from Src.Logics.storage_manager import storage_manager
from Src.Logics.convert_factory import convert_factory
from fastapi.responses import JSONResponse
from Src.Logics.domain_restapi import domain_restapi
import json
from Src.Logics.factory_domain_type import factory_domain_type
from Src.Logics.prototype import prototype
from Src.Logics.osv_service import osv_service
from Src.Dtos.filter_dto import filter_dto
from datetime import datetime
from Src.Logics.observer import observer
from Src.Core.event_type import event_type

class domain_router(abstract_router):

    __convert_factory: convert_factory = convert_factory()
    __domain_restapi: domain_restapi = domain_restapi()
    __domain_type_factory: factory_domain_type = factory_domain_type()
    __osv_service: osv_service = osv_service()

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_domain_router__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.prefix  = "/domain"
            cls.__instance.router = APIRouter(prefix=cls.__instance.prefix, tags=["domain"])
            cls.__instance._initing_paths()
            observer.create(event_type.init_router_path(cls.__name__),
                            {"router": cls.__name__, "prefix": cls.__instance.prefix})
        return cls.__instance

    def _initing_paths(self):
        """Initining paths for route"""
        self.router.add_api_route("/storage_manager", self.get_storage_manager, methods=["GET"])
        self.router.add_api_route("/{domain_id}", self.get_domain, methods=["GET"])
        self.router.add_api_route("", self.post_domain, methods=["POST"])
        self.router.add_api_route("/{domain_id}", self.put_domain, methods=["PUT"])
        self.router.add_api_route("/{domain_id}", self.delete_domain, methods=["DELETE"])
        self.router.add_api_route("/{domain_id}", self.patch_domain, methods=["PATCH"])
        self.router.add_api_route("/filter/{domain_type}", self.filter_domain, methods=["POST"])
        self.router.add_api_route("/osv/{domain_type}", self.post_osv, methods=["POST"])

    async def filter_domain(self, domain_type: str, request: Request) -> None:
        """Filter dto domains throught filter"""
        try:
            data = await request.json()

            observer.create(event_type.web_request(request.method, request.url.path),data)

            filter: filter_dto = self.__get_filter(data)
            items = self.__get_items_domain(domain_type)
            proto = self.__get_proto(items, filter)
            filtered = proto.data
            raw = self.__convert_factory.serialize(filtered)

            return JSONResponse(content=raw, status_code=200)
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def post_osv(self, domain_type: str, request: Request) -> None:
        """Filter dto domains throught filter and return osv"""
        try:
            data = await request.json()

            observer.create(event_type.web_request(request.method, request.url.path),data)

            start = datetime.fromisoformat(data.pop("start_date"))
            end = datetime.fromisoformat(data.pop("end_date"))
            filter: filter_dto = self.__get_filter(data)

            report = self.__osv_service.build(start, end, filter)
            result = self.__convert_factory.serialize(report.rows)

            observer.create(event_type.post_osv_report())

            return JSONResponse(content=result, status_code=200)
        except Exception as ex:
            raise HTTPException(status_code=400, detail=str(ex))

    def __get_items_domain(self, domain_type: str) -> list[any]:
        """Method for getting items domain from storage manager"""
        if domain_type in self.__domain_type_factory:
            return self.__domain_type_factory.convert(domain_type)
    
        raise HTTPException(status_code=400, detail="Unknown domain type")
    
    def __get_proto(self, items: list[any], filter: filter_dto) -> prototype:
        """Method for getting prototype"""
        return prototype(items).clone(filter)
        

    def __get_filter(self, data: dict) -> filter_dto:
        """Method for getting filter dto"""
        for item in data.get("filters", []):
                if isinstance(item, dict) and "__class__" not in item:
                    item["__class__"] = "filter_item_dto"
        return self.__convert_factory.deserialize({"__class__": "filter_dto", **data})

    async def get_storage_manager(self, request: Request):
        """Getting all domain from storage manager"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path))

            raw_dict = self.__convert_factory.serialize(storage_manager())
            observer.create(event_type.get_domains())        

            return Response(
                            content=json.dumps(raw_dict, ensure_ascii=False, indent=2),
                            media_type="application/json")
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def post_domain(self, request: Request, data: dict = Body(...)):
        """Adding new domain"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path), data)
            obj = self.__convert_factory.deserialize(data)
            self.__domain_restapi.create(obj)
            observer.create(event_type.post_domain(type(obj).__name__),
                            {"id": obj.id, "name": getattr(obj, "name", "")})
            
            raw = self.__convert_factory.serialize(obj)
            return JSONResponse(content=raw, status_code=201)
        except (arguments_exception, operation_exception, not_exist_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def put_domain(self, domain_id: str, request: Request):
        """Putting a domain"""
        try:
            data = await request.json()
            observer.create(event_type.web_request(request.method, request.url.path), data)

            new_obj = self.__convert_factory.deserialize(data)
            updated = self.__domain_restapi.update(domain_id, new_obj)
            observer.create(event_type.put_domain(type(updated).__name__),
                            {"id": updated.id})
            raw = self.__convert_factory.serialize(updated)
            return JSONResponse(content=raw, status_code=200)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except (arguments_exception, operation_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def delete_domain(self, request: Request, domain_id: str, force: bool = False):
        """Deleting a domain"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path))
            self.__domain_restapi.delete(domain_id, force)
            observer.create(event_type.delete_domain(domain_id),
                            {"id": domain_id, "is_force": force})

            return Response(status_code=204)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except operation_exception as ex:
            raise HTTPException(status_code=409, detail=str(ex))
        except arguments_exception as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def patch_domain(self, domain_id: str, request: Request):
        """Patching a domain"""
        try:
            data = await request.json()
            observer.create(event_type.web_request(request.method, request.url.path), data)
            
            current = self.__domain_restapi.read(domain_id)
            current_raw = self.__convert_factory.serialize(current)
            if not isinstance(data, dict) or not isinstance(current_raw, dict):
                raise arguments_exception("body", "patch body must be a JSON object")

            merged = {**current_raw, **data}
            new_obj = self.__convert_factory.deserialize(merged)
            updated = self.__domain_restapi.update(domain_id, new_obj)

            observer.create(event_type.patch_domain(type(updated).__name__),
                            {"id": domain_id, "name": getattr(updated, "name", "")})
            
            raw = self.__convert_factory.serialize(updated)
            return JSONResponse(content=raw, status_code=200)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except (arguments_exception, operation_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def get_domain(self, request: Request, domain_id: str):
        """Getting a domain"""
        try:
            observer.create(event_type.web_request(request.method, request.url.path))


            obj = self.__domain_restapi.read(domain_id)
            raw = self.__convert_factory.serialize(obj)

            observer.create(event_type.get_domain(type(obj).__name__),
                            {"id": obj.id, "name": getattr(obj, "name", "")})

            return JSONResponse(content=raw, status_code=200)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))
    

