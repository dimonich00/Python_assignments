from flask import Flask, render_template, request
from app import app
import math


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    figure = request.form.get('figure')
    if figure == 'circle':
        radius = float(request.form.get('radius', 0))
        if radius < 0:
            return render_template('result.html', result=f"Radius must be positive")
        area = math.pi * radius**2
        return render_template('result.html', result=f"The area of the circle is {area:.2f}")
    elif figure == 'rectangle':
        width = float(request.form.get('width', 0))
        height = float(request.form.get('height', 0))
        area = width * height
        if area < 0:
            return render_template('result.html', result=f"Area must be positive")
        return render_template('result.html', result=f"The area of the rectangle is {area:.2f}")
    elif figure == 'triangle':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
        return render_template('result.html', result=f"The area of the triangle is {area:.2f}")
    else:
        return render_template('result.html', result="Invalid figure selected.")

@app.route('/render-form', methods=['GET'])
def render_form():
    figure = request.args.get('figure')
    if figure == 'circle':
        return render_template('circle_form.html')
    elif figure == 'rectangle':
        return render_template('rectangle_form.html')
    elif figure == 'triangle':
        return render_template('triangle_form.html')
    else:
        return ""

if __name__ == '__main__':
    app.run(debug=True)
