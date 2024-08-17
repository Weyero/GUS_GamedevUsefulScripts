bl_info = {
    "name": "GUS - Gamedev Useful Scripts",
    "blender": (3, 5, 0),
    "category": "Object",
    "description": "A collection of useful scripts for various tasks, mostly for gamedev",
    "author": "ladno",
    "version": (1, 0, 0),
}

import bpy
from . import normals_panel  # Normals panel and operators
from . import uv_panel  # UV panel and operators
from . import materials_panel  # Materials panel and operators
from . import modifiers_panel  # Modifiers panel and operators
from . import cleanup_panel  # Cleanup panel and operators


class US_PT_MainPanel(bpy.types.Panel):
    bl_label = "GUS"
    bl_idname = "US_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'GUS'
    
    def draw(self, context):
        layout = self.layout


# register
def register():
    bpy.utils.register_class(US_PT_MainPanel)
    normals_panel.register()  # Регистрация панелей и операторов из normals_panel
    uv_panel.register()  # Регистрация панелей и операторов из uv_panel
    materials_panel.register()  # Регистрация панелей и операторов из materials_panel
    modifiers_panel.register()  # Регистрация панелей и операторов из modifiers_panel
    cleanup_panel.register()  # Регистрация панелей и операторов из cleanup_panel

def unregister():
    bpy.utils.unregister_class(US_PT_MainPanel)
    normals_panel.unregister()  # Отмена регистрации панелей и операторов из normals_panel
    uv_panel.unregister()  # Отмена регистрации панелей и операторов из uv_panel
    materials_panel.unregister()  # Отмена регистрации панелей и операторов из materials_panel
    modifiers_panel.unregister()  # Отмена регистрации панелей и операторов из modifiers_panel
    cleanup_panel.unregister()  # Отмена регистрации панелей и операторов из cleanup_panel

if __name__ == "__main__":
    register()
