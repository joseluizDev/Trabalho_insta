import json
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin


class credencial():
    jj = {
        "type": "service_account",
        "project_id": "instagram-criador",
        "private_key_id": "e8ba7116e9a8ce9275d06be909b76389fa7ee1aa",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQChO7E3amzwBAqb\nLx0ftEDT061kNlJcihj53EPSRPsQGeTgHKEDBtDwsZvcipjOS5f13RT1EeN3TQlj\ncYzZuIuKlJTRPaz9mFG3CZ6nCIhfHhywpwFLdw31Ierp0r8ZuKNeUUuzx5nJ5tDr\nWXOeCoy0AREvmqP11XoLWH56sgTstdZIT9j6E/BvGCTZS4sYKnf6AHSe7iubqDO0\n1jQqKR8KPoB/Aa48ZZkY6bryDAVdCwe6gjvEIRXYA4o+IgQkBX7IzfRumsrL/I/J\nw3Vo6dkYX6iyP87eHXD4sLmwO5AQ3EJT4Ke2wXZMmnbOAeYRJn64IMWTs4DL6kR5\nChjAHTQbAgMBAAECggEAQU8vHS3YW66fZzXB285Fdihns1CHsyFjNY6h0EIN2ntK\nqPcfx1yS9PRUmJRxihq3vqkjbJOm6nPDikr8DVMB/wvpbgpIEN8KtpRIdgtwResq\nHuo/DYT3m+R1xeoOa4pNbo6KlhOTeWOsG7D7srg+P0mxXvGKWbFzwrXBYczLTuBC\nhQ+iuu8L+pqsPTIyRD5K1anC+PvimW+N9WYEHCW29n4qJixYdeOh+fdyikGFIhp7\npHo8xotWdIXuTU8OuEbazFQDOEb3Z1LnAggZOiNYZJsONt0q+akbZApf4QsIZWql\nlcJA29VHiX334t3SbxWgvHAaXIgIPpeA9VMmYyGQVQKBgQDOKz9Rpz4wQ9aLVnV7\nqrq8m4fllRROVPaSSIYJK0lB8VwMTVdZRzOEvkVxuwAu2qWmova7he29a+2yUcyW\nTf7vRfPKvYIiaiMIfNDt4gPlyKX7orhF8MeDqCKeK2Ky5BQG1oGsepuV3fA+CS9C\nzeZK3HUgfC1z2gD5LisrwDZHLQKBgQDINAilqAl726wTFl89IN8llllYrQs1iOeD\nruHWS6mEU8LwDSGU4I7HTUlKT/qTxAwrjAx136BIXzyMlNSRbn9h+lExCsiSaWDY\n3Flv4jxMMhTxg/hxJx5ShXTgTJy2p5YZ0g1AgMiu/0/YLnvwr6NH+oCOF0iYUNlG\nnfZswht1ZwKBgQCDnmpzB3EVQQnDtLOV+r3yUNymPdFT3Lv5UaF4UxEWry6TkACW\nt3T1Zr9QxxBr2Rxt0JXxy6OmDTQXZk9VGYAKYz8rjGZ68AVjksOTSnowhTMp/Yzk\n4b2NmJZZIduF10PNxb3NTgzr1V9dS2HHpUlDO5Du5zfhQSjj64yWBsTgFQKBgBfW\n+mCfjeGN2wO62kRxMaFMMf95O6h4UPlBTesyv1DemIv1RFZyFw5siZmrxG7sHXbi\nCmnO40s66/7hih53RfvoztpEKnYkzj+EnbHRAtUf8ZaA3Ii828N/2NcMyGyHsDwK\n40EXFM6h4GQhxOh4Qb1EeyJwa1iX6Aecr8drpdFpAoGADHdi+Z7ASe6iGW201Vvb\nRZGPnNXagq8z1L0GSiPSF43dsXv6e4tA7ZE2hzwBvg6vVgQ7QgPeN4YLswRfUGD/\nXCHydZgUvSM/bYkv/MYlrrf24pT0/Gz5qeLJ5u23I19BFcACVqe5bIP/9z9whV5h\nH1Z+K5CEayna2iq2Dq+gJHE=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-fdrhi@instagram-criador.iam.gserviceaccount.com",
        "client_id": "104210109283213820346",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fdrhi%40instagram-criador.iam.gserviceaccount.com"
    }


cred = credentials.Certificate(credencial.jj)
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://instagram-criador-default-rtdb.firebaseio.com/"
})
ref = db.reference()


def setvalorFirebase(value):
    ref.child("contas").push().set(value)


def getvalueFirebase():
    return ref.child("very").get()
