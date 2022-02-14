import model_com as model
import model_rational as model_r
import view_complex as view_c
import viev_rational as view_r
import logging as lg

def menu():
    x = -1
    while x != 0:
        x = view_r.cho()
        if x == 1 or 2:
            button_click(x)

def button_click():
    x = ''
    while x != 'e':
        x = view_c.cho()
        if x == 'r':
            value_a = view_r.get_value('rational_a')
            value_operand = view_r.get_function()
            value_b = view_r.get_value('rational_b')
            model_r.init(value_a,value_b)
            if value_operand is "+": result = model_r.do_it_sum()
            if value_operand is "-": result = model_r.do_it_subt()
            if value_operand is "/": result = model_r.do_it_div()
            if value_operand is "*": result = model_r.do_it_mult()
            view_r.view_data(result, 'result')
            lg.log_create_rational(value_a,value_b, result, value_operand)
        if x == 'c':
            value_a = view_c.get_value('complex_a')
            value_b = view_c.get_value('complex_b')
            value_operand = view_c.get_function()
            value_c = view_c.get_value('complex_c')
            value_d = view_c.get_value('complex_d')
            model.init(value_a, value_b,value_c,value_d)
            if value_operand is '+': result = model.do_sum()
            if value_operand is '-': result = model.do_sub()
            if value_operand is '*': result = model.do_mult()
            if value_operand is '/': result = model.do_dev()
            view_c.view_data(result, 'result')
            lg.log_create_complex(value_a,value_b,value_c,value_d, result, value_operand)
        
