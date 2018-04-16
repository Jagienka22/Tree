import unittest

class Tree: 
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.value) + ", left = (" + str(self.left) + "), right = (" + str(self.right) + ")"

  def sum(self):
    sum = self.value
    if self.left != None:
      sum += self.left.sum()
    if self.right != None:
      sum += self.right.sum()
    return sum
   
  def average(self):
      return float(self.sum())/self.number_of_elements()
    
  def number_of_elements(self):
    number = 1
    if self.left != None:
      number += self.left.number_of_elements()
    if self.right != None:
      number += self.right.number_of_elements()
    return number

  def all_values(self):
    list = [self.value]
    if self.left != None:
      list += self.left.all_values()
    if self.right != None:
      list += self.right.all_values()
    return list

  def median(self):
    median = 0
    list = self.all_values()
    list.sort()
    if len(list) % 2 == 0:
      sum_of_middle_elements = list[len(list)/2] + list[(len(list)/2)-1]
      median = sum_of_middle_elements/2.0
    else:
      median = list[len(list)/2]
    return median


class TreeTests(unittest.TestCase):
  def test1(self):
    self.assertEqual((Tree(3, Tree(6), Tree(4))).median(), 4)

  def test2(self):
    self.assertEqual(Tree(0).sum(), 0)

  def test3(self):
    self.assertEqual(Tree(2).sum(), 2)

  def test4(self):
    self.assertEqual(Tree(2, Tree(5)).sum(), 7)

  def test5(self):
    self.assertEqual(Tree(2, Tree(5), Tree(7)).sum(), 14)

  def test6(self):
    self.assertEqual(Tree(5, Tree(3, Tree(2), Tree(5)), Tree(7, Tree(1), Tree(0, Tree(2), Tree(8, None, Tree(5))))).sum(), 38)

  def test7(self):
    self.assertEqual(Tree(0).average(), 0.0)

  def test8(self):
    self.assertEqual(Tree(2).average(), 2.0)

  def test9(self):
    self.assertEqual(Tree(2, Tree(5)).average(), 3.5)

  def test10(self):
    self.assertEqual(Tree(1, Tree(7)).average(), 4.0)

  def test11(self):
    self.assertEqual(Tree(2, Tree(7), Tree(3)).average(), 4.0)

  def test12(self):
    self.assertEqual(Tree(5, Tree(3, Tree(2), Tree(5)), Tree(7, Tree(1), Tree(0, Tree(2), Tree(8, None, Tree(5))))).average(), 3.8)

  def test13(self):
    self.assertEqual(Tree(0).median(), 0.0)

  def test14(self):
    self.assertEqual(Tree(2).median(), 2.0)

  def test15(self):
    self.assertEqual(Tree(2, Tree(4)).median(), 3.0)

  def test16(self):
    self.assertEqual(Tree(2, Tree(4), Tree(7)).median(), 4.0)

  def test17(self):
    self.assertEqual(Tree(5, Tree(3, Tree(2), Tree(5)), Tree(7, Tree(1), Tree(0, Tree(2), Tree(8, None, Tree(5))))).median(), 4.0)


if __name__ == "__main__":
  unittest.main()


