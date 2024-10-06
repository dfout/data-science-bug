char = [1]

num1 = char.pop()
num2 = char.pop()

console.log(num2)




exports.calculate = function(expression) {
    // Time Complexity: 0(n)
    // Data Structure: Stack 
    // Edge Cases: 
      // Addressed: if expression == "0"
      // Adressed: If operand is not one listed
      // Addressed: Division by zero
      // Adressed: (Left default) If decimal, to how many decimal points should we have? Currently: No set cap in this function. Default.
      // Non Numeric input
  
    // Dev Notes:
      // expression == string
      // pattern = in front --applies to behind 
      // / - 3 4 + 5 2 
      // 2,5 + -----> 5 + 2  ====> 7
      // 7, 4, 3 - -----> 3 - 4  ====> -1
      // 7, -1 / ------> -1 / 7 ======> - 0.14....
      // Data Structure: Use a stack/ array for numbers that are waiting to be calculated
  
  
    expression = expression.split(' '); // 0(n)
     if (expression.length == 1 && expression[0] == "0" || expression == " "){
     return 0
    }
    // Set of valid operators for error handling--- quick lookup
    let validOperators = new Set(['*', '/', '-','+'])
  
   // Helper function to do calculations
    function calculate(operator, num1, num2){
      switch(operator){
        case "+":{
            return num1 + num2
        }
        case "-":{
          return num1 - num2
        }
        case "/":{
          if(num2 == 0){
            throw new Error('Division by Zero is not allowed')
          }
          return (num1 / num2)
        }
        case "*":{
          return num1 * num2
        }
        default:
        throw new Error("Invalid Operator: Operator is not '*','/','+', or '-'.")
      }
    }
  
  
   // place to hold the numbers until you can operate: Stack
    let numbers = []
   // Go in reverse because there is a consistent pattern from reverse. 
   // When you hit an operand from left to right, you can compute right away
    for (let i = expression.length - 1; i >= 0; i--){ // 0(n)
      // Set variable to store character (str type)
      let char = expression[i]
      // if the character is not a number 
      if (isNaN(char)){
        // Retrieve last two numbers from the stack (most recent), but also, get them out of the stack: pop method
        // Operate and return its value to the stack : helper function
        // Error handling: check if the operator exists in the valid set of operators
        if (validOperators.has(char)){
        num1= numbers.pop()
        num2 = numbers.pop()
        if (num2 == undefined || num1 == undefined){
          throw new Error("Invalid Expression: Please input at least two numbers.")
        }
        let operator = char
        // Call the calculate function and push to the stack
        numbers.push((calculate(operator,num1, num2)))
        }else if (char.toUpperCase()== char.toLowerCase()){
          throw new Error("Invalid Operator: Operator is not '*','/','+', or '-'.")
        }else{
          throw new Error("Invalid Expression: Letters are not allowed.")
        }
      }else{
        // if character is a number we want to store it in a stack
        // Convert the character from str to num
        numbers.push(Number(char))
      }
    }
    // Return the final calculated value which is left in numbers
  
    // If there in not a final value, something went wrong
    if (numbers.length != 1){
      throw new Error('Invalid Expression.')
    }
    // Final calculation
    return numbers[0]
  }

  

  var assert = require("assert");
var calculator = require("../app/calculator");

describe("Calculator", function() {
  it("returns zero", function() {
    let result = calculator.calculate("0");
    return assert.equal(result, 0);
  });

  it("calculates addition", function() {
    let result = calculator.calculate("+ 3 4");
    return assert.equal(result, 3 + 4);
  });

  it("calculates subtraction and multiplication", function() {
    let result = calculator.calculate("- 3 * 4 5");
    return assert.equal(result, 3 - (4 * 5));  // -17
  });

  it("calculates addition and multiplication", function() {
    let result = calculator.calculate("* + 3 4 5");
    return assert.equal(result, (3 + 4) * 5);  // 35
  });
  // Wrote another test case based on task description
  it("calculates addition, subtraction, and division", function(){
    let result = calculator.calculate("/ - 3 4 + 5 2");
    return assert.equal(result, ((3 - 4) / (5 + 2))); // 1/7
  });
  // Test case for zero division
  it("throws an error when dividing by zero", function (){
    assert.throws(()=>{
      calculator.calculate("/ 4 0")
    }, /Error: Division by Zero is not allowed/)
  });
  // Test case for invalid input
  it("throws an error for malformed expressions", function(){
    assert.throws(()=> {
      calculator.calculate("+ 3")
    }, /Invalid Expression: Please input at least two numbers./)
  });
  it("throws an error if letters are included", function(){
    assert.throws(()=>{
      calculator.calculate("+ 3 a");
    }, /Invalid Expression: Letters are not allowed./)
  })
})
