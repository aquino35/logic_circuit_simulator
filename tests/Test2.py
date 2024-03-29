from unittest import TestCase
import pytest
from Components.Clock import clock
from Components.Constant import const
from Components.Gates import Gates
from Components.Inverter import Inverter
from Components.Mux41 import Mux
from Components.Switch import switch
from Components.USR import usr
from System.logicCircuitSystem import LogicCircuitSystem


class Test2(TestCase):
    """
    Description:
    Third tester class testing for outputs of components, valueErrors and outputting textfile required.
    """
    def test_output(self):
        andGate = Gates("AND0", "AND")

        andGate.Output([1, 0])
        self.assertEqual(andGate.result, 0, "The expected result is Zero")

        andGate.Output([1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
        self.assertEqual(andGate.result, 0, "The expected result is Zero")

        andGate.Output([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(andGate.result, 1, "The expected result is One")

        orGate = Gates("OR0", "OR")

        orGate.Output([1, 0, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(orGate.result, 1, "The expected result is One")
        orGate.Output([0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(orGate.result, 1, "The expected result is One")

        orGate.Output([0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(orGate.result, 0, "The expected result is Zero")

        nandGate = Gates("NAND0", "NAND")
        nandGate.Output([1, 0])
        self.assertEqual(nandGate.result, 1, "The expected result is One")

        norGate = Gates("NOR0", "NOR")
        norGate.Output([1, 0])
        self.assertEqual(norGate.result, 0, "The expected result is Zero")

        xorGate = Gates("XOR0", "XOR")
        xorGate.Output([0, 1]) # the only way we get a one
        self.assertEqual(xorGate.result, 1, "The expected result is One")

        xorGate.Output([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
        assert xorGate.result == 0, "The expected result was zero"
        xorGate.Output([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(xorGate.result, 0, "The expected result is Zero")

        xorGate.Output([1, 1, 1, 1, 1, 1, 1 , 1, 1, 1])
        self.assertEqual(xorGate.result, 0, "The expected result is Zero")

        # clck = clock("clck0", 1)
        # usrObject = usr("usr0", [1, 1, 1, 1])  # usr obj
        # print(usrObject.__doc__)  # printing USR documentation
        # usrObject.Output([1, 1])
        # print("-------------")
        # print("the USR Shift", usrObject.interior_seq)
        # print("The USR result is", usrObject.result)
        # print("-------------")
        # assert usrObject.result == 1, "The expected result was one"

        switchObj = switch("Switch0")
        switchObj.Output([101, 100, 0])
        self.assertEqual(switchObj.result, 101, "The expected result is 101")

        switchObj.Output([101, 100, 1])
        self.assertEqual(switchObj.result, 100, "The expected result is 100")

        switchObj.Output([101, None , 1])
        self.assertEqual(switchObj.result, 100, "The expected result is 100")

        switchObj.Output([None, None , 0])
        self.assertEqual(switchObj.result, 101, "The expected result is 101")

        switchObj.Output([None, None , 0])
        self.assertEqual(switchObj.result, None, "The expected result is 'none''")

        muxObject = Mux("Mux0")  # mux obj
        muxObject.Output([[10101], [1001], [110010], [10001010], 0, 1])
        self.assertEqual(muxObject.result, [1001], "The expected result is [1001]")


    def test_operate(self):  # testing the clck obj
        clockObject1 = clock("clck0", 1)
        clockObject1.Output(1)
        self.assertEqual(clockObject1.result, 0, "The expected result is Zero")

    def test_const(self):  # testing const obj
        constantObj = const("cosnt0", 1)
        self.assertEqual(constantObj.result, 1, "The expected result is One")

    def testraise(self):

        # testing switch value error
        with pytest.raises(ValueError):

            csntObj = const("Cst", 5520)
            self.assertRaises(ValueError, csntObj, csntObj.result,"Value must be binary")  # testing for none error

            csntObj = const("Cst", None)
            self.assertRaises(ValueError, csntObj, csntObj.result,"Value must be binary")  # testing for none error

            clkObj = const("Clk", 14)
            self.assertRaises(ValueError, clkObj, clkObj.result,"Value must be binary")  # testing for none erro

            clkObj = const("Clk", None)
            self.assertRaises(ValueError, clkObj, clkObj.result,"Value must be binary")  # testing for none error


            andGate = Gates("AND0", "AND")
            self.assertRaises(ValueError, andGate, andGate.Output([None, 1])," 'AND' Gate must have two binary inputs")  # testing for none error

            andGate = Gates("OR0", "OR")
            self.assertRaises(ValueError, andGate, andGate.Output([])," 'OR' Gate must have two binary inputs")  # testing for none error

            nandGate = Gates("NAND0", "NAND")
            self.assertRaises(ValueError, nandGate, nandGate.Output([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]),"NandGate cannot have more than two inputs")  # testing for size error

            norGate = Gates("NOR0", "NOR")
            self.assertRaises(ValueError, norGate, norGate.Output([1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1]),"NorGate cannot have more than two inputs")  # testing for size error

            #testing for switch errors
            switchObj = switch("Switch0")
            self.assertRaises(ValueError, switchObj, switchObj.Output([100, 200, 3, 0, 1]),"Switch cannot have more than three inputs")# Assertion error because of three or more inputs
            # #testing Value error
            muxObject = Mux("Mux0")  # mux obj
            self.assertRaises(ValueError, muxObject, muxObject.Output([[10101], [1001], [110010], [10001010], 7, 1]), "Mux selection must be binary")# Assertion error because of three or more inputs


    def test_Sys(self):  # this test creates a textfile that Simulates the System.

        a = const("Cnst1", 1)
        b = const("Cnst2", 0)
        c = clock("clk0", 1)
        d = usr("USR1", [0, 1, 0, 0])
        e = usr("USR2", [1, 0, 1, 0])
        f = Gates("AND1", "AND")
        g = Gates("AND2", "AND")
        h = Gates("OR1", "OR")
        i = usr("USR3")
        j = Mux("Mux0")
        #k = Gates("OR2", "OR")

        connection_dict = {a: [],
                           b: [],
                           c: [],
                           d: [a, a, b, b, a, b, a, c],
                           e: [b, b, a, b, a, a, a, c],
                           f: [a, a],
                           g: [c, b],
                           h: [f, g],
                           i: [a, b, b, b, a, h, b, c],
                           j: [c, b ,i, g, a, b]}
                          # k:[b,i]}

        Test_Sys = LogicCircuitSystem(connection_dict, 7)
        print(Test_Sys.network_dict)
        # print(d.__doc__)
        # print(Test_Sys.__doc__)
        # print(Test_Sys.traverse.__doc__)
        # print(Test_Sys.organize.__doc__)
