# -*- coding: UTF-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import fs_uae_launcher.fsui as fsui
from ..I18N import _, ngettext

class AboutDialog(fsui.Dialog):

    def __init__(self, parent):
        fsui.Dialog.__init__(self, parent, _("About {name}").format(
                name="FS-UAE Launcher"))
        self.layout = fsui.VerticalLayout()
        self.layout.padding_top = 10
        self.layout.padding_bottom = 10
        self.layout.padding_left = 10
        self.layout.padding_right = 10

        self.text_area = fsui.TextArea(self, about_message,
                read_only=True, font_family="monospace")
        self.text_area.set_min_width(700)
        self.text_area.set_min_height(400)
        self.layout.add(self.text_area, fill=True, margin=10)

        self.layout.add_spacer(10)
        hori_layout = fsui.HorizontalLayout()
        hori_layout.add_spacer(10, expand=True)
        self.layout.add(hori_layout, fill=True)

        self.close_button = fsui.Button(self, _("Close"))
        self.close_button.on_activate = self.on_close_button
        hori_layout.add(self.close_button, margin_left=10)
        hori_layout.add_spacer(10)
        self.layout.add_spacer(10)

        self.set_size(self.layout.get_min_size())
        self.center_on_parent()

    def on_close_button(self):
        self.end_modal(False)


about_message = u"""FS-UAE Launcher is Copyright (C) 2012-2013 Frode Solheim.

This package is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This package is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this package; if not, write to the Free Software Foundation, Inc.,
51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA

The following people have translated FS-UAE Launcher into several languages: 
Cédric "Foul" Monféfoul (French), nexusle (German), Speedvicio (Italian),
grimi (Polish), Milanchez (Serbian), albconde (Spanish), Treco (Portuguese),
GoingDown (Finish), spajdr (Czech).

A big thanks to everyone who have tested the software and provided valuable
feedback! Especially the encouraging members of the English Amiga Board, and
all you who have commented on the official FS-UAE web site.

FS-UAE Launcher includes icons from GNOME icon theme from the GNOME Project
(http://www.gnome.org). The GNOME icon theme is distributed under the terms
of either GNU LGPL v.3 or Creative Commons BY-SA 3.0 license.

FS-UAE Launcher includes icons from humanity-icon-theme, licensed under the
terms of the GNU General Public license.

FS-UAE includes icons from oxygen-icon-theme, licensed under the terms of the
GNU Lesser General Public License as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.

The Amiga Forever icon is (probably) copyright Cloanto Italia srl.

FS-UAE Launcher includes the oyoyo library, Copyright (c) 2008 Duncan Fordyce,
The license for this library is contained in the following paragraph:
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED
"AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

FS-UAE Launcher depends on several open source third party software packages,
including but not limited to, Python and wxPython.
"""
