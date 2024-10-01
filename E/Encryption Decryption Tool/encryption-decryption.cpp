#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Substitution cipher encryption algorithm
string encrypt(string message, string key) {
    string result = "";
    for (int i = 0; i < message.length(); i++) {
        if (isalpha(message[i])) {
            int index = tolower(message[i]) - 'a';
            result += key[index];
        } else {
            result += message[i];
        }
    }
    return result;
}

// Substitution cipher decryption algorithm
string decrypt(string message, string key) {
    string result = "";
    for (int i = 0; i < message.length(); i++) {
        if (isalpha(message[i])) {
            int index = key.find(tolower(message[i]));
            result += 'a' + index;
        } else {
            result += message[i];
        }
    }
    return result;
}

int main() {
    string key = "qwertyuiopasdfghjklzxcvbnm";
    string message, encrypted_message, decrypted_message;

    // Get user input message
    cout << "Enter a message to encrypt: ";
    getline(cin, message);

    // Encrypt message
    encrypted_message = encrypt(message, key);
    cout << "Encrypted message: " << encrypted_message << endl;

    // Decrypt message
    char answer;
    cout << "Do you want to decrypt the message? (y/n): ";
    cin >> answer;
    if (answer == 'y' || answer == 'Y') {
        cout << "Enter the encrypted message: ";
        cin.ignore();
        getline(cin, encrypted_message);
        decrypted_message = decrypt(encrypted_message, key);
        cout << "Decrypted message: " << decrypted_message << endl;
    }

    return 0;
}
