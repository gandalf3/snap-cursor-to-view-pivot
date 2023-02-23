bl_info = {
    "name": "Snap 3D Cursor to View Pivot",
    "author": "gandalf3",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Object > Snap > Cursor to View Pivot",
    "description": "Snap 3D Cursor to the 3D view pivot",
    "doc_url": "",
    "category": "3D View",
}

import bpy

class SnapCursorToViewPivot(bpy.types.Operator):
    """Snap 3D Cursor to the 3D view pivot"""
    bl_idname = "view3d.snap_cursor_to_view_pivot"
    bl_label = "Cursor to View Pivot"

    @classmethod
    def poll(cls, context):
        return context.area is not None and\
               context.area.type == 'VIEW_3D' and\
               context.scene is not None

    def execute(self, context):
        context.scene.cursor.location = context.space_data.region_3d.view_location
        context.scene.cursor.rotation_quaternion = context.space_data.region_3d.view_rotation
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(SnapCursorToViewPivot.bl_idname, text=SnapCursorToViewPivot.bl_label)

def register():
    bpy.utils.register_class(SnapCursorToViewPivot)
    bpy.types.VIEW3D_MT_snap.append(menu_func)
    # uncomment the line below to add an entry to the snap pie menu as well;
    # this menu is already crowded though..
    #bpy.types.VIEW3D_MT_snap_pie.append(menu_func)

def unregister():
    bpy.utils.unregister_class(SnapCursorToViewPivot)
    bpy.types.VIEW3D_MT_snap.remove(menu_func)
    # if you uncomment the line above, don't forget to uncomment this line too!
    #bpy.types.VIEW3D_MT_snap_pie.remove(menu_func)


if __name__ == '__main__':
    register()
