import pandas as pd
from firebase_admin import db
def fire(col, val):
    ref = db.reference('/rfid/')
    dat = pd.DataFrame(ref.get()).transpose()
    return dat[dat[col]== val].reset_index(drop=True)
# chipid | readerid | timestamp