import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='714117', db='mysql')
cursor = conn.cursor()
cursor.execute('show databases;')
cursor.execute('use pythonclass;')


# ID 姓名 年龄 性别 身份证号码    建表
# cursor.execute('create table Student(id int primary key auto_increment,'
#                'name varchar(8) not null,'
#                'age int, '
#                'sex varchar(3),'
#                'ID_card varchar(18))')

# cursor.execute('desc Student')
# row = cursor.fetchall()
# print(row)


def add_stu():
    try:
        id = input('添加的学生ID:')
        name = input('添加的学生姓名:')
        age = int(input('添加的学生年龄:'))
        sex = input('添加的学生性别:')
        ID_card = input('添加的学生身份证号码:')

        ad = "insert into Student values ('{}','{}',{},'{}','{}')".format(id, name, age, sex, ID_card);
        cursor.execute(ad)
        conn.commit()

        print('-------------------------')
        print('添加成功')
        print('学生   ID:', id)
        print('学生  姓名:', name)
        print('学生  年龄:', age)
        print('学生  性别:', sex)
        print('身份证号码:', ID_card)
        print('-------------------------')
    except:
        print('id 重复')

    print('**********************************')
    print('返回首页')


def show_stu():
    print("""        *1 ---> 单个学生信息
        *2 ---> 全部学生信息""")
    a = input('请选择:')
    if a == '1':
        id = input('请输入要查询的学生id:')
        cursor.execute('select * from Student where id = {}'.format(id))
        row = cursor.fetchall()
        try:
            if str(row[0][0]) == id:
                print(row)
                conn.commit()
        except:
            print('查不到此学生的信息...')
    elif a == '2':
        print('所有学生信息:')
        cursor.execute('select * from Student')
        conn.commit()
        row = cursor.fetchall()
        for i in row:
            print(i)
    else:
        print('无此选项')

    print('**********************************')
    print('返回首页')


def update_stu():
    id = input('请输入要修改的学生ID:')
    cursor.execute('select * from Student where id = {}'.format(id))
    row = cursor.fetchall()

    try:
        if str(row[0][0]) == id:
            new_id = input('请输入修改后的学生ID:')
            new_name = input('请输入修改后的学生姓名:')
            new_age = input('请输入修改后的学生年龄:')
            new_sex = input('请输入修改后的学生性别:')
            new_id_card = input('请输入修改后的学生身份证号码:')

            up = "update Student set id={},name='{}',age={},sex='{}',ID_card='{}' where id='{}' " \
                .format(new_id, new_name, new_age, new_sex, new_id_card, id)
            cursor.execute(up)
            conn.commit()
            print('修改成功')
    except:
        print('查不到此学生的信息...')
        print('无法对其进行修改.....')

    print('**********************************')
    print('返回首页')


def delete_stu():
    id = input('请输入要删除的学生ID:')
    cursor.execute('select * from Student where id = {}'.format(id))
    row = cursor.fetchall()

    try:
        if str(row[0][0]) == id:
            de = "delete from Student where id={}".format(id)
            cursor.execute(de)
            conn.commit()
            print('删除成功')
    except:
        print('查不到此学生的信息...')
        print('无法删除.............')

    print('**********************************')
    print('返回首页')


def main():
    while 1:
        print(""" --->** 欢迎使用学生管理系统 **<---
        *******************
        *1---> 查看学生信息*
        *2---> 添加学生信息*
        *3---> 更改学生信息*
        *4---> 删除学生信息*
        *5---> 退出管理系统*
        *******************""")

        num = input('请输入要进行的操作：')
        if num == '1':
            show_stu()
        elif num == '2':
            add_stu()
        elif num == '3':
            update_stu()
        elif num == '4':
            delete_stu()
        elif num == '5':
            print('退出管理系统......')
            break
        else:
            print('不好意思,暂时没有这个选项.....')


if __name__ == '__main__':
    main()

    cursor.close()
    conn.close()
