import pywhatkit
from conf import id_group_whatsapp, number_whatsapp

##pywhatkit.sendwhatmsg_to_group(id_group_whatsapp, "Testando Mensagem Python by GregMaster", 0, 0)
#pywhatkit.sendwhatmsg_to_group(group_id=id_group_whatsapp, message="Testando Mensagem Python by GregMaster", time_hour=19, time_min=52, wait_time=30)
pywhatkit.sendwhatmsg_to_group_instantly(group_id=id_group_whatsapp, message="Testando Mensagem Python by GregMaster", wait_time=30, tab_close=True ,close_time=60)