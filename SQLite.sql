CREATE TABLE [homework](
    [id] INTEGER,
    [subject] VARCHAR(65)
)

INSERT INTO [homework]
VALUES
    (1, "DTS"),
    (2, "DTG"),
    (3, "Chemistry"),
    (4, "Chinese"),
    (5, "English")


CREATE TABLE [student](
    [id] INTEGER,
    [name] VARCHAR(65),
    [homework_id] INTEGER
)

INSERT INTO [student]
VALUES
    (1, "Vu Hoang", 1),
    (2, "Van Vu Hoang", 3),
    (3, "Vu Van Hoang", 5)
