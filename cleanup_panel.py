# cleanup_panel.py

import bpy
import os

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "scripts")

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    with open(script_path, "r") as file:
        script_code = file.read()
    exec(script_code, globals())


class US_PT_CleanupPanel(bpy.types.Panel):
    bl_label = "Cleanup"
    bl_idname = "US_PT_CleanupPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Useful Scripts'
    bl_parent_id = "US_PT_MAINPANEL"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.operator("object.clear_ue_lods", text="Clear UE LODs")


class US_OT_ClearUELods(bpy.types.Operator):
    bl_idname = "object.clear_ue_lods"
    bl_label = "Clear UE LODs"
    bl_description = "Removes LODS and keeps only LOD0 after you import mesh from UE export"

    def execute(self, context):
        run_script("CU01_clear_lods.py") # file name
        return {'FINISHED'}
    

def register():
    bpy.utils.register_class(US_PT_CleanupPanel)
    bpy.utils.register_class(US_OT_ClearUELods)

def unregister():
    bpy.utils.unregister_class(US_PT_CleanupPanel)
    bpy.utils.unregister_class(US_OT_ClearUELods)