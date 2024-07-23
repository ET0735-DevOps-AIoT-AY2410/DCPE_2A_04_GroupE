import time
from website import hal_rfid_reader as rfid

def read():
    import time
    from website import hal_rfid_reader as rfid
    rfid_reader = rfid.SimpleMFRC522()
    print("Reading RFID card...")
    card_id, text = rfid_reader.read()
    print(f"Card ID: {card_id}")

    authorized_ids = [830894050716]


    if card_id not in authorized_ids:
        print("RFID authorization failed. Engine start aborted.")
        return False
    else:
        return True
    