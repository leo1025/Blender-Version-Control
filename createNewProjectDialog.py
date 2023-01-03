import bpy
from bpy.types import Operator

class BVC_OT_NewProject(Operator):
    """Open Create New Version Controlled Project Dialog"""
    bl_label = "Create New Project"
    bl_idname = "bvc.new_project"

    text = bpy.props.StringProperty(name= "Enter Project Name", default= "")

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=400)