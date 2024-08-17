# modifiers_panel.py

import bpy
import os

SCRIPT_DIR = os.path.join(os.path.dirname(__file__), "scripts")

def run_script(script_name, *args):
    script_path = os.path.join(SCRIPT_DIR, script_name)
    try:
        with open(script_path, "r") as file:
            script_code = file.read()
        print(f"Running script: {script_name} with args: {args}")
        # Execute the script in a new namespace with access to arguments
        exec(script_code, globals(), {'args': args})
    except Exception as e:
        print(f"Failed to run script {script_name}: {e}")

def get_modifiers_in_use():
    modifiers_set = set()
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            for modifier in obj.modifiers:
                modifiers_set.add(modifier.name)
    return list(modifiers_set)

def update_modifier_list(scene):
    # Update the modifier options whenever requested
    modifier_types = get_modifiers_in_use()
    bpy.types.Scene.modifier_options = bpy.props.EnumProperty(
        name="Modifier Options",
        items=[(mod_type, mod_type, "") for mod_type in modifier_types]
    )


class US_PT_ModifierPanel(bpy.types.Panel):
    bl_label = "Modifiers"
    bl_idname = "US_PT_ModifierPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Useful Scripts'
    bl_parent_id = "US_PT_MAINPANEL"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        ## Button to refresh the modifier list
        layout.operator("object.update_modifiers_list", text="Refresh Modifiers List")
        
        # Dropdown for selecting a modifier
        layout.prop(scene, "modifier_options", text="Select Modifier")

        # Button for deleting the selected modifier
        layout.operator("object.delete_certain_modif", text="Delete Only This")

class US_OT_UpdateModifiersList(bpy.types.Operator):
    bl_idname = "object.update_modifiers_list"
    bl_label = "Update Modifiers List"
    bl_description = "Update the list of modifiers available in the scene."

    def execute(self, context):
        update_modifier_list(context.scene)
        self.report({'INFO'}, "Modifiers list updated.")
        return {'FINISHED'}

class US_OT_DeleteCertainModifier(bpy.types.Operator):
    bl_idname = "object.delete_certain_modif"
    bl_label = "Delete Certain Modifier"
    bl_description = "Deletes the selected modifier from selected objects."

    def execute(self, context):
        modifier_name = context.scene.modifier_options
        # Run the external script with the selected modifier as an argument
        run_script("MF01_del_modifier_named.py", modifier_name)
        self.report({'INFO'}, f"Modifier '{modifier_name}' processed.")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(US_PT_ModifierPanel)
    bpy.utils.register_class(US_OT_UpdateModifiersList)
    bpy.utils.register_class(US_OT_DeleteCertainModifier)
    bpy.types.Scene.modifier_options = bpy.props.EnumProperty(
        name="Modifier Options",
        items=[]
    )

def unregister():
    bpy.utils.unregister_class(US_PT_ModifierPanel)
    bpy.utils.unregister_class(US_OT_UpdateModifiersList)
    bpy.utils.unregister_class(US_OT_DeleteCertainModifier)
    del bpy.types.Scene.modifier_options