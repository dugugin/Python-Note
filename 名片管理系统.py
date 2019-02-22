mycard = [{"name":"appple","phone":"111231"},
         {"name":"boy111","phone":"2211232"},
         {"name":"dood","phone":"42344"}]



def new_card():
        print( "输入要增加的名片：" )
        name = input( "姓名：" )
        phone = input( "手机：" )
        x = {"name":name,"phone":phone}
        n = len( mycard )
        i = 0

        while i < n and name > mycard[i]["name"]:
                i+=1

        if name!= mycard[i]["name"]:
                mycard.insert( i,x )
        else:
                print("\tError：已存在该联系人信息，无法插入。")


def look_all( ):
        if mycard != []:
                print(" "*65,end="")
                print( "===通讯录===" )
                print("-"*100)
                for k in mycard[0]:
                        print( "%50s"%k ,end="" )

                print( "" )
                print("-"*100)
                for x in mycard:
                        for k in x:
                                print( "%50s"%x[k] ,end="" )
                        print("" )
                print("-"*100)
                print( "" )
                
        else:
                print( "\n没有任何记录！" )


def cardrewrite(name,phone):     #      定义字典型参数的时候要展开，引用函数时字典型实参要加**
        name1 = input( "姓名：[回车不修改]" )
        if name1!="":
                name=name1
        phone1 = input( "手机：[回车不修改]" )
        if phone1!="":
                phone=phone1
        return {"name":name,"phone":phone}


def find_card( ):
        name = input( "输入想要查找的联系人姓名：" )
        for x in mycard:
                if x["name"] == name:
                        y=x
                        id=mycard.index(y)

                        for k in mycard[0]:
                                print( "%50s" % k,end="" )
                        print( "\n",end="" )
                        print( "-" * 100 )
                        for k in y:
                                print( "%50s" % y[k]  ,end="" )
                        print( "\n" )
                        
                        c=input("【1=删除，2=修改，0=结束查询】\t请选择操作功能：" )
                       
                        while c != "0":
                                if c == "1":
                                        del mycard[id]
                                        print( "\tDeleted!" )
                                elif c == "2":
                                        print( "输入更正后的信息：" )
                                        mycard[id] = cardrewrite( **mycard[id] )
                                else:
                                        print( "\tError:非法输入。" )
                                c = input( "【1=删除，2=修改，0=结束查询】\t请选择操作功能：" ) 
                        break
        else:
                print( "\tNo!通讯录没有该联系人。" )
        print( "\n" ,end="")


#       -----------------------------------main--------------------------------- #
print( "*" * 50 )
print( "欢迎使用【名片管理系统】V1.0\n\n1. 新建名片\n2. 显示全部\n3. 查询名片\n\n0. 退出系统" )
print( "*" * 50 )
# TODO(boy) sdawd
cc=input("按回车继续")
c = input( "\t请选择操作功能：" ) 
while c != "0":
        if c == "1":
                new_card()
        elif c == "2":
                look_all()
        elif c == "3":
                find_card()
        else:
                print( "\tError:非法输入。" )
        print("*"*50)
        c = input( "【1=新建，2=打印，3=查询，0=退出】\t请选择操作功能：" ) 
        
print( "Good Bye!\n按回车退出..." )
input()

