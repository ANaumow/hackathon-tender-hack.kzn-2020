import pymysql


class Dao:

    def __init__(self) -> None:
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='12345',
                                          db='hack')

    def execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return [x[0] for x in cursor.fetchall()]

    def get_dictionary(self):
        answer_to_key = {}
        all_answers_id = self.execute("select `id` from answer")
        for answer_id in all_answers_id:
            keys = self.execute("select `text` from `key` where answer_id = " + str(answer_id) + "")
            answer_to_key[answer_id] = keys
        return answer_to_key
