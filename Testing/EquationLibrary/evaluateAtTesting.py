from EquationLibrary.InfixEvaluation import evaluateAt

assert(evaluateAt("x^2+3*x+4","x",3)) == 22
assert(evaluateAt("(2*x+3)/(3*x+1)","x",1)) == 1.25
assert(evaluateAt("2x+3","x",2)) == 7
assert(evaluateAt("2x^2+46x+1","x",10)) == 661
