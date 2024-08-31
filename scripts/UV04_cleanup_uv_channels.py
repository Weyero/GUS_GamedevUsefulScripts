import bpy

def cleanup_uv_maps(obj, new_uv_map_name="UVMap"):
    if obj.type == 'MESH':
        uv_layers = obj.data.uv_layers
        
        if uv_layers:  # Check if the object has any UV Maps
            # Remove all UV Maps except the first one, starting from the end
            for i in reversed(range(1, len(uv_layers))):
                uv_layers.remove(uv_layers[i])
            
            # Rename the remaining UV Map to "UVMap"
            uv_layers[0].name = new_uv_map_name
            print(f"UV channels cleaned up for {obj.name}. Only '{new_uv_map_name}' remains.")
        else:
            print(f"No UV channels found for {obj.name}.")
    else:
        print(f"Skipping non-mesh object: {obj.name}")

# Apply to all selected objects
selection = bpy.context.selected_objects

for obj in selection:
    cleanup_uv_maps(obj)
