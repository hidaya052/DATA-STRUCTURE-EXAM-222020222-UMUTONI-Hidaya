Header and Namespace

#include <iostream>
Includes the standard input-output stream library for using cin, cout.

#include <vector>
Includes the vector container to store ticket objects dynamically.

#include <memory>
Includes the memory library for smart pointers (unique_ptr) to manage memory safely.

using namespace std;
So you don’t have to prefix std:: before standard library types like vector, cout, etc.

Base Class: Ticket
class Ticket {
protected:
    string movie;
    string seat;
    double price;
Defines a base class Ticket with protected attributes: movie name, seat number, and price.

public:
    Ticket(string m, string s, double p) : movie(m), seat(s), price(p) {}
Constructor to initialize the movie, seat, and price.

    virtual void display() const {
        cout << movie << " - Seat " << seat << " - $" << price;
    }
A virtual function to display ticket details. Allows derived classes to override it.

    virtual ~Ticket() = default;
Virtual destructor to ensure proper cleanup of derived class objects.

Derived Class: NormalTicket
class NormalTicket : public Ticket {
public:
    NormalTicket(string m, string s, double p) : Ticket(m, s, p) {}
Inherits from Ticket. The constructor calls the base constructor.

    void display() const override {
        Ticket::display();
        cout << " (Normal)\n";
    }
Overrides display() to add " (Normal)" after the base class display.

Derived Class: VIPTicket
class VIPTicket : public Ticket {
public:
    VIPTicket(string m, string s, double p) : Ticket(m, s, p) {}
    void display() const override {
        Ticket::display();
        cout << " (VIP)\n";
    }
};
Same as NormalTicket, but tags with " (VIP)".

Derived Class: StudentTicket
class StudentTicket : public Ticket {
public:
    StudentTicket(string m, string s, double p) : Ticket(m, s, p) {}
    void display() const override {
        Ticket::display();
        cout << " (Student)\n";
    }
};
Tags with " (Student)".

Derived Class: StudentVIPTicket
class StudentVIPTicket : public StudentTicket {
public:
    StudentVIPTicket(string m, string s, double p) : StudentTicket(m, s, p) {}
Inherits from StudentTicket.

    void display() const override {
        Ticket::display();
        cout << " (Student VIP)\n";
    }
};
Tags with " (Student VIP)". Even though it inherits from StudentTicket, it overrides display() to identify as a Student VIP.

CinemaSystem Class
class CinemaSystem {
    vector<unique_ptr<Ticket>> tickets;
Contains a vector of unique_ptrs to Ticket objects, allowing polymorphic storage and automatic memory management.

public:
    void addTicket(unique_ptr<Ticket> ticket) {
        tickets.push_back(move(ticket));
    }
Adds a ticket to the vector using move to transfer ownership.

    void showAllTickets() const {
        cout << "\n=== TICKET LIST ===\n";
        for (const auto& t : tickets) {
            t->display();
        }
    }
};
Loops through all tickets and calls their display() method to show their info.

Main Function
int main() {
    CinemaSystem cinema;
    string movie, seat;
    double price;
    int choice;
    char more;
Declares variables and an instance of CinemaSystem.

    do {
        cout << "\nEnter movie name: ";
        cin >> movie;
        
        cout << "Enter seat number: ";
        cin >> seat;
        
        cout << "Enter price: $";
        cin >> price;
Gets input for movie, seat, and price.

        cout << "\nSelect ticket type:\n"
             << "1. Normal\n2. VIP\n3. Student\n4. Student VIP\n"
             << "Your choice: ";
        cin >> choice;
Prompts the user to choose a ticket type.

        switch(choice) {
            case 1:
                cinema.addTicket(make_unique<NormalTicket>(movie, seat, price));
                break;
            case 2:
                cinema.addTicket(make_unique<VIPTicket>(movie, seat, price));
                break;
            case 3:
                cinema.addTicket(make_unique<StudentTicket>(movie, seat, price));
                break;
            case 4:
                cinema.addTicket(make_unique<StudentVIPTicket>(movie, seat, price));
                break;
            default:
                cout << "Invalid choice, creating Normal ticket\n";
                cinema.addTicket(make_unique<NormalTicket>(movie, seat, price));
        }
Depending on the user’s choice, creates a corresponding ticket using make_unique and adds it to the system.

        cout << "\nAdd another ticket? (y/n): ";
        cin >> more;
    } while (more == 'y' || more == 'Y');
Loops to allow entering multiple tickets.

    cinema.showAllTickets();
    
    return 0;
}
After ticket entry is done, displays all tickets and ends the program.

In Summary:
OOP Concepts used: Inheritance, Polymorphism (via virtual functions), and Smart Pointers.

Functionality: A small ticket booking system for a cinema that handles different ticket types and displays them.

Safety: unique_ptr ensures no memory leaks, and virtual ~Ticket() ensures proper destruction of derived objects.
