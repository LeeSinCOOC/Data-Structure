def dib(need,give):
    dib_ = give - need
    fifty_ = dib_ // 50
    fifty_c = dib_ % 50

    tw_ = fifty_c // 20
    tw_c = fifty_c % 20

    ten_ = tw_c // 10
    ten_c = tw_c % 10

    fiv_ = ten_c // 5
    fiv_c = ten_c % 5

    one = fiv_c

    return '找零：{}\n 50---{}张\n 20---{}张\n 10---{}张\n 5---{}张\n 1---{}张'.\
           format(dib_,fifty_,tw_,ten_,fiv_,one)

a = dib(23,100)
print(a)

    
