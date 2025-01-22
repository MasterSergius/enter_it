/*
struct Student {
   char name[50];
   int year;
   int marks[5];
}

Print names and age
*/
#include <stdio.h>
#include <string.h>


typedef struct {
   char name[50];
   int year;
   int marks[5];
} Student;


const int TOTAL_STUDENTS = 5;
const int CURRENT_YEAR = 2025;


void setup_students_info(Student students[]) {
    for (int num_student=0; num_student<TOTAL_STUDENTS; num_student++) {

        sprintf(students[num_student].name, "Student %d", num_student+1);

        if (num_student % 2 == 0) {
            students[num_student].year = 2015;
        } else {
            students[num_student].year = 2014;
        };

        for (int i=0; i<5; i++) {
            students[num_student].marks[i] = (num_student + i) % 5 + 1;
        }
    }
}


void print_students_age(Student students[]) {
    for (int num_student=0; num_student<TOTAL_STUDENTS; num_student++) {
        printf("Name: %s\n", students[num_student].name);
        printf("Age: %d\n", CURRENT_YEAR - students[num_student].year);
        printf("\n");
    }
}


int main() {
    Student students[TOTAL_STUDENTS];
    setup_students_info(students);
    print_students_age(students);
    return 0;
}
