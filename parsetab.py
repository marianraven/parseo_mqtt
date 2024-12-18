
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AUTH CON CONECTAR DESCONECTAR DESUSCRIBIRSE DISPOSITIVO ENCRIPTADO FALSE KEY MENSAJE MQTT PUBLICAR SUSCRIBIRSE TOPIC TRUE VALORprograma : comandoscomandos : comando\n                | comando comandoscomando : conectar\n               | desconectar\n               | publicar\n               | suscribirse\n               | desuscribirse\n               | habilitar_encriptado\n               | habilitar_authhabilitar_encriptado : ENCRIPTADO A valor_booleanovalor_booleano : TRUE\n                      | FALSEhabilitar_auth : AUTH VALOR VALORconectar : CONECTAR MQTT DISPOSITIVOsuscribirse : SUSCRIBIRSE DISPOSITIVO A TOPICpublicar : PUBLICAR DISPOSITIVO MENSAJE A TOPIC CON KEY VALORdesconectar : DESCONECTAR MQTT DISPOSITIVOdesuscribirse : DESUSCRIBIRSE DISPOSITIVO A TOPIC'
    
_lr_action_items = {'CONECTAR':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[11,11,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'DESCONECTAR':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[12,12,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'PUBLICAR':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[13,13,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'SUSCRIBIRSE':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[14,14,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'DESUSCRIBIRSE':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[15,15,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'ENCRIPTADO':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[16,16,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'AUTH':([0,3,4,5,6,7,8,9,10,26,27,31,32,33,34,36,37,41,],[17,17,-4,-5,-6,-7,-8,-9,-10,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'$end':([1,2,3,4,5,6,7,8,9,10,18,26,27,31,32,33,34,36,37,41,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-10,-3,-15,-18,-11,-12,-13,-14,-16,-19,-17,]),'MQTT':([11,12,],[19,20,]),'DISPOSITIVO':([13,14,15,19,20,],[21,22,23,26,27,]),'A':([16,22,23,28,],[24,29,30,35,]),'VALOR':([17,25,40,],[25,34,41,]),'MENSAJE':([21,],[28,]),'TRUE':([24,],[32,]),'FALSE':([24,],[33,]),'TOPIC':([29,30,35,],[36,37,38,]),'CON':([38,],[39,]),'KEY':([39,],[40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'comandos':([0,3,],[2,18,]),'comando':([0,3,],[3,3,]),'conectar':([0,3,],[4,4,]),'desconectar':([0,3,],[5,5,]),'publicar':([0,3,],[6,6,]),'suscribirse':([0,3,],[7,7,]),'desuscribirse':([0,3,],[8,8,]),'habilitar_encriptado':([0,3,],[9,9,]),'habilitar_auth':([0,3,],[10,10,]),'valor_booleano':([24,],[31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> comandos','programa',1,'p_programa','mqtt_parser.py',21),
  ('comandos -> comando','comandos',1,'p_comandos','mqtt_parser.py',25),
  ('comandos -> comando comandos','comandos',2,'p_comandos','mqtt_parser.py',26),
  ('comando -> conectar','comando',1,'p_comando','mqtt_parser.py',30),
  ('comando -> desconectar','comando',1,'p_comando','mqtt_parser.py',31),
  ('comando -> publicar','comando',1,'p_comando','mqtt_parser.py',32),
  ('comando -> suscribirse','comando',1,'p_comando','mqtt_parser.py',33),
  ('comando -> desuscribirse','comando',1,'p_comando','mqtt_parser.py',34),
  ('comando -> habilitar_encriptado','comando',1,'p_comando','mqtt_parser.py',35),
  ('comando -> habilitar_auth','comando',1,'p_comando','mqtt_parser.py',36),
  ('habilitar_encriptado -> ENCRIPTADO A valor_booleano','habilitar_encriptado',3,'p_habilitar_encriptado','mqtt_parser.py',39),
  ('valor_booleano -> TRUE','valor_booleano',1,'p_valor_booleano','mqtt_parser.py',45),
  ('valor_booleano -> FALSE','valor_booleano',1,'p_valor_booleano','mqtt_parser.py',46),
  ('habilitar_auth -> AUTH VALOR VALOR','habilitar_auth',3,'p_habilitar_auth','mqtt_parser.py',50),
  ('conectar -> CONECTAR MQTT DISPOSITIVO','conectar',3,'p_conectar','mqtt_parser.py',68),
  ('suscribirse -> SUSCRIBIRSE DISPOSITIVO A TOPIC','suscribirse',4,'p_suscribirse','mqtt_parser.py',89),
  ('publicar -> PUBLICAR DISPOSITIVO MENSAJE A TOPIC CON KEY VALOR','publicar',8,'p_publicar','mqtt_parser.py',109),
  ('desconectar -> DESCONECTAR MQTT DISPOSITIVO','desconectar',3,'p_desconectar','mqtt_parser.py',142),
  ('desuscribirse -> DESUSCRIBIRSE DISPOSITIVO A TOPIC','desuscribirse',4,'p_desuscribirse','mqtt_parser.py',151),
]
