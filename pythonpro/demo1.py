class ShopCart():
    '''
    属性：大小、重量
    '''    
    def __init__(self,size=16,weight=2):
        self.size=size
        self.weight=weight

    '''
    行为：存放普通商品的功能
    '''
    def save(self,something='水果'):
        print("这个购物车可以存放{}".format(something))

if __name__=="__main__":
    
    # 实例化对象，不传参数
    cart1=ShopCart()
    print("这个购物车的大小是{}寸".format(cart1.size))
    print("这个购物车的重量是{}kg".format(cart1.weight))
    cart1.save()

    # 实例化对象，传参数
    cart2=ShopCart('24寸','1kg')
    print("这个购物车的大小是{},重量是{}".format(cart2.size,cart2.weight))
    cart2.save('大米')