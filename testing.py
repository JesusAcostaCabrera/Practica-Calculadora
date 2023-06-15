import pytest
import Opt

def testAnswers():
    op = Opt.Operations(4,4)
    assert op.Sum() == 8
    assert op.Sub() == 0
    assert op.Mult() == 16
    assert op.Div() == 1