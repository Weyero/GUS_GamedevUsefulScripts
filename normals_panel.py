# normals_panel.py

import bpy
import os

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "scripts")

def run_script(script_name):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    with open(script_path, "r") as file:
        script_code = file.read()
    exec(script_code, globals())


class US_PT_NormalPanel(bpy.types.Panel):
    bl_label = "Normals"
    bl_idname = "US_PT_NormalPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Useful Scripts'
    bl_parent_id = "US_PT_MAINPANEL"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.operator("object.run_clear_custom_normals", text="Clear Custom Normals")
        # layout.operator("object.run_add_custom_normals", text="Add Custom Normals")
        # buttons

class US_OT_ClearCustomNormals(bpy.types.Operator):
    bl_idname = "object.run_clear_custom_normals"
    bl_label = "Run Clear Custom Normals"
    bl_description = "Clear custom normals for selected objects"

    def execute(self, context):
        run_script("N01_clear_cust_N.py") # file name
        return {'FINISHED'}

# class US_OT_AddCustomNormals(bpy.types.Operator):
#    bl_idname = "object.run_add_custom_normals"
#    bl_label = "Run Add Custom Normals"
#    bl_description = "Adds custom normals for selected objects"

#    def execute(self, context):
#        run_script("N02_add_custom_normals.py") # file name
#        return {'FINISHED'}


def register():
    bpy.utils.register_class(US_PT_NormalPanel)
    bpy.utils.register_class(US_OT_ClearCustomNormals)
#    bpy.utils.register_class(US_OT_AddCustomNormals)

def unregister():
    bpy.utils.unregister_class(US_PT_NormalPanel)
    bpy.utils.unregister_class(US_OT_ClearCustomNormals)
#    bpy.utils.unregister_class(US_OT_AddCustomNormals)