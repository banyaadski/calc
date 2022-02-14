import model_com as model
import model_rational as model_r
import view_complex as view_c
import viev_rational as view_r
# import logger

def button_click():
    x = input('used complex? Y/N == ')
    if x == 'N':
        value_a = view_r.get_value()
        value_b = view_r.get_value()
        value_operand = view_r.get_function()
        model_r.init(value_a,value_b)
        if value_operand is "+": result = model_r.do_it_sum()
        if value_operand is "-": result = model_r.do_it_subt()
        if value_operand is "/": result = model_r.do_it_div()
        if value_operand is "*": result = model_r.do_it_mult()
        view_r.view_data(result, 'result')
    else:
        value_a = view_c.get_value()
        value_b = view_c.get_value()
        value_operand = view_c.get_function()
        value_c = view_c.get_value()
        value_d = view_c.get_value()
        model.init(value_a, value_b,value_c,value_d)
        if value_operand is '+': result = model.do_sum()
        if value_operand is '-': result = model.do_sub()
        if value_operand is '*': result = model.do_mult()
        if value_operand is '/': result = model.do_dev()
        view_c.view_data(result, 'result')