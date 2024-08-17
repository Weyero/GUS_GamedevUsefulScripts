import bpy

def set_active_uv_channel(uv_channel_name):
    selected_objects = bpy.context.selected_objects

    for obj in selected_objects:
        if obj.type == 'MESH':
            uv_layers = obj.data.uv_layers
            # Find the index of the UV channel by its name
            uv_channel_index = None
            for i, uv_layer in enumerate(uv_layers):
                if uv_layer.name == uv_channel_name:
                    uv_channel_index = i
                    break
            
            if uv_channel_index is not None:
                uv_layers.active_index = uv_channel_index
                print(f"UV channel '{uv_channel_name}' set as active for {obj.name}")
                # Verify the change
                print(f"Current active UV index: {obj.data.uv_layers.active_index}")
                print(f"Current active UV name: {obj.data.uv_layers.active.name}")
            else:
                print(f"UV channel '{uv_channel_name}' does not exist for {obj.name}")
        else:
            print(f"Skipping non-mesh object: {obj.name}")

# Get the UV channel name from the passed arguments
if 'args' in locals():
    uv_channel_name = args[0]  # Extract the name from the passed arguments
    set_active_uv_channel(uv_channel_name)
else:
    print("No arguments provided.")
