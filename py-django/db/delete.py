from db.dao import Dao

dao = Dao()

print(dao.execute("select * from hack.`answer`;"))