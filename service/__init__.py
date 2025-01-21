# service/__init__.py
import os
import importlib

routers = []

current_dir = os.path.dirname(__file__)

for folder_name in os.listdir(current_dir):
    sub_path = os.path.join(current_dir, folder_name)
    # 하위 디렉터리인지 확인
    if os.path.isdir(sub_path):
        route_file = os.path.join(sub_path, 'route.py')
        # route.py 파일이 존재하는지 확인
        if os.path.isfile(route_file):
            # 예: service.cluster.route 로 모듈 import
            module_name = f"service.{folder_name}.route"
            module = importlib.import_module(module_name)
            routers.append(module.router)

__all__ = ["routers"]