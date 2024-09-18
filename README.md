https://github.com/user-attachments/assets/5ec37134-bdae-463f-baad-cf8e23e1ce62

# CalcPlus
Advanced calculator with standard, scientific, and AI-powered computational capabilities. Features natural language input, predictive calculations, and data analysis tools. Built with React, TypeScript, and integrates cutting-edge machine learning models. Combines traditional calculation with intelligent, context-aware problem-solving.
# Math Problem Solver

This project is a web application that allows users to draw mathematical expressions, equations, or graphical problems on a canvas and get solutions using AI-powered image analysis.

## Features

- Interactive drawing canvas
- Color selection for drawing
- Eraser functionality
- AI-powered image analysis for solving mathematical problems
- LaTeX rendering of solutions
- Draggable solution display

## Technology Stack

- Backend: Python with FastAPI
- Frontend: React with TypeScript
- AI: Google's Generative AI (Gemini 1.5 Flash)
- Additional libraries: MathJax for LaTeX rendering, react-draggable for solution positioning

## Setup and Installation

1. Clone the repository:
   ```
   git clone [https://github.com/shashank651156/CalcPlus]
   cd [CalcPlus]
   ```

2. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install frontend dependencies:
   ```
   cd frontend
   npm install
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add the following variables:
     ```
     GEMINI_API_KEY=[Your Gemini API Key]
     SERVER_URL=[Your Server URL]
     PORT=[Your Port Number]
     ENV=[dev/prod]
     ```

5. Start the backend server:
   ```
   python main.py
   ```

6. Start the frontend development server:
   ```
   cd frontend
   npm run dev
   ```

## Usage

1. Open the application in your web browser.
2. Use the canvas to draw your mathematical problem.
3. Select colors using the color swatches.
4. Use the eraser button to correct mistakes.
5. Click "Calculate" to send the image for analysis.
6. View the solution rendered in LaTeX format.
7. Drag the solution to reposition it on the canvas.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
