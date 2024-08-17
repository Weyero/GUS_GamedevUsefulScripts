import bpy

def delete_uv_channel(uv_channel_name):
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        if obj.type == 'MESH':
            uv_layers = obj.data.uv_layers
            # check if there's such uv channel name
            if uv_channel_name in uv_layers:
                uv_layer = uv_layers.get(uv_channel_name)
                if uv_layer:
                    uv_layers.remove(uv_layer)
                    print(f"UV channel '{uv_channel_name}' removed from {obj.name}")
                else:
                    print(f"UV channel '{uv_channel_name}' not found for {obj.name}")
            else:
                print(f"UV channel '{uv_channel_name}' does not exist for {obj.name}")
        else:
            print(f"Skipping non-mesh object: {obj.name}")

    # update mesh and interface
    bpy.context.view_layer.update()
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()

if 'args' in locals():
    uv_channel_name = args[0]  # extract uv channel name from args
    delete_uv_channel(uv_channel_name)
else:
    print("No arguments provided.")
