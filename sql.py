import sqlite3
class SQL:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_flag(self, site_id):
        """Получаем флаг в очереди"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user_info` WHERE `site_id` = ?", (site_id,)).fetchall()

    def get_pos(self, site_id):
        """Получаем место в очереди"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user_info` WHERE `site_id` = ?", (site_id,)).fetchall()
