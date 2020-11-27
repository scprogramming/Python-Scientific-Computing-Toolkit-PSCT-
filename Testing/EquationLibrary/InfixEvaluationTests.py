from EquationLibrary.InfixEvaluation import evaluate

infixExpression = "2*(5*(3+6))/15-2"
assert evaluate(infixExpression) == 4.0

infixExpression = "2^3*(5*(3+6))/15-2+1/2"
assert evaluate(infixExpression) == 22.5

infixExpression = "2^3*(5^4*(3^3+6^2))/15*2*1-2+1/2"
assert evaluate(infixExpression) == 41998.5

infixExpression = "0+2+(3*0)+2^0"
assert evaluate(infixExpression) == 3



