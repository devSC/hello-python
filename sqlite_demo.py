#coding=utf-8

'a demo for sqlite'

__author__ = 'Wilson'

#导入SQLite库
import sqlite3

#插入数据
def testInsert():
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在, 则会自动创建
    conn = sqlite3.connect('test.db')

    # 创建一个cursor
    cursor = conn.cursor()

    # 执行一条SQL语句, 创建user表.
    cursor.execute('CREATE TABLE IF NOT EXISTS user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

    # 插入一条记录
    cursor.execute('INSERT OR IGNORE INTO user (id, name) VALUES (\'1\', \'Michael\')')

    # 获取行数
    print(cursor.rowcount)
    #log: 0

    # 关闭cursor
    cursor.close()

    # 提交事务
    conn.commit()

    # 关闭connection
    conn.close()

def testRead():
    # 连接到SQLite数据库
    # 数据库文件是test.db
    # 如果文件不存在, 则会自动创建
    conn = sqlite3.connect('test.db')

    cursor = conn.cursor()
    #执行查询语句
    cursor.execute('SELECT * FROM user WHERE id = ?', ('1',))
    #获得查询结果
    values = cursor.fetchall()

    print(values)
    #log: [('1', 'Michael')]

    cursor.close()

testInsert()
testRead()



