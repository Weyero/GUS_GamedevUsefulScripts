# uv_panel.py

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



class US_PT_UVPanel(bpy.types.Panel):
    bl_label = "UV"
    bl_idname = "US_PT_UVPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Useful Scripts'
    bl_parent_id = "US_PT_MAINPANEL"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        
        # Add a text field for UV channel name input
        layout.prop(context.scene, "uv_channel_name", text="UV Channel Name")
        
        # Add space between buttons
        layout.separator()
        
        # Button to add UV channel
        layout.operator("object.add_uv_channel", text="Add UV Channel")
        
        # Button to delete UV channel
        layout.operator("object.del_uv_channel", text="Delete UV Channel")
        
        # Button to set UV channel as active
        layout.operator("object.set_active_uv_channel", text="Set Active UV Channel")

        layout.operator("object.rename_active_to", text="Rename Active Layer to")

        layout.separator()

        layout.operator("object.clean_uv_channels", text="Clean UV Channels")

# this OPERATOR adds uv channel with certain name
class US_OT_AddUVChannel(bpy.types.Operator):
    bl_idname = "object.add_uv_channel"
    bl_label = "Add UV Channel"
    bl_description = "Adds UV channel to selected objects with the name specified in the panel."

    def execute(self, context):
        uv_channel_name = context.scene.uv_channel_name
        run_script("UV01_2uv_nameit.py", uv_channel_name)
        self.report({'INFO'}, f"UV channel '{uv_channel_name}' added.")
        return {'FINISHED'}

# this OPERATOR removes uv channel with certain name
class US_OT_DelUVChannel(bpy.types.Operator):
    bl_idname = "object.del_uv_channel"
    bl_label = "Delete UV Channel"
    bl_description = "Removes UV channel from selected objects with the name specified in the panel."

    def execute(self, context):
        uv_channel_name = context.scene.uv_channel_name
        run_script("UV02_del_uv_ch_named.py", uv_channel_name)
        self.report({'INFO'}, f"UV channel '{uv_channel_name}' deleted.")
        return {'FINISHED'}

# Operator to set UV channel as active
class US_OT_SetActiveUVChannel(bpy.types.Operator):
    bl_idname = "object.set_active_uv_channel"
    bl_label = "Set Active UV Channel"
    bl_description = "Sets the UV channel as active for selected objects with the name specified in the panel."

    def execute(self, context):
        uv_channel_name = context.scene.uv_channel_name
        run_script("UV03_channel_make_active.py", uv_channel_name)
        self.report({'INFO'}, f"UV channel '{uv_channel_name}' set as active.")
        return {'FINISHED'}

class US_OT_RenameActiveUV(bpy.types.Operator):
    bl_idname = "object.rename_active_to"
    bl_label = "Rename active channel"
    bl_description = "Renames the active UV channel on all selected objects to the specified name."

    def execute(self, context):
        uv_channel_name = context.scene.uv_channel_name
        run_script("UV05_rename_active_channel_to.py", uv_channel_name)
        self.report({'INFO'}, f"UV Channels renamed to '{uv_channel_name}'.")
        return {'FINISHED'}


class US_OT_CleanupUVChannels(bpy.types.Operator):
    bl_idname = "object.clean_uv_channels"
    bl_label = "Clean UV Channels"
    bl_description = "Removes all UV channels except the first and renames it to default name"

    def execute(self, context):
        run_script("UV04_cleanup_uv_channels.py")
        self.report({'INFO'}, "UV Channels Cleaned up.")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(US_PT_UVPanel)
    bpy.utils.register_class(US_OT_AddUVChannel)
    bpy.utils.register_class(US_OT_DelUVChannel)
    bpy.utils.register_class(US_OT_SetActiveUVChannel)
    bpy.utils.register_class(US_OT_CleanupUVChannels)
    bpy.utils.register_class(US_OT_RenameActiveUV)
    bpy.types.Scene.uv_channel_name = bpy.props.StringProperty(
        name="UV Channel Name",
        default="UVMap02",
        description="Name of the UV channel to create, delete, or activate"
    )

def unregister():
    bpy.utils.unregister_class(US_PT_UVPanel)
    bpy.utils.unregister_class(US_OT_AddUVChannel)
    bpy.utils.unregister_class(US_OT_DelUVChannel)
    bpy.utils.unregister_class(US_OT_SetActiveUVChannel)
    bpy.utils.unregister_class(US_OT_CleanupUVChannels)
    bpy.utils.unregister_class(US_OT_RenameActiveUV)
    del bpy.types.Scene.uv_channel_name