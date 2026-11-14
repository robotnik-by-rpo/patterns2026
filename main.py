from Src.Logics.storage_manager import storage_manager
from Src.Logics.report_factory import report_factory
from fastapi import FastAPI
from Src.Logics.settings_manager import setting_manager
from Src.API.router import server_API
import uvicorn


app = FastAPI()

setting_manager().load("settings.json") 
store = storage_manager()
server = server_API()
app.include_router(server_API().api)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)