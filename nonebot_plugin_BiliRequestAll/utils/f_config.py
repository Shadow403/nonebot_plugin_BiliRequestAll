import json

def func_switch_status(x):
    if x in ["on","开","开启"]:
        return "on"
    elif x in ["off","关","关闭"]:
        return "off"
    else:
        return "off"
    
def func_load_switchdata(fp, _gid):
    with open(fp, "r", encoding="UTF-8") as f:
        _GSD = json.load(f)
        if _gid in _GSD["data"]:
            return _GSD["data"][_gid]
        else:
            return None
