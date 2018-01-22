def select(command):
    # this is select function



def add():
    # this is add function


def change():
    # this is change function


def delete():
    # this is delete function


def main():
    # 欢迎信息
    print('welcome!you can search add change or delete elements in the chart')
    user_input = input('PLEASE ENTER THE COMMAND:')
    # 将用户输入的字符串按空格分割，转换成列表
    user_input = user_input.split()
    if user_input[0] == 'SELECT':
        # call select function
        select(user_input)

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
