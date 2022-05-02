# -*- coding: utf8 -*-
import sqlite3

class SQL:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_flag(self, id):
        """Получаем флаг в очереди"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user_info` WHERE `id` = ?", (id,)).fetchall()[0][3]

    def get_pos(self, id):
        """Получаем место в очереди"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user_info` WHERE `id` = ?", (id,)).fetchall()[0][1]

    def get_fio(self, id):
        """Получаем место в очереди"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `user_info` WHERE `id` = ?", (id,)).fetchall()[0][0]