message_queue = Queue()  # 输出消息 保证里面取出来的数据类型一定是str
OutputReachedLimit
CalculationProgramIsRunning
CalculationProgramIsFinished（下一条消息是所用时间，类型int，单位ns）
output_queue = Queue()  # 输出结果 生产者-消费者模型 保证里面取出来的数据类型一定是str
error_queue = Queue()  # 输出错误 保证里面取出来的数据类型一定是str
TypeConversionError
CalculationError

getOutputQueue
getErroeQueue
getMessageQueue
getPluginsDirPath
getOutputDirPath
getSettingsDirPath

getPluginsTagOption
getPluginsOptionToId

getPluginInstance
getPluginMetadata

setPluginsDirPath

eventReloadPlugins
eventStartCalculate
eventExit

设置文件会设置
plugins_dir_path
output_dir_path

要用对应方法获取，不推荐直接from import
message_queue
output_queue
error_queue
instance_settings_file