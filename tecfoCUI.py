#!/usr/bin/env python3
#tecfo
#Copyright (C) 2026 lazypaCCap
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
from textual.app import App
from textual.widgets import Input, Button, RichLog, Header, Footer, Button
from textual.containers import VerticalGroup, HorizontalGroup
import tecfocore
import sys
侧边栏开启 = False
core = tecfocore.core()
if(core.gety() == True):
    引导 = True
else:
    引导=False
class Cbl(VerticalGroup):
    def on_mount(self):
        self.styles.width = 0
        self.cblzt()
        
    def cblzt(self):
        self.mount(Button("历史记录<ctrl+l>", id="history", variant="default"))
        self.mount(Button("设置<ctrl+s>", id="settings", variant="default"))
        self.mount(Button("退出程序<ctrl+e>", id="quit", variant="default"))
        
    def on_button_pressed(self, event):
        bid = event.button.id
        if (bid == "quit"):
            self.app.exit()
        elif (bid == "settings"):
            self.app.action_设置()
        elif (bid == "history"):
            self.app.action_历史()
        else:
            sys.exit(1)
class qd(App):
    BINDINGS = [("ctrl+c", "侧边栏", ""),
    ("ctrl+e", "退出", "退出"),
    ("ctrl+s", "设置", ""),
    ("ctrl+l", "历史",""),
    ("ctrl+q", "nexit","")]
    def __init__(self):
         super().__init__()
         global 引导
         global useing
         useing = False
         if (引导 == True):
             ...
             
         
    def action_侧边栏(self):
        # cbll这个变量在本类的compose()被定义
        global 侧边栏开启
        global cbll
        self.log("cbll:", cbll)
        if(侧边栏开启 == True):
            侧边栏开启 = False
            cbll.styles.width = 0
        else:
            侧边栏开启 = True
            cbll.styles.width = 30
            self.notify(f"如要退出，请使用ctrl+e(If you want to exit,use ctrl+e)")
    def action_退出(self):
        self.exit()
    def action_设置(self):
        ...
    def action_历史(self):
        ...
    def compose(self):
        global cbll
        global main
        global maini
        global maint
        cbll = Cbl()
        self.log("cbll:", cbll)
        with HorizontalGroup():
            yield cbll
            with VerticalGroup():
                maint = RichLog()
                maint.styles.height = "1fr"
                yield maint
                #maini=main+input
                #maint=main+text
                #mainr=main+right
                maini = Input(placeholder="输入消息,Enter发送,此版本暂不支持换行,使用Ctrl+C来开启/关闭侧边栏,Ctrl+E来退出,暂不支持上下文和流式输出")
                maini.styles.height = 5
                yield maini
    def action_nexit(self):
        self.notify(f"如要退出，请使用ctrl+e(If you want to exit,use ctrl+e)")
    def on_input_submitted(self, event: Input.Submitted):
        global useing
        global maini
        global maint
        inp = event.value
        if (useing == True):
            return
        elif (inp == ""):
            self.log("内容不能为空")
            return
        elif(inp == " "):
            self.log("内容不能为空")
            maini.value = ""
            return
        maini.value = ""
        maint.write(f"你：{inp}")
        useing = True
        aiout = core.askn(inp)
        if not (aiout == ""):
            maint.write(f"AI：{aiout}")
        useing = False
qd().run()
