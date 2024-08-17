import bpy
import re

def clear_parent_keep_transform(obj):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

def apply_scale(obj):
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

def delete_lod_objects():
    pattern = re.compile(r"LOD[1-9]\d*(\.\d+)?")
    all_objects = bpy.data.objects
    objects_to_delete = [obj for obj in all_objects if pattern.search(obj.name)]
    
    for obj in objects_to_delete:
        bpy.data.objects.remove(obj, do_unlink=True)

def delete_empty_objects():
    all_objects = bpy.data.objects
    empties_to_delete = [obj for obj in all_objects if obj.type == 'EMPTY']
    
    for obj in empties_to_delete:
        bpy.data.objects.remove(obj, do_unlink=True)


# clear parent and keep transform
for obj in bpy.context.selected_objects:
    clear_parent_keep_transform(obj)

# apply scale
for obj in bpy.context.selected_objects:
    apply_scale(obj)

# remove object by pattern
delete_lod_objects()

# remove empty
delete_empty_objects()
