
#buttons
class Button:
    def _init_ (B):
        B.x = 0
        B.y = 0
        B.h = 0
        B.w = 0
        B.x_w = 0
        B.y_h = 0
        B.set(_x,_y,_w,_h)
        B.clicked = False
    

    def set (B, _x,_y,_w,_h):
        B.x = _x
        B.y = _y
        B.w = _w
        B.y = _y
        B.x_w = _x + _w
        B.y_h = _y + _h

    
    
    
