import bpy

selection = bpy.context.selected_objects

for obj in selection:
    if obj.type == 'MESH':
        try:
            # set active element
            bpy.context.view_layer.objects.active = obj
            
            # to edit mode
            bpy.ops.object.mode_set(mode='EDIT')
            
            # clear custom normals
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
            
            # back to obj mode
            bpy.ops.object.mode_set(mode='OBJECT')
            print(f"Custom split normals cleared for: {obj.name}")
        
        except Exception as e:
            print(f"Failed to clear custom split normals for: {obj.name}, Error: {e}")
    
    else:
        print(f"Skipping non-mesh object: {obj.name}")
