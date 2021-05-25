class Scene:
  def __init__(self, dimensions):
    self.objects = []
    self.width = dimensions[0]
    self.height = dimensions[1]

  def render(self):
    positions = []
    for object in self.objects:
      positions.append(object.location)
    for height in range(self.height):
      for width in range(self.width):
        if (width, height) in positions:
          print('X', end="")
        else:
          print('-', end="")
      print(" ")

  def add_object(self, object):
    self.objects.append(object)
    
class Object:
  def __init__(self, location):
    self.location = location


scene1 = Scene((50, 20))


scene1.add_object(Object((2, 2)))
scene1.add_object(Object((0, 6)))

scene1.render()
