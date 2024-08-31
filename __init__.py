bl_info = {
    "name": "GUS - Gamedev Useful Scripts",
    "blender": (4, 2, 0),
    "category": "Object",
    "description": "A collection of useful scripts for various tasks, mostly for gamedev",
    "author": "ladno",
    "version": (1, 0, 1),
}

import bpy
from . import normals_panel  # Normals panel and operators
from . import uv_panel  # UV panel and operators
from . import materials_panel  # Materials panel and operators
from . import modifiers_panel  # Modifiers panel and operators
from . import cleanup_panel  # Cleanup panel and operators
from . import selection_panel  # Selection panel and operators


class US_PT_MainPanel(bpy.types.Panel):
    bl_label = "GUS"
    bl_idname = "US_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout


# register
def register():
    bpy.utils.register_class(US_PT_MainPanel)
    normals_panel.register()
    uv_panel.register()
    materials_panel.register()
    modifiers_panel.register()
    cleanup_panel.register()
    selection_panel.register()

def unregister():
    bpy.utils.unregister_class(US_PT_MainPanel)
    normals_panel.unregister()
    uv_panel.unregister()
    materials_panel.unregister()
    modifiers_panel.unregister()
    cleanup_panel.unregister()
    selection_panel.unregister()

if __name__ == "__main__":
    register()
