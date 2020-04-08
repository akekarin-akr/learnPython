status = 0
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == 'start':
        if status == 0:
            print("Car started... Ready to go!")
            status = 1
        else:
            print("Hey! car has been started")
    elif command == 'stop':
        if status == 1:
            print("Car stopped.")
            status = 0
        else:
            print("Hey The car has stopped")
    elif command == 'quit':
        break
    else:
        print("I don't understand that!")



