#SEL02_select_all_multiuser.py

import bpy

def select_multiuser_objects():
    user_map = bpy.data.user_map()

    bpy.context.view_layer.objects.active = None
    for obj in bpy.context.selectable_objects:
        obj.select_set(False)
        objects_users = [o for o in user_map.get(obj.data) if isinstance(o, bpy.types.Object)]
        if len(objects_users) > 1:
            obj.select_set(True)
    if bpy.context.selected_objects:
        bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]

# Запуск функции
select_multiuser_objects()
