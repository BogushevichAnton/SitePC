--
-- ���� ������������ � ������� SQLiteStudio v3.4.3 � �� ��� 25 22:36:14 2023
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: SitePC_category
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
                                '�������',
                                'igrovye'
                            );

INSERT INTO SitePC_category (
                                id,
                                name,
                                slug
                            )
                            VALUES (
                                2,
                                '��� ����� � ����',
                                'dlya-ofisa-i-doma'
                            );

INSERT INTO SitePC_category (
                                id,
                                name,
                                slug
                            )
                            VALUES (
                                3,
                                '��������',
                                'noutbuki'
                            );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
