
import src.object.fund
import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import timestamp

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


nval_end_index = 761

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def create_database(database_conn):
    fund_nval = '''
        CREATE TABLE fund_nval(
            fund_name text Not Null, 
            nval_date text not null,
            nval Double not null,
            remarks text,
            primary key (fund_name, nval_date))
    '''
    database_conn.execute(fund_nval)
    print("fund_nval表创建成功！")

    fund_base_info = '''
        CREATE TABLE fund_base_info(
            fund_name text not null,
            fund_id_zyyx text,
            fund_name_zyyx text ,
            fund_id_smpp Double ,
            strategy text,
            administrator int Not Null, 
            region text ,
            manager text ,
            establish_time text ,
            report_data_source Double ,
            report_nval_type text,
            remarks text,
            primary key (fund_name))
    '''

    database_conn.execute(fund_base_info)
    print("fund_base_info表创建成功！")

def read_update_file():
    fund_base_info = pd.read_excel('../../tests/重点观察私募周报_第28周.xlsx', sheet_name='股票多头-多空')
    # fund_base_info = pd.read_excel('../../tests/重点观察私募周报-测试数据.xlsx')
    return fund_base_info

def update_database():
    output_database_dir = 'test2.db'
    conn = sqlite3.connect(output_database_dir)
    cursor = conn.cursor()
    # create_database(cursor)

    fund_base_info = read_update_file()

    time_list = fund_base_info.iloc[7: nval_end_index, 0].apply(lambda x: x.strftime('%Y-%m-%d'))
    time_list = list(np.array(time_list))

    for index, col in fund_base_info.iteritems():
        if index == 'Unnamed: 0':
            continue
        try:
            if isinstance(col[0], str) or not np.isnan(col[0]):
                fund_name, strategy, administrator, region, manager, establish_time = \
                    col[0], col[1], col[2], col[3], col[4], col[5].strftime('%Y-%m-%d')
                print(fund_name, strategy, administrator, region, manager, establish_time)
                input_info = (fund_name, strategy, administrator, region, manager, establish_time)
                try:
                    cursor.execute("insert into fund_base_info(fund_name, strategy, administrator, region, manager, establish_time)\
                    values(?, ?, ?, ?, ?, ?)", input_info)
                except sqlite3.IntegrityError as e:
                    if e.__str__().startswith('UNIQUE constraint failed'):
                        print('基金{}已经在库中了，本次未录入。该条数据详情如下：'.format(input_info[0]))
                        print(input_info)
                        continue
                    else:
                        print(e)
        except:
            print(col)
    conn.commit()

    for index, col in fund_base_info.iteritems():
        if index == 'Unnamed: 0':
            continue
        if isinstance(col[0], str) or not np.isnan(col[0]):
            fund_name = col[0]
            if fund_name == '沪深300指数':
                break
            for j in range(7, nval_end_index):
                if is_number(col[j]) and not np.isnan(col[j]):
                    input_info = (fund_name, time_list[j-7], col[j])
                    try:
                        cursor.execute("insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)", input_info)
                    except sqlite3.IntegrityError as e:
                        if e.__str__().startswith('UNIQUE constraint failed'):
                            print('基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(input_info[0], input_info[1]))
                            print(input_info)
                            continue
                        else:
                            print(e)
        else:
            continue
        conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    update_database()