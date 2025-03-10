# Students service API

### Install dependencies
```sh
sudo apt install libcjson-dev
git clone https://github.com/civetweb/civetweb.git
cd civetweb
make
```

### Compile
If you have students_api.c and civetweb in the same folder then:
```sh
gcc students_api.c -I./civetweb/include -L./civetweb -I/usr/include/cjson -L/usr/lib/x86_64-linux-gnu/ -lsqlite3 -lcivetweb -lcjson -o students_api
```
### Try it
```sh
curl http://localhost:8080/api/v1/get_all_students
curl http://localhost:8080/api/v1/get_students_by_city?city=Villamakako
curl http://localhost:8080/api/v1/get_students_by_city?city=Villafronto
```
