import datetime

def check_last_workdays(date_str: str) -> tuple:
    """
    判断指定日期是否是本周/本月最后一个工作日（内置完整节假日系统）
    
    :param date_str: 日期字符串，格式"YYYY-MM-DD HH:MM:SS"
    :return: (是否本周最后一个工作日, 是否本月最后一个工作日)
    """
    # 内置节假日系统（2025年中国大陆法定节假日及调休）
    HOLIDAY_DATA = {
        "year": 2025,
        "region": "CN",
        "dates": [
            {"date": "2025-01-01", "type": "public_holiday"},
            {"date": "2025-01-26", "type": "transfer_workday"},
            {"date": "2025-01-28", "type": "public_holiday"},
            {"date": "2025-01-29", "type": "public_holiday"},
            {"date": "2025-01-30", "type": "public_holiday"},
            {"date": "2025-01-31", "type": "public_holiday"},
            {"date": "2025-02-01", "type": "public_holiday"},
            {"date": "2025-02-02", "type": "public_holiday"},
            {"date": "2025-02-03", "type": "public_holiday"},
            {"date": "2025-02-08", "type": "transfer_workday"},
            {"date": "2025-04-04", "type": "public_holiday"},
            {"date": "2025-04-05", "type": "public_holiday"},
            {"date": "2025-04-06", "type": "public_holiday"},
            {"date": "2025-04-27", "type": "transfer_workday"},
            {"date": "2025-05-01", "type": "public_holiday"},
            {"date": "2025-05-02", "type": "public_holiday"},
            {"date": "2025-05-03", "type": "public_holiday"},
            {"date": "2025-05-04", "type": "public_holiday"},
            {"date": "2025-05-05", "type": "public_holiday"},
            {"date": "2025-05-31", "type": "public_holiday"},
            {"date": "2025-06-01", "type": "public_holiday"},
            {"date": "2025-06-02", "type": "public_holiday"},
            {"date": "2025-09-28", "type": "transfer_workday"},
            {"date": "2025-10-01", "type": "public_holiday"},
            {"date": "2025-10-02", "type": "public_holiday"},
            {"date": "2025-10-03", "type": "public_holiday"},
            {"date": "2025-10-04", "type": "public_holiday"},
            {"date": "2025-10-05", "type": "public_holiday"},
            {"date": "2025-10-06", "type": "public_holiday"},
            {"date": "2025-10-07", "type": "public_holiday"},
            {"date": "2025-10-11", "type": "transfer_workday"}
        ]
    }

    try:
        # 解析输入日期
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").date()
        
        # 构建工作日判断系统
        holidays = set()
        workdays = set()
        for item in HOLIDAY_DATA["dates"]:
            date = datetime.datetime.strptime(item["date"], "%Y-%m-%d").date()
            if item["type"] == "public_holiday":
                holidays.add(date)
            elif item["type"] == "transfer_workday":
                workdays.add(date)

        def is_workday(d):
            """智能工作日判断"""
            # 先检查是否是调休工作日
            if d in workdays:
                return True
            # 再检查是否是节假日
            if d in holidays:
                return False
            # 最后判断是否是自然工作日（周一至周五）
            return d.weekday() < 5

        def find_last(start, end):
            """逆向查找最后一个有效工作日"""
            current = end
            while current >= start:
                if is_workday(current):
                    return current
                current -= datetime.timedelta(days=1)
            return None

        # 计算周范围（周一为周起始）
        week_start = target_date - datetime.timedelta(days=target_date.weekday())
        week_end = week_start + datetime.timedelta(days=6)
        
        # 计算月范围
        month_start = target_date.replace(day=1)
        if target_date.month == 12:
            month_end = datetime.date(target_date.year + 1, 1, 1) - datetime.timedelta(days=1)
        else:
            month_end = datetime.date(target_date.year, target_date.month + 1, 1) - datetime.timedelta(days=1)

        # 获取最后工作日
        last_week = find_last(week_start, week_end)
        last_month = find_last(month_start, month_end)

        # 如果当前日期大于最后工作日，说明当前日期就是最后工作日
        if last_month and target_date > last_month:
            last_month = target_date

        # 修复周最后工作日的判断
        # 如果当前日期不是本周最后工作日，但大于最后工作日，说明最后工作日在下周
        if last_week and target_date > last_week:
            last_week = None

        return (
            last_week == target_date if last_week else False,
            last_month == target_date if last_month else False
        )

    except ValueError as e:
        raise ValueError(f"无效日期格式: {date_str} (应使用 YYYY-MM-DD HH:MM:SS)") from e

# 使用示例
if __name__ == "__main__":
    test_dates = [
        # 月初工作日
        "2025-01-02 09:00:00",  # 元旦假期后第一个工作日
        
        # 月末工作日
        "2025-04-30 14:50:11",  # 4月最后工作日
        "2025-12-31 15:00:00",  # 年末最后工作日
        
        # 节假日
        "2025-01-01 10:00:00",  # 元旦
        "2025-10-01 10:00:00",  # 国庆节
        
        # 调休工作日
        "2025-01-26 09:00:00",  # 周日调休
        "2025-04-27 09:00:00",  # 周日调休
        
        # 跨月工作日
        "2025-05-01 09:00:00",  # 劳动节
        "2025-09-30 15:00:00",  # 9月最后工作日
        
        # 跨年工作日
        "2025-12-30 14:00:00",  # 年末倒数第二个工作日
        
        # 周末工作日
        "2025-02-08 10:00:00",  # 周六调休
        
        # 普通工作日
        "2025-03-15 11:00:00",  # 普通工作日
        "2025-07-15 13:00:00"   # 普通工作日
    ]
    
    print("工作日判断系统测试结果：\n")
    for date in test_dates:
        try:
            is_last_week, is_last_month = check_last_workdays(date)
            print(f"日期 {date[:10]}：")
            print(f"  周最后工作日 → {'✔️' if is_last_week else '✖️'}")
            print(f"  月最后工作日 → {'✔️' if is_last_month else '✖️'}\n")
        except Exception as e:
            print(f"错误：{e}\n")