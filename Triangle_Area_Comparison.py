
#Shandra Bryant Triangle Area Comparison

class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0
        
    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
        
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
    
    def print_info(self):
        print('Triangle with larger area:')
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))
            
if __name__ == "__main__":    
    triangle1 = Triangle()
    triangle2 = Triangle()
    
    triangle1.set_base(3)
    triangle1.set_height(4)
    triangle2.set_base(4)
    triangle2.set_height(5)   
    
    if triangle1.get_area()>triangle2.get_area():
       triangle1.print_info()
    else: 
        triangle2.print_info()
    