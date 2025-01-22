# service/__init__.py

import os
import importlib

routers = []

current_dir = os.path.dirname(__file__)

for folder_name in os.listdir(current_dir):
    sub_path = os.path.join(current_dir, folder_name)
    # 하위 디렉터리인지 확인
    if os.path.isdir(sub_path):
        # 폴더이름과 동일한 형태로 라우트 파일이 존재하는지 확인: [folder_name]_route.py
        route_file_name = f"{folder_name}_route.py"
        route_file = os.path.join(sub_path, route_file_name)
        
        if os.path.isfile(route_file):
            # 예: service.auth.auth_route 형태로 모듈 import
            module_name = f"service.{folder_name}.{folder_name}_route"
            module = importlib.import_module(module_name)
            routers.append(module.router)

__all__ = ["routers"]
