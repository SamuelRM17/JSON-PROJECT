
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMA CORCHETE_DER CORCHETE_IZQ DATE DOSPUNTOS EMAIL ID LLAVE_DER LLAVE_IZQ MOVIE_ID NAME NUMBERLONG OID SDATE TEXTjson : CORCHETE_IZQ elementos CORCHETE_DERelementos : LLAVE_IZQ p_ID COMA p_name COMA p_email COMA p_movie_id COMA p_text COMA p_date LLAVE_DER COMA elementoselementos : LLAVE_IZQ p_ID COMA p_name COMA p_email COMA p_movie_id COMA p_text COMA p_date LLAVE_DERp_ID : ID DOSPUNTOS LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DERp_name : NAME DOSPUNTOS CADENAp_email : EMAIL DOSPUNTOS CADENAp_movie_id : MOVIE_ID DOSPUNTOS LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DERp_text : TEXT DOSPUNTOS CADENAp_date : DATE DOSPUNTOS LLAVE_IZQ SDATE DOSPUNTOS LLAVE_IZQ NUMBERLONG DOSPUNTOS CADENA LLAVE_DER LLAVE_DER'
    
_lr_action_items = {'CORCHETE_IZQ':([0,],[2,]),'$end':([1,5,],[0,-1,]),'LLAVE_IZQ':([2,9,28,40,42,47,],[4,12,31,43,4,48,]),'CORCHETE_DER':([3,39,45,],[5,-3,-2,]),'ID':([4,],[7,]),'COMA':([6,10,16,18,23,25,26,29,37,39,44,],[8,13,20,-5,27,-6,-4,32,-8,42,-7,]),'DOSPUNTOS':([7,11,15,17,24,30,34,36,46,49,],[9,14,19,21,28,33,38,40,47,50,]),'NAME':([8,],[11,]),'OID':([12,31,],[15,34,]),'EMAIL':([13,],[17,]),'CADENA':([14,19,21,33,38,50,],[18,22,25,37,41,51,]),'MOVIE_ID':([20,],[24,]),'LLAVE_DER':([22,35,41,51,52,53,],[26,39,44,52,53,-9,]),'TEXT':([27,],[30,]),'DATE':([32,],[36,]),'SDATE':([43,],[46,]),'NUMBERLONG':([48,],[49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'json':([0,],[1,]),'elementos':([2,42,],[3,45,]),'p_ID':([4,],[6,]),'p_name':([8,],[10,]),'p_email':([13,],[16,]),'p_movie_id':([20,],[23,]),'p_text':([27,],[29,]),'p_date':([32,],[35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> json","S'",1,None,None,None),
  ('json -> CORCHETE_IZQ elementos CORCHETE_DER','json',3,'p_json','yacc.py',9),
  ('elementos -> LLAVE_IZQ p_ID COMA p_name COMA p_email COMA p_movie_id COMA p_text COMA p_date LLAVE_DER COMA elementos','elementos',15,'p_elementos_1','yacc.py',13),
  ('elementos -> LLAVE_IZQ p_ID COMA p_name COMA p_email COMA p_movie_id COMA p_text COMA p_date LLAVE_DER','elementos',13,'p_elementos_2','yacc.py',17),
  ('p_ID -> ID DOSPUNTOS LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DER','p_ID',7,'p_ID','yacc.py',21),
  ('p_name -> NAME DOSPUNTOS CADENA','p_name',3,'p_name','yacc.py',25),
  ('p_email -> EMAIL DOSPUNTOS CADENA','p_email',3,'p_email','yacc.py',29),
  ('p_movie_id -> MOVIE_ID DOSPUNTOS LLAVE_IZQ OID DOSPUNTOS CADENA LLAVE_DER','p_movie_id',7,'p_movie_id','yacc.py',33),
  ('p_text -> TEXT DOSPUNTOS CADENA','p_text',3,'p_text','yacc.py',37),
  ('p_date -> DATE DOSPUNTOS LLAVE_IZQ SDATE DOSPUNTOS LLAVE_IZQ NUMBERLONG DOSPUNTOS CADENA LLAVE_DER LLAVE_DER','p_date',11,'p_date','yacc.py',41),
]
