# test for wrap error

from subprocess import PIPE
from subprocess import call
from subprocess import Popen
rtnCode = call(["lsl", "-l"], shell=True)
print "rtnCode", rtnCode
try:
    proc = Popen(['echohh', "to STDOUT\n"],
                 stdout = PIPE,)
    stdot = proc.communicate()[0]
    print stdot
except OSError:
    print "Wrong answer"


def test_throw():
    try:
        proc = Popen(['echo', "to STDOUT"],
                     stdout = PIPE,)
        stdot = proc.communicate()[0]
        print stdot
        return 1
    except OSError:
        print "Error in wrapping"
        return -1

rtn = test_throw()
print "answer is : ", rtn

