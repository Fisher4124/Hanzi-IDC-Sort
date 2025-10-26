import os
import datetime
from collections import defaultdict

while True:
    ids_path = input("请输入IDS.txt文件路径：").strip('"').strip("'")
    Hanzi_path = input("请输入Hanzi.txt文件路径：").strip('"').strip("'")

    # === IDC到结构描述的映射 ===
    IDC_MAP = {
        "⿰": "左右结构",
        "⿱": "上下结构",
        "⿲": "左中右结构",
        "⿳": "上中下结构",
        "⿴": "全包围结构",
        "⿵": "上包围结构",
        "⿶": "下包围结构",
        "⿷": "左包围结构",
        "⿸": "左上包围结构",
        "⿹": "右上包围结构",
        "⿺": "左下包围结构",
        "⿻": "嵌套结构",
        "⿼": "右包围结构",
        "⿽": "右下包围结构",
        "⿾": "水平翻转",
        "⿿": "颠倒旋转",
        "〾": "形似字符",
        "㇯": "减去笔画",
    }

    IDC_SET = set(IDC_MAP.keys())

    import unicodedata

    # === 读取IDS.txt === 
    char_to_idc = {}

    with open(ids_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # 检测对应汉字
            parts = line.split()
            if len(parts) < 2:
                continue
            char = parts[1]

            # 找到第一个IDC
            for ch in line:
                if ch in IDC_SET:
                    char_to_idc[char] = ch
                    break

    # === 读取Hanzi.txt ===
    structure_dict = defaultdict(list)

    with open(Hanzi_path, "r", encoding="utf-8") as f:
        text = f.read().strip().replace("\u3000", "")
        for char in text:
            idc = char_to_idc.get(char)
            if idc:
                structure = IDC_MAP.get(idc, "未知结构")
                structure_dict[structure].append(char)
            else:
                structure_dict["未识别结构"].append(char)

    # === 输出结果 ===
    output_lines = []
    for structure, chars in structure_dict.items():
        output_lines.append(f"{structure}：")
        output_lines.append("".join(chars))
        output_lines.append("")

    result_text = "\n".join(output_lines)

    # === 输出到桌面 ===
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    date_tag = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    output_filename = f"汉字结构分拣_{date_tag}.txt"
    output_path = os.path.join(desktop, output_filename)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write(result_text)

    print(f"完毕！结果已保存至：{output_path}")
    
    choice = input("\n按回车键重新运行／[ENTER]=ReRun")
    if choice.strip() == "":
        print("\n=== 重新运行 ===\n")
        continue
    else:
        break