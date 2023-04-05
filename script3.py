acl=int(input("ingrese el numero de la ACL IPV4: "))

if acl >= 1 and acl <= 99:
    print("tu ACL es standard")
elif acl >=100 and acl <=199:
    print("tu acl es extendida")
else:
    print("ingrese un numero valido de ACL")

