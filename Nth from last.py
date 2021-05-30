from LinkedList import LinkedList

def nThfromlast(ll,n):
    pointer1=ll.head
    pointer2=ll.head

    for i in range(n):
        if ll.head is None:
            return None
        pointer2=pointer2.next

    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next


    return pointer1


customDll=LinkedList()
customDll.generate(10,0,99)
print(customDll)
print(nThfromlast(customDll,5))

