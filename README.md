# 工作日判断系统

这是一个用于判断工作日状态的Python工具，特别适用于需要处理中国节假日和调休安排的场景。

## 功能特点

- 判断指定日期是否是本周最后一个工作日
- 判断指定日期是否是本月最后一个工作日
- 判断指定日期之后在本周内是否还有工作日
- 判断指定日期之后在本月内是否还有工作日
- 内置2025年中国大陆法定节假日及调休安排
- 智能处理节假日和调休工作日

## 安装要求

- Python 3.x
- datetime 模块（Python标准库）

## 使用方法

1. 基本使用：
```python
from check_last_workdays import check_last_workdays, has_next_workday_in_week, has_next_workday_in_month

# 判断是否是最后工作日
date_str = "2025-04-30 14:50:11"
is_last_week, is_last_month = check_last_workdays(date_str)
print(f"是否是本周最后工作日: {'是' if is_last_week else '否'}")
print(f"是否是本月最后工作日: {'是' if is_last_month else '否'}")

# 判断是否还有工作日
has_next_week = has_next_workday_in_week(date_str)
has_next_month = has_next_workday_in_month(date_str)
print(f"本周是否还有工作日: {'是' if has_next_week else '否'}")
print(f"本月是否还有工作日: {'是' if has_next_month else '否'}")
```

2. 日期格式：
- 输入日期格式：`YYYY-MM-DD HH:MM:SS`
- 示例：`2025-04-30 14:50:11`

## 节假日处理

系统内置了2025年中国大陆的法定节假日和调休安排，包括：
- 元旦假期
- 春节假期
- 清明节假期
- 劳动节假期
- 端午节假期
- 中秋节假期
- 国庆节假期
- 调休工作日安排

## 注意事项

1. 日期输入必须符合指定格式
2. 系统默认使用周一作为每周的第一天
3. 节假日数据需要定期更新
4. 跨年日期会自动处理

## 修订记录

详细的修订记录请查看 [CHANGELOG.md](CHANGELOG.md)

## 更新日志

### v1.0.1 (2024-03-21)
- 会话目的：修复工作日判断逻辑中的问题
- 完成的主要任务：
  - 修复了月最后工作日判断逻辑
  - 添加了当前日期大于最后工作日的处理
  - 扩展了测试用例
- 关键决策和解决方案：
  - 优化了月范围的计算逻辑
  - 增加了对当前日期位置的判断
- 使用的技术栈：
  - Python 3.x
  - datetime 模块
- 修改的文件：
  - test.py 

### v1.0.2 (2024-03-21)
- 会话目的：修复周最后工作日判断逻辑
- 完成的主要任务：
  - 修复了周最后工作日的判断逻辑
  - 优化了跨周工作日的处理
- 关键决策和解决方案：
  - 添加了对当前日期大于周最后工作日的特殊处理
  - 确保跨周情况下返回正确的判断结果
- 使用的技术栈：
  - Python 3.x
  - datetime 模块
- 修改的文件：
  - test.py 

### v1.0.3 (2024-03-21)
- 会话目的：扩展测试用例并验证系统正确性
- 完成的主要任务：
  - 添加了13个全面的测试用例
  - 优化了工作日判断逻辑
  - 验证了系统在各种情况下的表现
- 关键决策和解决方案：
  - 测试用例覆盖：月初/月末工作日、节假日、调休日、跨月/年工作日、周末工作日、普通工作日
  - 优化了工作日判断函数的可读性
- 使用的技术栈：
  - Python 3.x
  - datetime 模块
- 修改的文件：
  - test.py 

### v1.0.4 (2024-03-21)
- 会话目的：添加判断本周是否还有工作日的功能
- 完成的主要任务：
  - 添加了has_next_workday_in_week函数
  - 将HOLIDAY_DATA移至全局作用域
  - 扩展了测试用例输出
- 关键决策和解决方案：
  - 新增函数判断当前日期之后在本周期内是否还有工作日
  - 优化了代码结构，提高可维护性
  - 完善了测试用例的输出信息
- 使用的技术栈：
  - Python 3.x
  - datetime 模块
- 修改的文件：
  - check_last_workdays.py 

### v1.0.5 (2024-03-21)
- 会话目的：添加判断本月是否还有工作日的功能
- 完成的主要任务：
  - 添加了has_next_workday_in_month函数
  - 扩展了测试用例输出
- 关键决策和解决方案：
  - 新增函数判断当前日期之后在本月内是否还有工作日
  - 完善了测试用例的输出信息
- 使用的技术栈：
  - Python 3.x
  - datetime 模块
- 修改的文件：
  - check_last_workdays.py 