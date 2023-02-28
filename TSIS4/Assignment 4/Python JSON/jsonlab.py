import json
with open("json.json") as file:
    x=json.load(file)
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for s in x["imdata"]:
    #print(s["l1PhysIf"]["attributes"]["dn"])
    #print(s["l1PhysIf"]["attributes"]["speed"])
    #print(s["l1PhysIf"]["attributes"]["mtu"])
    #print()
    print(s["l1PhysIf"]["attributes"]["dn"] + " "*30,
          s["l1PhysIf"]["attributes"]["speed"],
          s["l1PhysIf"]["attributes"]["mtu"])