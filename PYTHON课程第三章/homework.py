def filter(command, staff_list):
    # initial filter_list as empty list
    filter_list = []
    #according to command,choose filter method
    if command[1] in ['>', '<', '=']:
        conditon_number = int(command[-1])
        if command[0] == 'age':
            screening_item = 2
        elif command[0] == 'staff_id':
            screening_item = 0
        elif command[0] == 'dept':
            pass
        else:
            #filter condition error
            print('format error!')
            return
        if command[1] == '>':
            for staff in staff_list:
                if int(staff[screening_item]) > conditon_number:
                    filter_list.append(staff)
        elif command[1] == '<':
            for staff in staff_list:
                if int(staff[screening_item]) < conditon_number:
                    filter_list.append(staff)
        elif command[1] == '=':
            if command[0] != 'dept':
                for staff in staff_list:
                    if int(staff[screening_item]) == conditon_number:
                        filter_list.append(staff)
            else:
                dept = command[-1][1:-1]
                for staff in staff_list:
                    if staff[4] == dept:
                        filter_list.append(staff)
                    else:
                        pass

    elif command[1] == 'like':
        # 还是字典比较好啊
        for staff in staff_list:
            for item in staff[1:]:
                if command[-1][1:-1] in  item:
                    filter_list.append(staff)

    return filter_list


def select(command, staff_list):
    # this is select function
    filter_command = command[5:]
    # 根据command内容，对staff_list进行筛选
    filter_list = filter(filter_command, staff_list)
    # if filter_list not none
    print(filter_list)
    return

# def add():
#     # this is add function
#
#
# def change():
#     # this is change function
#
#
# def delete():
#     # this is delete function


def main():
    # 文件预处理，将文件转为二级列表
    with open('staff_list.csv', 'r') as f:
        staff_list = []
        for line in f:
            staff = line.strip().split(',') # 首先删除头尾的空格和换行符，再以','分割，返回一个列表赋值给staff
            staff_list.append(staff)    # 此处不可用a = a.append()的形式，因为.append方法是没有返回值的。

    # 欢迎信息
    print('welcome!you can search-add-change-delete elements in the chart')
    user_input = input('PLEASE ENTER THE COMMAND:')
    # 将用户输入的字符串按空格分割，转换成列表
    user_input = user_input.split()

    # 根据列表内容不同调用四大函数
    if user_input[0] == 'SELECT':
        # call select function
        select(user_input, staff_list)

    elif user_input[0] == 'ADD':
        add(user_input)

    elif user_input[0] == 'CHANGE':
        change(user_input)

    elif user_input[0] == 'DELETE':
        delete(user_input)

    else:
        print('false!')


if __name__=='__main__':
    while True:
        main()
