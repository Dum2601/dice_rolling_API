"""
MIT License

Copyright (c) 2026 Douglas Barbosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from src.dice_logic.die import Die
from src.dice_logic.rpg_die import RpgDices
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/die")
def die_values():
    # use route: http://127.0.0.1:5000/die for 1 die with 6 sides
    # or http://127.0.0.1:5000/die?sides=<int>&quantity=<int> for choose the quantity of dice and/or sides
    sides = int(request.args.get("sides", 6))  # default 6
    quantity = int(request.args.get("quantity", 1))  # default 1
    die = Die(sides, quantity).die_result_json
    return jsonify(die)

@app.route("/rpg-dice")
def rpg_dice():
    # use route: http://127.0.0.1:5000/rpg-dice for 1 die with 6 sides
    # or http://127.0.0.1:5000/rpg-dice?sides=8&quantity=2&modifiers=1,2 for choose the quantity of dice, modifiers and/or sides
    sides = int(request.args.get("sides", 6))
    quantity = int(request.args.get("quantity", 1))
    modifiers_str = request.args.get("modifiers", "")  # example: "1,2"

    modifiers = []
    if modifiers_str:
        for m in modifiers_str.split(","):
            if m:
                modifiers.append(int(m))

    dice = RpgDices(sides=sides, quantity=quantity, modifiers=modifiers)
    return jsonify(dice.rpg_dice_json)


