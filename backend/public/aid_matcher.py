from public.first_aid import FIRST_AID_GUIDE

def get_first_aid(text):
    text = text.lower()
    for keyword in FIRST_AID_GUIDE:
        if keyword in text:
            return FIRST_AID_GUIDE[keyword]
    return None
