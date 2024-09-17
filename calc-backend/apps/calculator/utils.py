# import google.generativeai as genai
# import ast 
# import json
# from PIL import Image
# from constant import GEMINI_API_KEY

# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel(model_name = "gemini-1.5-flash")
# def analyze_image(img: Image, dict_of_vars: dict):
#     dict_of_vars_str = json.dumps(dict_of_vars, ensure_ascii = False)  
#     prompt = (
#         f"You have been given an image with some mathematical expressions, equations, or graphical problems, and you need to solve them. "
#         f"Note: Use the PEMDAS rule for solving mathematical expressions. PEMDAS stands for the Priority Order: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right). Parentheses have the highest priority, followed by Exponents, then Multiplication and Division, and lastly Addition and Subtraction. "
#         f"For example: "
#         f"Q. 2 + 3 * 4 "
#         f"(3 * 4) => 12, 2 + 12 = 14. "
#         f"Q. 2 + 3 + 5 * 4 - 8 / 2 "
#         f"5 * 4 => 20, 8 / 2 => 4, 2 + 3 => 5, 5 + 20 => 25, 25 - 4 => 21. "
#         f"YOU CAN HAVE FIVE TYPES OF EQUATIONS/EXPRESSIONS IN THIS IMAGE, AND ONLY ONE CASE SHALL APPLY EVERY TIME: "
#         f"Following are the cases: "
#         f"1. Simple mathematical expressions like 2 + 2, 3 * 4, 5 / 6, 7 - 8, etc.: In this case, solve and return the answer in the format of a LIST OF ONE DICT [{{'expr': given expression, 'result': calculated answer}}]. "
#         f"2. Set of Equations like x^2 + 2x + 1 = 0, 3y + 4x = 0, 5x^2 + 6y + 7 = 12, etc.: In this case, solve for the given variable, and the format should be a COMMA SEPARATED LIST OF DICTS, with dict 1 as {{'expr': 'x', 'result': 2, 'assign': True}} and dict 2 as {{'expr': 'y', 'result': 5, 'assign': True}}. This example assumes x was calculated as 2, and y as 5. Include as many dicts as there are variables. "
#         f"3. Assigning values to variables like x = 4, y = 5, z = 6, etc.: In this case, assign values to variables and return another key in the dict called {{'assign': True}}, keeping the variable as 'expr' and the value as 'result' in the original dictionary. RETURN AS A LIST OF DICTS. "
#         f"4. Analyzing Graphical Math problems, which are word problems represented in drawing form, such as cars colliding, trigonometric problems, problems on the Pythagorean theorem, adding runs from a cricket wagon wheel, etc. These will have a drawing representing some scenario and accompanying information with the image. PAY CLOSE ATTENTION TO DIFFERENT COLORS FOR THESE PROBLEMS. You need to return the answer in the format of a LIST OF ONE DICT [{{'expr': given expression, 'result': calculated answer}}]. "
#         f"5. Detecting Abstract Concepts that a drawing might show, such as love, hate, jealousy, patriotism, or a historic reference to war, invention, discovery, quote, etc. USE THE SAME FORMAT AS OTHERS TO RETURN THE ANSWER, where 'expr' will be the explanation of the drawing, and 'result' will be the abstract concept. "
#         f"Analyze the equation or expression in this image and return the answer according to the given rules: "
#         f"Make sure to use extra backslashes for escape characters like \\f -> \\\\f, \\n -> \\\\n, etc. "
#         f"Here is a dictionary of user-assigned variables. If the given expression has any of these variables, use its actual value from this dictionary accordingly: {dict_of_vars_str}. "
#         f"DO NOT USE BACKTICKS OR MARKDOWN FORMATTING. "
#         f"PROPERLY QUOTE THE KEYS AND VALUES IN THE DICTIONARY FOR EASIER PARSING WITH Python's ast.literal_eval."
#     )
#     response = model.generate_content([prompt, img])
#     print(response.text)
#     answers=[]
#     try:
#         answers = ast.literal_eval(response.text)
#     except Exception as e:
#         print(f"Error in parsing the response: {e}")
#     print('returned answer ', answers)

#     for answer in answers:
#         if 'assign' in answer:
#             answer['assign'] = True
#         else:
#             answer['assign'] = False
#     return answers




import google.generativeai as genai
import ast 
import json
from PIL import Image
from constant import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name = "gemini-1.5-flash")
def analyze_image(img: Image, dict_of_vars: dict):
    dict_of_vars_str = json.dumps(dict_of_vars, ensure_ascii=False)
    prompt = f"""
    Analyze the given image containing mathematical expressions, equations, or graphical problems. Solve them accurately and return the results in the specified format. Follow these guidelines:

    1. Mathematical Order of Operations:
       - Use the PEMDAS rule: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right).
       - Example 1: 2 + 3 * 4 = 2 + 12 = 14
       - Example 2: 2 + 3 + 5 * 4 - 8 / 2 = 2 + 3 + 20 - 4 = 21

    2. Problem Types and Response Formats:
       a) Simple Mathematical Expressions:
          Format: [{{"expr": "given expression", "result": calculated_answer}}]
          Example: [{{"expr": "2 + 2", "result": 4}}]

       b) Equation Sets:
          Format: [{{"expr": "variable", "result": value, "assign": True}}, ...]
          Example: [{{"expr": "x", "result": 2, "assign": True}}, {{"expr": "y", "result": 5, "assign": True}}]

       c) Variable Assignments:
          Format: [{{"expr": "variable", "result": value, "assign": True}}]
          Example: [{{"expr": "x", "result": 4, "assign": True}}]

       d) Graphical Math Problems:
          - Analyze drawings representing scenarios like collisions, trigonometry, Pythagorean theorem, etc.
          - Consider color-coding in the image.
          Format: [{{"expr": "problem description", "result": calculated_answer}}]

       e) Abstract Concepts:
          - Interpret drawings showing concepts like emotions, historical events, or scientific discoveries.
          Format: [{{"expr": "drawing explanation", "result": "abstract concept"}}]

    3. Additional Instructions:
       - Use the provided dictionary of variables: {dict_of_vars_str}
       - For fractions, convert to decimals rounded to 4 decimal places.
       - For equations with multiple solutions, list all solutions.
       - If a problem involves multiple steps, show key intermediate results.
       - For graphical problems, describe your interpretation before solving.
       - Handle special mathematical notations (e.g., square roots, integrals) appropriately.
       - If the image contains text, incorporate it into your analysis.

    4. Output Formatting:
       - Ensure proper quoting of dictionary keys and values for parsing with ast.literal_eval.
       - Use double backslashes for escape characters (e.g., \\\\n, \\\\t).
       - Do not use backticks or markdown formatting.

    Analyze the image thoroughly and provide a comprehensive solution following these guidelines.
    """
    response = model.generate_content([prompt, img])
    print(response.text)
    answers = []
    try:
        answers = ast.literal_eval(response.text)
    except Exception as e:
        print(f"Error in parsing the response: {e}")
    print('returned answer ', answers)

    for answer in answers:
        answer['assign'] = 'assign' in answer and answer['assign']
    return answers