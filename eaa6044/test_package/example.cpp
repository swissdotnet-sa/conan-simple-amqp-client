
#include <iostream>
#include <SimpleAmqpClient/SimpleAmqpClient.h>

int main() {
    try
    {
        AmqpClient::Channel::ptr_t connection = AmqpClient::Channel::Create("localhost");
    }
    catch (const std::runtime_error& e)
    {
        // A runtime_error will be thrown when creating the channel if it cannot connect.
    }
    return 0;
}
