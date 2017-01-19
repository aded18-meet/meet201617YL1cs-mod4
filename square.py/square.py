from rectangle import Rectangle
class square(Rectangle):
  def  __init__(self,length):
          super(square,self).__init__(length,length)
          def set_length(self,new_length):
              new_length>=0
                  self.length=new_length
                  self.height=new_length
                      if self.has_been_drawn:
                          self.draw_shape()
               def set_height(self,new_height):
                   
                     if new_height>=0 :
            self.height=new_height
            if self.has_been_drawn : #Only redraw rectangle; don't make new drawing.
                self.draw_shape()         
          
