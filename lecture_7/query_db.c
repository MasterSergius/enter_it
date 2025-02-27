#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>

// Callback function for SELECT queries
static int callback(void *data, int argc, char **argv, char **azColName) {
    int i;
    for (i = 0; i < argc; i++) {
        //printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
        printf("%s,", argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main() {
    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    char *sql;
    const char *data = "Callback function called"; // Data for callback

    rc = sqlite3_open("students.db", &db);
    if (rc) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        return 1;
    }

    // SELECT query for students younger than 18
    // Structured Query Language - SQL
    // sql = "SELECT * FROM Students WHERE " \
    //      "(julianday('now') - julianday(dob)) / 365.25 < 18;";

    sql = "SELECT * FROM Students WHERE grp='I-10' ORDER BY dob DESC LIMIT 3;";
    rc = sqlite3_exec(db, sql, callback, (void *)data, &zErrMsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Select error: %s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    }

    sqlite3_close(db);
    return 0;
}
