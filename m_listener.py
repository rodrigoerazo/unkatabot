import telebot
from telebot import types
from m_token import bot

from errores import error

reg_arch = "./datos/registro.txt"

def listener(messages):
	#Guarda mensajes--------------------------------------------------------------------------------------------------------------------------
	try:
		for m in messages:
			cid = m.chat.id
			if cid > 0:
				mensaje = str(m.chat.first_name) + "(" + str(cid) + ")" + str(m.text)
			else:
				uid = m.from_user.id
				mensaje = str(m.chat.first_name) + "-" + str(m.from_user.first_name)
				mensaje += "(" + str(cid) + "*" + str(uid) + ")" + str(m.text)
			with open(reg_arch,"a") as arch:
				arch.write(mensaje + "\n")	
			print(mensaje)					
	except:
		try:
			error(sys.exc_info()[0],"listener")
		except:
			error(None, "listener")