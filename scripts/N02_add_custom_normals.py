import bpy

def add_custom_normals(obj):
    if obj.type == 'MESH':
        try:
            # Ensure we are operating on the active object
            bpy.context.view_layer.objects.active = obj
            
            # Use the new normal attributes system in Blender 4.1+
            if not obj.data.has_custom_normals:
                # Create the split normals layer
                obj.data.calc_normals_split()

                # Enable custom normals
                obj.data.use_customdata_edge_split_normals = True
                print(f"Custom split normals added to: {obj.name}")
            else:
                print(f"{obj.name} already has custom split normals")
        
        except Exception as e:
            print(f"Failed to add custom split normals for: {obj.name}, Error: {e}")
    else:
        print(f"Skipping non-mesh object: {obj.name}")

# Execution part
selection = bpy.context.selected_objects

for obj in selection:
    add_custom_normals(obj)
