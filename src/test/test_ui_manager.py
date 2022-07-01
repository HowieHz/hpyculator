# @pytest.mark.run(order=1)
# def test_hpysignal():
#     """
#     测试hpysignal子模块
#
#     :return:
#     """
#     global test_reflect
#
#     def _slot_fun(text: str):  # 模拟str型形参槽
#         global test_reflect
#         test_reflect = text
#
#     def _slot_fun_none():  # 模拟无参数槽
#         global test_reflect
#         test_reflect = None
#
#     def _slot_fun_bool(b: bool):  # 模拟bool型形参槽
#         global test_reflect
#         test_reflect = b
#
#     # 绑定对应槽函数
#     main_signal.set_output_box.connect(_slot_fun)
#     main_signal.clear_output_box.connect(_slot_fun_none)
#     main_signal.append_output_box.connect(_slot_fun)
#     main_signal.insert_output_box.connect(_slot_fun)
#     main_signal.append_output_box_.connect(_slot_fun)
#     main_signal.insert_output_box_.connect(_slot_fun)
#     main_signal.get_output_box.connect(_slot_fun_none)
#     main_signal.set_start_button_text.connect(_slot_fun)
#     main_signal.set_start_button_state.connect(_slot_fun_bool)
#     main_signal.set_output_box_cursor.connect(_slot_fun)
#     main_signal.draw_background.connect(_slot_fun_none)
#
#     main_signal.set_output_box.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.clear_output_box.emit()
#     assert test_reflect is None
#
#     main_signal.append_output_box.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.insert_output_box.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.append_output_box_.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.insert_output_box_.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.get_output_box.emit()
#     assert test_reflect is None
#
#     main_signal.set_start_button_text.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.set_start_button_state.emit(test_bool)
#     assert test_reflect == test_bool
#
#     main_signal.set_output_box_cursor.emit(test_data)
#     assert test_reflect == test_data
#
#     main_signal.draw_background.emit()
#     assert test_reflect is None
