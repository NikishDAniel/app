page = -1
def load(increment=1):
    global page
    if page==-1:page=0
    else:
        if increment:page += 1 
        elif page:page += -1
    print(page)
while 1:
    operation = int(input('Operation : '))
    if operation==1:load()
    elif operation!=0:break
    else:load(0)