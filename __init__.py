# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Blender Version Control Util",
    "author" : "Leona DA",
    "description" : "",
    "blender" : (3, 4, 1),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.props import PointerProperty

from . bvc_op import BVC_OT_Create_New
from . bvc_pnl import BVC_PT_Panel
from . bvc_pnl import Properties

classes = (BVC_OT_Create_New, BVC_PT_Panel, Properties)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.my_tool = PointerProperty(type=Properties)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.my_tool
