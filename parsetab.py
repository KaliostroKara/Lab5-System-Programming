
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE LPAREN MINUS NUMBER PLUS POWER RPAREN TIMESexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression POWER expressionexpression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'LPAREN':([0,2,4,5,6,7,8,],[2,2,2,2,2,2,2,]),'NUMBER':([0,2,4,5,6,7,8,],[3,3,3,3,3,3,3,]),'$end':([1,3,10,11,12,13,14,15,],[0,-7,-1,-2,-3,-4,-5,-6,]),'PLUS':([1,3,9,10,11,12,13,14,15,],[4,-7,4,4,4,4,4,4,-6,]),'MINUS':([1,3,9,10,11,12,13,14,15,],[5,-7,5,5,5,5,5,5,-6,]),'TIMES':([1,3,9,10,11,12,13,14,15,],[6,-7,6,6,6,6,6,6,-6,]),'DIVIDE':([1,3,9,10,11,12,13,14,15,],[7,-7,7,7,7,7,7,7,-6,]),'POWER':([1,3,9,10,11,12,13,14,15,],[8,-7,8,8,8,8,8,8,-6,]),'RPAREN':([3,9,10,11,12,13,14,15,],[-7,15,-1,-2,-3,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,5,6,7,8,],[1,9,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_express_binop','expr_parser.py',10),
  ('expression -> expression MINUS expression','expression',3,'p_express_binop','expr_parser.py',11),
  ('expression -> expression TIMES expression','expression',3,'p_express_binop','expr_parser.py',12),
  ('expression -> expression DIVIDE expression','expression',3,'p_express_binop','expr_parser.py',13),
  ('expression -> expression POWER expression','expression',3,'p_express_binop','expr_parser.py',14),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_express_group','expr_parser.py',18),
  ('expression -> NUMBER','expression',1,'p_express_number','expr_parser.py',22),
]
