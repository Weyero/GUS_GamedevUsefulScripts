# materials_panel.py

import bpy
import os

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "scripts")

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    with open(script_path, "r") as file:
        script_code = file.read()
    exec(script_code, globals())


class US_PT_MaterialPanel(bpy.types.Panel):
    bl_label = "Materials"
    bl_idname = "US_PT_MaterialPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Useful Scripts'
    bl_parent_id = "US_PT_MAINPANEL"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.operator("object.delete_mat_duplicates", text="Clear Mat Duplicates")
        # buttons


class US_OT_ClearMaterialDuplicates(bpy.types.Operator):
    bl_idname = "object.delete_mat_duplicates"
    bl_label = "Clear Mat Duplicates"
    bl_description = "After you import several meshes with the same material, it becomes duplicated with suffix .001, .002 etc. This script replaces those duplicates with original material and removes them from .blend file"

    
    def execute(self, context):
        run_script("M01_del_mat_dupli.py") # file name
        return {'FINISHED'}


def register():
    bpy.utils.register_class(US_PT_MaterialPanel)
    bpy.utils.register_class(US_OT_ClearMaterialDuplicates)

def unregister():
    bpy.utils.unregister_class(US_PT_MaterialPanel)
    bpy.utils.unregister_class(US_OT_ClearMaterialDuplicates)