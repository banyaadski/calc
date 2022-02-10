import model_com as model
import view

def button_click():


    # complex 
    value_a = view.get_value()
    value_b = view.get_value()
    value_operand = view.get_function()
    value_c = view.get_value()
    value_d = view.get_value()
    model.init(value_a, value_b,value_c,value_d)
    if value_operand is '+': result = model.do_sum()
    if value_operand is '-': result = model.do_sub()
    if value_operand is '*': result = model.do_mult()
    if value_operand is '/': result = model.do_dev()
    view.view_data(result, 'result')