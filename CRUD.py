loop_continue = True
while loop_continue:
    items = ['T-Shirt', 'Sweater', 'Jeans']
    print("clothes shop")
    print("1.creater(C)")
    print("2.read(R)")
    print("3.update(U)")
    print("4.delete(D)")
    print("5.thoát")
    print("--------------------------------------")
    choice = int(input("bạn muốn làm gì?"))

    def item_list():
        item_no = 1
        for item in items:
            print(item_no, end= '-')
            print(item)
            item_no += 1
    if choice == 1:
        new_item = input("nhập tên món hàng : ")
        items.append(new_item)
        item_list()
    elif choice == 2:
        item_list()
    elif choice == 3:
        position = int(input("vị trí muốn đổi(nhập số):"))
        new_item = input("nhập tên món hàng mới :")
        items[position - 1] = new_item
        item_list()
    elif choice == 4:
        position = int(input("bạn muốn xóa món hàng nào(nhập số):"))
        items.pop(position - 1)
        item_list()
    elif choice == 5:
        print("hẹn gặp lại")
        loop_continue = False
    else:
        print("sai r,nhap lại")
        print("1.creater (C)")
        print("2.read shop menu(R)")
        print("3.update(U)")
        print("4.delete(D)")
        print("5.thoát")