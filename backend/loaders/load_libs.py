#!/usr/bin/python3

import os

from markupsafe import Markup

from backend.utils.files import FilesUtils

from backend.classes.settings import Settings

class LoadLibs:
    
    @classmethod
    def css_internal(cls) -> str:
        styles = []
        
        path = Settings.get('paths.static.css', 'string')
        libs = FilesUtils.scan_path(path)
        
        for lib in libs:
            file = lib.replace('./static/', '')
            styles.append(f'{file}')
            
        return set(styles)
    
    @classmethod
    def js_internal(cls, plugins:bool=False) -> str:
        scripts = []
        js_files_path = 'paths.static.js'
        
        if plugins:
            js_files_path = 'paths.static.js_plugins'
        
        path = Settings.get(js_files_path, 'string')
        libs = FilesUtils.scan_path(path)
        
        for lib in libs:
            file = lib.replace('./static/', '')
            scripts.append(f'{file}')
            
        return set(scripts)
    
    @classmethod
    def js_external(cls, page:str) -> str:
        scripts = []
        libs = Settings.get(f'external_libs.{page}', 'list')

        for lib in libs:
            scripts.append(f"<script src='{lib}'></script>")
        
        scripts = set(scripts)
        return Markup(''.join(scripts))
