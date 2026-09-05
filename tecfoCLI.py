#!/usr/bin/env python3
#Lzici
#Copyright (C) 2026 lazypaCCap
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
#You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
import sys
import urllib.request
import json
def 输入():
    if len(sys.argv) > 1:
        p = [None]*30
        p[13] = ' '.join(sys.argv[1:2])
        q = 3
        for _ in range(11):
            p[q-1] = ' '.join(sys.argv[q-1:q])
            q = q + 1
        默认值 = {
        10: 0.7,
        11: 1.0,
        12: None,
        13: None,
        14: 2048,
        15: 40,
        16: 0.9,
        17: None,
        18: None
        }
        i = 10
        r = [None]*30
        for _ in range(9):
            r[i] = p[i - 8]
            if r[i] == None or r[i] == '':
                r[i] = 默认值[i]
            i = i + 1
        r[21] = p [13]
        r[20] = p [12]
        r[19] = p [11]
        qr = 19
        for _ in range(3):
            if r[qr] == '':
                print("非法的值")
                sys.exit(1)
            else:
                qr=qr+1
    else:
        print("请附带参数.")
        sys.exit(1)
    ollama(r[21],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19],r[20])
def ollama(提示词, 温度, 重复惩罚, 种子, 最大生成长度, 上下文长度, top_k, top_p, 停止词, 存货时间,模型名,流式):
    调用链接 = "http://127.0.0.1:11434/api/generate"
    options = {}
    流式布尔 = (流式 == 'True')
    payload = {
        "model": 模型名,
        "prompt": 提示词,
        "stream": 流式布尔,
        "options": {}
    }
    if 停止词 not in (None, ''):
        payload["options"]["stop"] = [停止词]
    else:
        停止词 = None
    payload["options"]["temperature"] = float(温度)
    payload["options"]["repeat_penalty"] = float(重复惩罚)
    payload["options"]["seed"] = int(种子)
    payload["options"]["num_predict"] = int(最大生成长度)
    payload["options"]["num_ctx"] = int(上下文长度)
    payload["options"]["top_k"] = int(top_k)
    payload["options"]["top_p"] = float(top_p)
    payload["options"]["keep_alive"] = 存货时间
    if 流式 == 'True':
        流式解析 = 1
    else:
        if 流式 == 'False':
            流式解析 = 0
        else:
            print ("流式的值不合法,使用True/False,首字母大写")
            sys.exit(1)
        流式布尔 = (流式解析 == 1)
    if 流式解析 == 0:
        req = urllib.request.Request(调用链接, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as resp:
#             print(json.loads(resp.read().decode()))
            print(json.loads(resp.read().decode())["response"])
    else:
        req = urllib.request.Request(调用链接,data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req) as resp:
            for line in resp:
                if line:
                    chunk = json.loads(line.decode())
                    print(chunk["response"], end="", flush=True)
        print()
        sys.exit(0)
if __name__ == "__main__":
    输入()

