import json

def getDatabase(dbname):
    try:
        file=open("database/"+dbname+".json", "r")
        data=json.loads(file.read())
        file.close()
        return data
    except Exception as e:
        print("error", e)
        file.close()
    finally:
        file.close()
    

def saveDatabase(data, dbname):
    try:
        file=open("database/"+dbname+".json", "w")
        json.dump(data, file)
        print("data saved")
    except Exception as e:
        print(e)
        file.close()
    finally:
        file.close()

