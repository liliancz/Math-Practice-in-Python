
#buttons
class Button:
    def _init_ (B, _x, _y, _w, _h):
    	B.x = _x
    	B.y = _y
    	B.w = _w
    	B.y = _y	
    	B.x_w = _x + _w
    	B.y_h = _y + _h
    	B.set(_x,_y,_w,_h)
    	B.clicked = False
    

    def set (B, _x,_y,_w,_h):
        B.x = _x
        B.y = _y
        B.w = _w
        B.y = _y	
        B.x_w = _x + _w
        B.y_h = _y + _h

    
    
    
