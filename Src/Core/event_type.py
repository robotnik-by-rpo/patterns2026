
""" 
Types messages for events
"""
class event_type:

    @staticmethod
    def get_domain(domain_name: str) -> str:
        return f"getting_{domain_name}"

    @staticmethod
    def change_settings() -> str:
        return "change_settings"
    
    @staticmethod
    def load_settings() -> str:
        return "load_settings"
    
    @staticmethod 
    def get_domains() -> str:
        return "getting_domains"
    
    @staticmethod
    def put_domain(class_name: str) -> str:
        return f"putting_{class_name}"
    
    @staticmethod
    def post_domain(new_domain: str) -> str:
        return f"posting_{new_domain}"
    
    @staticmethod
    def delete_domain(id_domain: str) -> str:
        return f"deleting_{id_domain}"
    
    @staticmethod
    def patch_domain(domain_name: str) -> str:
        return f"patching_{domain_name}"
    
    @staticmethod
    def get_table_extension(domain_name: str, extension: str) -> str:
        return f"getting_information_{domain_name}_into_{extension}_file"
    
    @staticmethod
    def post_osv_report() -> str:
        return f"posting_osv_report"
    
    @staticmethod
    def web_request(method: str, path: str) -> str:
        return f"web_{method.upper()}_{path}"
    
    @staticmethod
    def init_router_path(router_name: str) -> str:
        return f"initing_{router_name}"

    @staticmethod
    def get_extenstions() -> str:
        return "getting_extensions"
    
    @staticmethod
    def init_tech_map()->str:
        return "initing_tech_map"
    
    @staticmethod
    def init_company()->str:
        return "initing_company"
    
    @staticmethod
    def init_groups()->str:
        return "initing_groups"
    
    @staticmethod
    def init_nomenclatures() -> str:
        return "initing_nomenclature"
    
    @staticmethod
    def init_warehouses() -> str:
        return "initing_warehouses"
    
    @staticmethod
    def init_units() -> str:
        return "initing_units"
    
    @staticmethod
    def init_transactions() -> str:
        return "initing_transaction"
    
    @staticmethod
    def add_domain_storage(domain_name: str ) -> str:
        return f"adding_{domain_name}_into_storage"
    
    @staticmethod
    def remove_domain_storage(domain_name: str) -> str:
        return f"removing_{domain_name}_from_storage"
    
    @staticmethod
    def update_groups() -> str:
        return "updating_groups"
    
    @staticmethod
    def update_nomenclature() -> str:
        return "updating_nomenclature"
    
    @staticmethod
    def update_warehouses() -> str:
        return "updating_warehouses"
    
    @staticmethod
    def update_company() -> str:
        return "updating_company"
    
    @staticmethod
    def update_tech_maps() -> str:
        return "updating_tech_maps"

    @staticmethod
    def update_is_first() -> str:
        return "updating_is_first"

    @staticmethod
    def update_units() -> str:
        return "updating_units"
    
    @staticmethod
    def update_transactions() -> str:
        return "updating_transactions"
    