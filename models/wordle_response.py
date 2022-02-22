class WordleRespBody(object):
  def __init__(self, alphabet, isFound):
    self.alphabet = alphabet
    self.isFound = isFound # 0 = not found, 1 = found but wrong position, 2 = found and correct position
