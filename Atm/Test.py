import unittest
from ATM import *
from ATM import Tk
from ATM import password_not_recognised
from ATM import user_not_found


class Test(unittest.TestCase):
    
 def setScreen(self):
     sc = Tk()
     self.assertEqual(sc, Tk())
     
#  def test_about(self):
#      display = about()
#      self.assertEqual(display, Label(Toplevel(screen),bg='lightpink', text = "\n\n\n Created and developed by\n SEDRIC \n\n\n Made with: \nTkinter GUI, Python with Mysql database",font = ("orbitron", 10)).pack())
    

 def test_password_not_recognised(self):
     d = password_not_recognised()
     self.assertEqual(d, None)

 def test_user_not_found(self):
     u = user_not_found()
     self.assertEqual(u, None)   


     

if __name__ == '__main__':
    unittest.main()   