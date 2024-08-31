# selection_panel.py

import bpy
import os

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "scripts")

def run_script(script_name, *args):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    with open(script_path, "r") as file:
        script_code = file.read()
    exec(script_code, globals(), {'args': args})

# Define an integer property
bpy.types.Scene.my_int = bpy.props.IntProperty(
    name="Integer Input",
    description="Enter an integer value",
    default=5000,  # Default value
    min=0,       # Minimum value
    max=50000      # Maximum value
)

class US_PT_SelectionPanel(bpy.types.Panel):
    bl_label = "Selection"
    bl_idname = "US_PT_SelectionPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Useful Scripts'
    bl_parent_id = "US_PT_MAINPANEL"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.label(text="Number of polygons")
        layout.prop(context.scene, "my_int")
        layout.operator("object.select_by_polycount", text="Select object more than")
        
        layout.separator()

        layout.operator("object.select_multiuser", text="Select all multi-user")


class US_OT_Select_by_polycount(bpy.types.Operator):
    bl_idname = "object.select_by_polycount"
    bl_label = "SelectByPolycount"
    bl_description = "Selects objects with more than entered value."

    def execute(self, context):
        threshold = context.scene.my_int
        run_script("SEL01_select_by_polycount.py", threshold)
        self.report({'INFO'}, f"Objects selected")
        return {'FINISHED'}


class US_OT_Select_All_MultiUser(bpy.types.Operator):
    bl_idname = "object.select_multiuser"
    bl_label = "SelectAllMultiUser"
    bl_description = "Selects all multi-user objects"

    def execute(self, context):
        run_script("SEL02_select_all_multiuser.py")
        self.report({'INFO'}, f"Objects selected")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(US_PT_SelectionPanel)
    bpy.utils.register_class(US_OT_Select_by_polycount)
    bpy.utils.register_class(US_OT_Select_All_MultiUser)

def unregister():
    bpy.utils.unregister_class(US_PT_SelectionPanel)
    bpy.utils.unregister_class(US_OT_Select_by_polycount)
    bpy.utils.unregister_class(US_OT_Select_All_MultiUser)