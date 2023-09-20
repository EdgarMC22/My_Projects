#ifndef __MYINFIXCALCULATOR_H__
#define __MYINFIXCALCULATOR_H__

#include <algorithm>
#include <string>

#include "MyStack_e272m757.h"
#include "MyVector_e272m757.h"

class MyInfixCalculator{

  public:
    
    MyInfixCalculator()
    {

    }

    ~MyInfixCalculator()
    {
     
    }

    double calculate(const std::string& s)
    {
        // code begins
	MyVector<std::string> infix_tokens;
	MyVector<std::string> postfix_tokens;
	tokenize(s, infix_tokens);
	infixToPostfix(infix_tokens, postfix_tokens);
	return calPostfix(postfix_tokens);
        // code ends
    }

  private:

    // returns operator precedance; the smaller the number the higher precedence
    // returns -1 if the operator is invalid
    // does not consider parenthesis
    int operatorPrec(const char c) const
    {
        switch(c)
        {
			case '^':
				return 1;
            case '*':
                return 2;
            case '/':
                return 2;
			case '%':
				return 2;
            case '+':
                return 3;
            case '-':
                return 3;
            default:
                return -1;
        }
    }

    // checks if a character corresponds to a valid parenthesis
    bool isValidParenthesis(const char c) const
    {
        switch(c)
        {
            case '(':
                return true;
            case ')':
                return true;
            default:
                return false;
        }
    }

    // checks if a character corresponds to a valid digit
    bool isDigit(const char c) const
    {
        if(c >= '0' && c <= '9')
            return true;
        return false;
    }

    // computes binary operation given the two operands and the operator in their string form
    double computeBinaryOperation(const std::string& ornd1, const std::string& ornd2, const std::string& opt) const
    {
        double o1 = std::stod(ornd1);
        double o2 = std::stod(ornd2);
        switch(opt[0])
        {
			case '^':
				return pow(o1, o2);
            case '+':
                return o1 + o2;
            case '-':
                return o1 - o2;
			case '%':
				return remainder(o1, o2);
            case '*':
                return o1 * o2;
            case '/':
                return o1 / o2;
            default:
                std::cout << "Error: unrecognized operator: " << opt << std::endl;
                return 0.0;
        }
    }


    // tokenizes an infix string s into a set of tokens (operands or operators)
    void tokenize(const std::string& s, MyVector<std::string>& tokens)
    {
        // code begins
	std::string current_token = "";
	bool expecting_operator = false;
	for (size_t i = 0; i < s.size(); i++){
		char c = s[i];
		if (isDigit(c) || c == '.'){
			current_token += c;
			expecting_operator = true;
		}else if (c == '-'){
			if (expecting_operator){
				if (!current_token.empty()){
					tokens.push_back(current_token);
					current_token = "";
				}
				tokens.push_back("-");
				expecting_operator = false;
			}else {
				current_token += c;
				expecting_operator = true;
			}
		}else if (isValidParenthesis(c)){
			if (c == '('){
				if (!current_token.empty()){
					tokens.push_back(current_token);
					current_token = "";
				}
				tokens.push_back("(");
				expecting_operator = false;
			}else {
				if (!current_token.empty()){
					tokens.push_back(current_token);
					current_token = "";
				}
				tokens.push_back(")");
				expecting_operator = true;
			}
		}else if (c == ' '){
			continue;
		}else {
			if (!current_token.empty()){
				tokens.push_back(current_token);
				current_token = "";
			}
			current_token += c;
			tokens.push_back(current_token);
			current_token = "";
			expecting_operator = false;
		}
	}
	if (!current_token.empty()){
		tokens.push_back(current_token);
	}
        // code ends
    }

    // converts a set of infix tokens to a set of postfix tokens
    void infixToPostfix(MyVector<std::string>& infix_tokens, MyVector<std::string>& postfix_tokens)
    {
        // code begins
	MyStack<std::string> operator_stack;
	bool is_operand = false;
	for (const auto& token : infix_tokens){
		for (int i = 0; i < token.size(); i++){
			if (isDigit(token[i])){
				is_operand = true;
				break;
			}else {
				is_operand = false;
				continue;
			}
		}
		if (is_operand){
			postfix_tokens.push_back(token);
		}else if (token == "("){
			operator_stack.push(token);
		}else if (token == ")"){
			while ((!operator_stack.empty()) && (operator_stack.top() != "(")){
				postfix_tokens.push_back(operator_stack.top());
				operator_stack.pop();
			}
			operator_stack.pop();
		}else {
			while ((!operator_stack.empty()) && (operatorPrec(operator_stack.top()[0]) <= operatorPrec(token[0])) && (operator_stack.top() != "(")){
				postfix_tokens.push_back(operator_stack.top());
				operator_stack.pop();
			}
			operator_stack.push(token);
		}
	}
	while (!operator_stack.empty()){
		postfix_tokens.push_back(operator_stack.top());
		operator_stack.pop();
	}
        // code ends
    }

    // calculates the final result from postfix tokens
    double calPostfix(const MyVector<std::string>& postfix_tokens) const
    {
        // code begins
	MyStack<std::string> operand_stack;
	bool is_operand = false;
	for (const auto& token : postfix_tokens){
		for (int i = 0; i < token.size(); i++){
			if (isDigit(token[i])){
				is_operand = true;
				break;
			}else {
				is_operand = false;
				continue;
			}
		}
		if (is_operand){
			operand_stack.push(token);
		}else {
			std::string o2 = operand_stack.top();
			operand_stack.pop();
			std::string o1 = operand_stack.top();
			operand_stack.pop();
			std::string result = std::to_string(computeBinaryOperation(o1, o2, token));
			operand_stack.push(result);
		}
	}
	return std::stod(operand_stack.top());
        // code ends
    }
};

#endif // __MYINFIXCALCULATOR_H__
