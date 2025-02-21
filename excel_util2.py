from datetime import datetime

# transform excel to csv
import pandas as pd
from pandas import DataFrame

emp_dict = {"emp_no":"员工编号", "emp_name": "员工姓名", "dep_no": "部门编号", "dep_name": "部门名称"}


def excel_transform():
    # 读取excel
    df = pd.read_excel('employee_department_info.xlsx')

    xls_dict = {}

    # 遍历每行数据, 转为dict格式, 列名由英文转为中文
    for index, row in df.iterrows():
        # 按列名分组数据存到dict
        for h in df.head():
            if xls_dict.get(emp_dict.get(h)) is None:
                item_list = []
            else:
                item_list = xls_dict[emp_dict.get(h)]
            item_list.append(row[h])
            xls_dict[emp_dict.get(h)] = item_list

    # 将转换出来的dict放入pandas的DataFrame
    df_output = pd.DataFrame(xls_dict)

    # 用年月日时分秒为每次生成的csv文件名
    dt = datetime.now()
    dtYmdHms = dt.strftime('%Y%m%d%H%M%S')

    # 保存到csv
    df_output.to_csv(f'{dtYmdHms}.csv', encoding='gbk')

excel_transform()