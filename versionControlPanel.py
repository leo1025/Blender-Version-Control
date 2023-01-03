import bpy
from bpy.types import Panel

class BVC_PT_MainPanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Version Control"
    bl_category = "BVC"

    def draw(self, context):

        layout = self.layout

        row = layout.row()
        col = row.column()
        col.operator("bvc.new_project", text="New Project")
# https://b3d.interplanety.org/en/creating-pop-up-panels-with-user-ui-in-blender-add-on/
class BVC_PT_newPanel(Panel):