from modules.constants import *
from modules.utils import *
import sys

consts = Constant()

def before_all(self):
    self.const = consts
    print(sys.getdefaultencoding())