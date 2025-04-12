#include<stdio.h>
#include<string>

using namespace std;


class Unit {
private:
    string name;
    int hp;
    int speed;
    int damage;

public:
    Unit(string unit_name, int unit_hp, int unit_speed, int unit_damage) {
        name=unit_name;
        hp=unit_hp;
        speed=unit_speed;
        damage=unit_damage;
    }

    void say_name() {
        printf("My name is %s\n", name.c_str());
    }

    void show_special() {
        printf("Unit special\n");
    }
};


class Worker: public Unit {
public:
    Worker(string name, int hp, int speed, int damage): Unit(name, hp, speed, damage) {
    }

    void build(string building) {
        printf("Going to build %s\n", building.c_str());
    }

    void show_special() {
        printf("Worker special\n");
    }
};


class Archer: public Unit {
public:
    Archer(string name, int hp, int speed, int damage): Unit(name, hp, speed, damage) {
    }

    void shoot() {
        printf("shooting");
    }

    void show_special() {
        printf("Archer special\n");
    }
};

int main() {
    Unit unit("Joe", 50, 10, 10);
    unit.say_name();
    unit.show_special();

    Worker worker("John", 100, 10, 10);
    worker.say_name();
    worker.show_special();

    Archer archer("Jane", 100, 10, 10);
    archer.say_name();
    archer.show_special();
    return 0;
}
