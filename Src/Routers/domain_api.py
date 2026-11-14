from fastapi import HTTPException, APIRouter, Request, Response, Body
from Src.Core.exception import arguments_exception, not_exist_exception, operation_exception
from Src.Core.abstract_router import abstract_router
from Src.Logics.storage_manager import storage_manager
from Src.Logics.convert_factory import convert_factory
from fastapi.responses import JSONResponse
from Src.Logics.domain_restapi_factory import domain_restapi_factory
import json

class domain_router(abstract_router):

    __convert_factory: convert_factory = convert_factory()
    __domain_api_factory: domain_restapi_factory = domain_restapi_factory()

    def __new__(cls):
        """Singletone"""
        if not hasattr(cls, '_domain_router__instance'):
            cls.__instance = super().__new__(cls)
            cls.__instance.prefix  = "/domain"
            cls.__instance.router = APIRouter(prefix=cls.__instance.prefix, tags=["domain"])
            cls.__instance._initing_paths()
        return cls.__instance

    def _initing_paths(self):
        """Initining paths for route"""
        self.router.add_api_route("/storage_manager", self.get_storage_manager, methods=["GET"])
        self.router.add_api_route("/{domain_id}", self.get_domain, methods=["GET"])
        self.router.add_api_route("", self.post_domain, methods=["POST"])
        self.router.add_api_route("/{domain_id}", self.put_domain, methods=["PUT"])
        self.router.add_api_route("/{domain_id}", self.delete_domain, methods=["DELETE"])
        self.router.add_api_route("/{domain_id}", self.patch_domain, methods=["PATCH"])

    def get_storage_manager(self):
        """Getting all domain from storage manager"""
        try:
            raw_dict = self.__convert_factory.serialize(storage_manager())
            return Response(
                            content=json.dumps(raw_dict, ensure_ascii=False, indent=2),
                            media_type="application/json")
        
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def post_domain(self, data: dict = Body(...)):
        """Adding new domain"""
        try:
            obj = self.__convert_factory.deserialize(data)
            self.__domain_api_factory.create(obj)
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
            new_obj = self.__convert_factory.deserialize(data)
            updated = self.__domain_api_factory.update(domain_id, new_obj)
            raw = self.__convert_factory.serialize(updated)
            return JSONResponse(content=raw, status_code=200)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except (arguments_exception, operation_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def delete_domain(self, domain_id: str, force: bool = False):
        """Deleting a domain"""
        try:
            self.__domain_api_factory.delete(domain_id, force)
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
            current = self.__domain_api_factory.read(domain_id)
            current_raw = self.__convert_factory.serialize(current)
            if not isinstance(data, dict) or not isinstance(current_raw, dict):
                raise arguments_exception("body", "patch body must be a JSON object")

            merged = {**current_raw, **data}
            new_obj = self.__convert_factory.deserialize(merged)
            updated = self.__domain_api_factory.update(domain_id, new_obj)
            raw = self.__convert_factory.serialize(updated)
            return JSONResponse(content=raw, status_code=200)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except (arguments_exception, operation_exception) as ex:
            raise HTTPException(status_code=400, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))

    async def get_domain(self, domain_id: str):
        """Getting a domain"""
        try:
            obj = self.__domain_api_factory.read(domain_id)
            raw = self.__convert_factory.serialize(obj)
            return JSONResponse(content=raw, status_code=200)
        except not_exist_exception as ex:
            raise HTTPException(status_code=404, detail=str(ex))
        except Exception as ex:
            raise HTTPException(status_code=500, detail=str(ex))
    

