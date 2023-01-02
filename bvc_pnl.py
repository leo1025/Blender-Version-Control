import bpy
from bpy.props import StringProperty
from bpy.types import (Panel, PropertyGroup)

class Properties(PropertyGroup):
    path : StringProperty(
        name="",
        description="Path to Directory",
        default="",
        maxlen=1024,
        subtype='DIR_PATH')

class BVC_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Version Control"
    bl_category = "BVC"

    def draw(self, context):

        layout = self.layout
        scn = context.scene

        row = layout.row()
        col = row.column()
        col.prop(scn.my_tool, "path", text="")

        row = layout.row()
        col = row.column()
        col.operator("object.create_new_project", text="New")

        # print the path to the console
        print (scn.my_tool.path)

