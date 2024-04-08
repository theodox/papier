import network

pwdb = "300spartans∅simonides".partition('∅')
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(f"{pwdb[-1]}", f"{pwdb[0]}!")

print ("wifi connection: {}".format(sta_if.isconnected()))


