from hpyc_core import Core
import os

VERSION = "V1.0.1"
yes = ("y", "Y", "YES", "Yes", "yes", "true", "True", "是", "确认")
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
    [print(id) for id in instance_core.getPluginsOptionToId().keys()]
    while True:
        if (option := input("\n输入你想使用的插件的选项名, 如想退出输入exit\n:")) == "exit":
            input(f"感谢您的使用, hpyc_cli version:{VERSION}\n按下回车键退出程序")
            break

        print(
            f"使用提示：\n{instance_core.getPluginMetadata((plugin_id := instance_core.getPluginIdFromOption(option)))['help']}\n"
        )

        if not (input("如想使用此插件请输入 y 否则输入 n\n:") in yes):
            continue

        instance_core.eventStartCalculate(
            plugin_id=plugin_id,
            input_data=input("请输入待处理数据(如需换行请输入 \\n )\n:"),
            mode=("Save" if input("如想将结果保存至文件请输入 y 否则输入 n\n:") in yes else "Return"),
        )

        while True:  # 消息处理
            rev = message_queue.get()
            match rev[0]:
                case "OUTPUT":
                    print(rev[1])
                case "ERROR":
                    print(f"发生了{rev[1]}\n详细错误:{rev[2]}")
                    break
                case "MESSAGE":
                    if rev[1] == "CalculationProgramIsRunning":
                        print("正在计算, 请耐心等待")
                    elif rev[1] == "CalculationProgramIsFinished":
                        print(f"计算完毕, 花费了{rev[2]}ns")
                        break
