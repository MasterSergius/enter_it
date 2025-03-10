#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>
#include "civetweb.h"
#include "cJSON.h"


static int callback_json(void *data, int argc, char **argv, char **azColName) {
    cJSON *array = (cJSON *)data;
    cJSON *obj = cJSON_CreateObject();

    for (int i = 0; i < argc; i++) {
        cJSON_AddStringToObject(obj, azColName[i], argv[i] ? argv[i] : "NULL");
    }

    cJSON_AddItemToArray(array, obj);
    return 0;
}


static int get_all_students_json_handler(struct mg_connection *conn, void *userdata) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;

    rc = sqlite3_open("students.db", &db);
    if (rc) {
        mg_printf(conn, "HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/json\r\n\r\n{\"error\":\"Database error\"}");
        return 500;
    }

    sql = "SELECT * FROM Students;";
    cJSON *json_array = cJSON_CreateArray();

    rc = sqlite3_exec(db, sql, callback_json, json_array, &zErrMsg);
    if (rc != SQLITE_OK) {
        mg_printf(conn, "HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/json\r\n\r\n{\"error\":\"%s\"}", zErrMsg);
        sqlite3_free(zErrMsg);
        cJSON_Delete(json_array);
        sqlite3_close(db);
        return 500;
    }

    char *json_string = cJSON_Print(json_array);
    cJSON_Delete(json_array);

    mg_printf(conn, "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n%s", json_string);

    free(json_string);
    sqlite3_close(db);
    return 200; // HTTP status OK
}


static int get_students_by_city_handler(struct mg_connection *conn, void *userdata) {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;
    char city[256]; // Buffer to store the city param
    const char *query_string = mg_get_request_info(conn)->query_string; // Get the query string.

    if (query_string == NULL || mg_get_var(query_string, strlen(query_string), "city", city, sizeof(city)) <= 0) {
        mg_printf(conn, "HTTP/1.1 400 Bad Request\r\nContent-Type: application/json\r\n\r\n{\"error\":\"City parameter missing\"}");
        return 400;
    }

    rc = sqlite3_open("students.db", &db);
    if (rc) {
        mg_printf(conn, "HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/json\r\n\r\n{\"error\":\"Database error\"}");
        return 500;
    }

    sql = sqlite3_mprintf("SELECT * FROM Students WHERE city = '%q';", city); // Use sqlite3_mprintf to avoid SQL injection.
    cJSON *json_array = cJSON_CreateArray();

    rc = sqlite3_exec(db, sql, callback_json, json_array, &zErrMsg);
    if (rc != SQLITE_OK) {
        mg_printf(conn, "HTTP/1.1 500 Internal Server Error\r\nContent-Type: application/json\r\n\r\n{\"error\":\"%s\"}", zErrMsg);
        sqlite3_free(zErrMsg);
        cJSON_Delete(json_array);
        sqlite3_free(sql);
        sqlite3_close(db);
        return 500;
    }

    char *json_string = cJSON_Print(json_array);
    cJSON_Delete(json_array);
    sqlite3_free(sql);

    mg_printf(conn, "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n%s", json_string);

    free(json_string);
    sqlite3_close(db);
    return 200; // HTTP status OK
}


int main() {
    struct mg_callbacks callbacks;
    struct mg_context *ctx;
    const char *options[] = {"listening_ports", "8080", NULL};

    memset(&callbacks, 0, sizeof(callbacks));
    ctx = mg_start(&callbacks, NULL, options);

    // register API endpoints
    mg_set_request_handler(ctx, "/api/v1/get_all_students", get_all_students_json_handler, NULL);
    mg_set_request_handler(ctx, "/api/v1/get_students_by_city", get_students_by_city_handler, NULL);

    printf("Server started on port 8080\n");
    getchar();

    mg_stop(ctx);
    return 0;
}
