# Stack-Based Expression Evaluator

This project implements an **expression evaluation system** using a **stack-based approach** to process mathematical equations. The goal is to evaluate arithmetic expressions with different operators and parentheses, following the correct order of operations (PEMDAS: Parentheses, Exponents, Multiplication and Division, Addition and Subtraction).

### Key Features:
- **Operator Precedence**: The system correctly handles operators based on their precedence (e.g., multiplication before addition).
- **Parentheses Handling**: Supports expressions with parentheses (round brackets `()`, square brackets `[]`, and curly braces `{}`) to prioritize the operations within them.
- **Arithmetic Operations**: The system supports basic arithmetic operations, including addition, subtraction, multiplication, and division.
- **Expression Validation**: Ensures that the given expression is valid and correctly formatted, handling errors such as mismatched parentheses or invalid characters.

### Purpose:
The project simulates a **mathematical expression evaluator** that processes complex expressions containing multiple operators and operands. It offers an efficient way to calculate results, even for expressions with nested structures, while ensuring accurate operator precedence and parentheses handling.

By leveraging a stack data structure, this system is designed to:
- Parse and evaluate expressions dynamically.
- Handle multiple types of grouping symbols (parentheses, brackets, and braces).
- Provide clear feedback for invalid expressions, ensuring that only well-formed equations are processed.
