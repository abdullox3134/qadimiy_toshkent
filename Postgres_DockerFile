FROM postgres:alpine

# Ma'lumotlar bazasi nomi, foydalanuvchi nomi va parolini o'rnating
ENV POSTGRES_DB=toshkent
ENV POSTGRES_USER=toshkent_user
ENV POSTGRES_PASSWORD=toshkent_password

# Ma'lumotlar bazasi boshlang'ich holatga keltiruvchi SQL skriptini ko'chiring
COPY init.sql /docker-entrypoint-initdb.d/

# Portni oching
EXPOSE 5432
