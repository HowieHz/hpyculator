RAW_VERSION = "1.4.2"  # todo 发布的时候改版本号

if "w" in RAW_VERSION:
    VERSION = RAW_VERSION + " \n警告：开发版本，可能有未知bug\n"
else:
    VERSION = RAW_VERSION

# 尾巴越短越新
# 下一个稳定版版本 1.4.2
# 下一个预览版版本 1.4.2-epsilon
# 下一个周结算 22w20
# 下一个开发大版本迭代 22w20c
# 下一个目前小版迭代 22w20c-Delta
# 下一个提交迭代 22w20c-Delta.1
#
#
# 版本号更新约定（x为更新的版本号）:
#
# 大改动，重写(api可能需要更新):                V x.*.*
# 改进，完成TODO(api可能需要更新):              V *.x.*
# 修bug，小问题:                              V *.*.x
# 分支（以及内测版，预览版。此处x为小写字母）:      V *.*.*-x
#
# 开发周结算 22w19
# 开发大版本迭代 22w19a
# 开发小版迭代 22w19a-a
# 开发提交迭代 22w19a-a.1
#
# 正式版 V x.x.x
# 正式测试预览版 V x.x.x-alpha(beta……
#
# 正式版  开发大版本迭代  开发小版本迭代   开发小版本迭代   开发提交迭代   开发提交迭代    开发小版本迭代   开发大版本迭代  正式预览版       正式预览版             正式版
# v1.0.0 22w18a        22w18b-a      22w18b-b       22w18b-c.1   22w18b-c.2    22w18b-c       22w18b       v1.1.0-alpha   v1.1.0-alpha.1        v1.1.0
#
# geek=[
#     'Alpha',
#     'Beta',
#     'Gamma',
#     'Delta',
#     'Epsilon',
#     'Zeta',
#     'Nu',
#     'Xi',
#     'Omicron',
#     'Pi',
#     'Rho',
#     'Sigma',
#     'Eta',
#     'Theta',
#     'Iota',
#     'Kappa',
#     'Lambada',
#     'Mu',
#     'Tau',
#     'Upsilon',
#     'Phi',
#     'Chi',
#     'Psi',
#     'Omega']
