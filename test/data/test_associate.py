# create table associate(
#     salesforceId varchar(10) primary key not null,
#     firstname varchar(20) not null,
#     lastname varchar(20) not null,
#     email varchar(40) UNIQUE,
#     pswrd varchar(40)
# );
from src.model.associate import Associate
associates = [
    Associate("ex0001@example.com", "EX-0001", "ExFirst", "ExLast", ""),
    Associate("ex0002@example.com", "EX-0002", "ExFirst", "ExLast", ""),
    Associate("ex0003@example.com", "EX-0003", "ExFirst", "ExLast", ""),
    Associate("ex0004@example.com", "EX-0004", "ExFirst", "ExLast", ""),
    Associate("ex0005@example.com", "EX-0005", "ExFirst", "ExLast", ""),
    Associate("ex0006@example.com", "EX-0006", "ExFirst", "ExLast", ""),
    Associate("ex0007@example.com", "EX-0007", "ExFirst", "ExLast", ""),
    Associate("ex0008@example.com", "EX-0008", "ExFirst", "ExLast", ""),
    Associate("ex0009@example.com", "EX-0009", "ExFirst", "ExLast", ""),
]
