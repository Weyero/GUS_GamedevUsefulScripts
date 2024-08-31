import bpy

def rename_active_uv_channel(new_uv_name):
    # Iterate over all selected objects
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':  # Ensure the object is a mesh
            uv_layers = obj.data.uv_layers
            if uv_layers:  # Check if the object has any UV Maps
                active_uv = uv_layers.active  # Get the active UV map
                active_uv.name = new_uv_name  # Rename the active UV map
                print(f"Renamed active UV channel to '{new_uv_name}' for object {obj.name}")
            else:
                print(f"No UV maps found for object {obj.name}")
        else:
            print(f"Skipping non-mesh object: {obj.name}")

# Get the UV channel name from the passed arguments
if 'args' in locals():
    new_uv_name = args[0]  # Extract the name from the passed arguments
    rename_active_uv_channel(new_uv_name)
else:
    print("No arguments provided.")
