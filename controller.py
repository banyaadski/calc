import model as model
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    value_operand = view.get_function()
    model.init(value_a,value_b)
    if value_operand is "+": result = model.do_it_sum()
    if value_operand is "-": result = model.do_it_subt()
    if value_operand is "/": result = model.do_it_div()
    if value_operand is "*": result = model.do_it_mult()
    view.view_data(result, 'result')