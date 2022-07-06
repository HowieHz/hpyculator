from hpyc_core import Core
from pprint import pprint
import os

VERSION = "V1.0.0"
yes = ("y", "Y", "YES", "Yes", "yes")
instance_core = Core()
message_queue = instance_core.getMessageQueue()

if __name__ == "__main__":
    os.system("chcp 65001")
    print(
        f"""\
插件存放目录: {instance_core.getPluginsDirPath()}
设置文件存放目录: {instance_core.getSettingsDirPath()}
输出目录: {instance_core.getOutputDirPath()}
获取到的插件选项名: """
    )
    pprint(tuple(instance_core.getPluginsOptionToId().keys()))
    while True:
        option = input("输入你想使用的插件的选项名, 如想退出输入exit\n:")
        if option == "exit":
            print(f"感谢您的使用, hpyc_cli version:{VERSION}")
            break

        plugin_id = instance_core.getPluginIdFromOption(option)

        print(f"使用提示：\n{instance_core.getPluginMetadata(plugin_id)['help']}")

        if not input("如想使用此插件请输入 y 否则输入 n\n:") in yes:
            continue
        rev_input = input(r"请输入待处理数据(如需换行请输入 \n ):")

        if input("如想将结果保存至文件请输入 y 否则输入 n\n:") in yes:
            instance_core.eventStartCalculate(
                plugin_id=plugin_id, input_data=rev_input, mode="Save"
            )
        else:
            instance_core.eventStartCalculate(
                plugin_id=plugin_id, input_data=rev_input, mode="Return"
            )
        while True:  # 消息处理
            rev = message_queue.get()
            if rev[0] == "OUTPUT":
                print(rev[1])
            elif rev[0] == "ERROR":
                print(f"发生了{rev[1]}\n详细错误:{rev[2]}")
                break
            elif rev[0] == "MESSAGE":
                if rev[1] == "CalculationProgramIsRunning":
                    print("正在计算, 请耐心等待")
                elif rev[1] == "CalculationProgramIsFinished":
                    print(f"计算完毕, 花费了{rev[2]}ns")
                    break
