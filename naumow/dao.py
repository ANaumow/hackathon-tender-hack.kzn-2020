import pymysql


class Dao:

    def __init__(self, debug=False) -> None:
        self.debug = debug
        self.connection = pymysql.connect(host='10.20.1.205',
                                          user='user',
                                          password='123',
                                          db='hack')

    def execute(self, sql):
        cursor = self.connection.cursor()
        if self.debug:
            print('"' + sql + '" is executing')
        cursor.execute(sql)
        self.connection.commit()
        if self.debug:
            print('"' + sql + '" is executed')
        return [x[0] for x in cursor.fetchall()]

    def get_dictionary(self):
        answer_to_key = {}
        all_answers_id = self.execute("select `id` from answer")
        for answer_id in all_answers_id:
            keys = self.execute("select `text` from `key` where answer_id = " + str(answer_id) + "")
            answer_to_key[answer_id] = keys
        return answer_to_key

    def get_answer(self, num):
        return self.execute("select `text` from answer where id = " + str(num))
