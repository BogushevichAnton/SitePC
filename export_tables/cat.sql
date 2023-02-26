--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.3 в Сб фев 25 22:36:14 2023
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: SitePC_category
CREATE TABLE IF NOT EXISTS SitePC_category (
    id   INTEGER       NOT NULL
                       PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (100) NOT NULL,
    slug VARCHAR (255) NOT NULL
                       UNIQUE
);

INSERT INTO SitePC_category (
                                id,
                                name,
                                slug
                            )
                            VALUES (
                                1,
                                'Игровые',
                                'igrovye'
                            );

INSERT INTO SitePC_category (
                                id,
                                name,
                                slug
                            )
                            VALUES (
                                2,
                                'Для офиса и дома',
                                'dlya-ofisa-i-doma'
                            );

INSERT INTO SitePC_category (
                                id,
                                name,
                                slug
                            )
                            VALUES (
                                3,
                                'Ноутбуки',
                                'noutbuki'
                            );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
