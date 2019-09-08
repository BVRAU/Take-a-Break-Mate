import webbrowser


def game_menu():
    # Take a Break, Mate: Menu Code

    print("Welcome to Take a Break, Mate. This game will test your knowledge on safe driving practices,"
          " and your knowledge of rest areas.")
    location = input('Enter your location: ')
    print('Your location is ' + location)
    age = int(input('Enter your age: '))

    loop = True

    while loop:  # While loop which will keep going until loop = False
        print_menu()  # Displays menu
        choice = input("Enter your choice [1-4]: ")

        if choice == '1':
            print("The Game will start")
            if age <= 17:
                print('You are driving from Mount Gambier to Adelaide.\n '
                      'Along the way, you should take rest breaks when you become tired. '
                      'As a first year probationary driver, you are at a higher risk of\n '
                      'suffering a fatal crash in your first year of unsupervised driving.\n '
                      'To reduce the likelihood of an accident, rest breaks should be taken '
                      'frequently to make sure you are alert and not fatigued.\n')
            elif age >= 18 <= 25:
                print("You are driving from Mount Gambier to Adelaide."
                      "Along the way, you should take rest breaks when you become tired. "
                      "As a younger driver, you are at a higher risk of "
                      "suffering a fatal crash. "
                      "To reduce the likelihood of an accident, rest breaks should be taken "
                      "frequently to make sure you are alert and not fatigued.\n")

            print('Rest breaks are an important part of safe driving, just like '
                  'looking both ways at an intersection and stopping at traffic lights.\n '
                  'Within South Australia, many rest areas are maintained to ensure safety'
                  'and good driving habits in all road users.\n '
                  'Rest areas are typically found on the side of highways and major roads '
                  'which provide arterial transport.\n')

            print('Using this knowledge, you are now going to undertake scenarios which'
                  'test your perception of fatigue, and raise\n'
                  'awareness of rest areas in your local areas.')

            print('You are now ready to begin driving. Enter "Yes" to begin.\n'
                  'If you are not ready, enter "No" and you will be returned to the menu. ')
            start = input('')
            if start == 'Yes':
                main_game()
            else:
                game_menu()
        elif choice == '2':
            print("High scores not yet functional. Try again later!")
        elif choice == '3':
            print("You will now be taken to the MAC Website")
            webbrowser.open('https://www.mac.sa.gov.au/')
        elif choice == '4':
            print("The game will now end")
            break
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-4 we print an error message
        print("Invalid Option Selected. Please start again.")


def print_menu():  # Main Menu
    print(30 * "-", "MENU", 30 * "-")
    print("1. Start Game")
    print("2. High Scores")
    print("3. MAC Website")
    print("4. Exit")
    print(67 * "-")


def main_game():
    score = int(1)
    print('You about 30 kilometres from Penola. As you are driving, you begin to become drowsy.\n'
          'There is a rest area just past the turnoff to Kalangadoo, and there are areas to pull over in Penola.')
    cp = input('Do you wish to\n A: Pull over past the Kalangadoo turnoff\n B: Pull over in Penola')
    if cp == 'A':
        print('Good choice, you are driving cautiously.\n'
              ' After a 10 minute rest break, you continue driving, \n'
              'alert and refreshed.')
    else:
        print('Neither a good choice or a bad choice. \n'
              'Although it is best to rest when you are tired, you have only started driving \n'
              'so not pulling over is okay as well. Make sure you judge the risks and weight up \n'
              'the best option for you and other road users when choosing not to take a rest break.')
    print('Practice round over, good luck!\n'
          'Round 1')
    print("You are driving through Coonawarra, and you begin getting hungry.\n"
          "As your hunger increases, you become more drowsy and less focused on your driving.\n"
          "You have packed lunch with your for your trip. You can pull over at the Bool Lagoon\n"
          "Rest Area, or you can stop and have lunch in Naracoorte.\n")
    c1 = input('Do you wish to\n'
               'A: Pull over at the Bool Lagoon Rest Area\n'
               'B: Keep driving until you get to Naracoorte\n')
    if c1 == 'A':
        score = score + 1
        print('Good choice. By stopping for lunch, you have increased your level of concentration,\n'
              ' and you have reduced the risk of a crash(and your hunger!). You have earned 1 point.')
        print('Your current score is ' + str(score))
    else:
        score = score - 1
        print('Bad choice. By stopping for lunch, you have not decreased your hunger,\n'
              'and you have made yourself a risk to other road users. This time, you made it to Naracoorte luckily.')
        print('Your current score is ' + str(score))
    print('Round 2. Good luck!')
    print('You are now driving from Naracoorte to Keith. \n'
          'You are approaching Padthaway, and you are again feeling drowsy.\n'
          'Dusk is beginning to take hold, and drivers are putting on their headlights, dazing you every few seconds.\n'
          'You are finding it hard to keep your eyes open, and are veering off the road.')
    c2 = input('Do you wish to\n'
               'A: Take a power break at the Padthaway Rest Area\n'
               'B: Keep driving and stop for dinner at Keith')
    if c2 == 'A':
        score = score + 1
        print('Good choice! As your fatigue increased, you were finding it hard to focus on driving\n'
              'and keeping your vehicle on the road. By choosing to stop, you ensured there would be no fatalities\n'
              'as a result of your dangerous driving. ')
        print('Your current score is ' + str(score))
    if c2 == 'B':
        score = score - 1
        print('Not a good choice. By continuing to drive, you put yourself and other road users at risk. \n'
              'You should pull over and take a rest if you feel fatigued.')
        print('Your current score is ' + str(score))
    print('Round 3')
    print('As you are driving between Keith and Murray Bridge, \n'
          'you see multiple rest areas along the side of the road.\n'
          'It is now completely night, and it is completely dark.\n'
          'You need to get to Adelaide tonight, but you are still two hours away.\n')
    c3 = input('Do you wish to\n'
               'A: Pull over at On The Run and get a Krispy Kreme and Coffee\n'
               'B: Pull over and have a quick 10 minute rest\n'
               'C: Keep driving all night until you get to Adelaide')
    if c3 == 'A':
        score = score + 2
        print('Awesome choice! As a result of pulling over, having a coffee and something to eat,\n'
              ' you have allowed yourself to recover from your driving, and concentrate better while driving. \n'
              'You have earned double points this round.')
        print('Your current score is ' + str(score))
    elif c3 == 'B':
        score = score + 1
        print('Good choice. By pulling over and having a quick rest break, \n'
              'you have allowed yourself have a quick break, and regain your concentration.\n'
              'You have earned 1 point.')
        print('Your current score is ' + str(score))
    else:
        score = score - 1
        print('Not a good choice. By continuing to drive when you are fatigued and hungry,\n'
              ' you are not making the roads safe for anyone, including yourself. \n'
              'You were sadly the victim of a car crash and have been eliminated from the game.')
        print('Your final score is ' + str(score))
        game_menu()
        # End Game Here
    print('Round 4')
    print('You are now driving on the South Eastern Freeway between Murray Bridge and Adelaide.\n'
          'As you are driving along, you become dazed by the lights of the freeway, and the oncoming traffic.\n'
          'But you are only 30 minutes from Adelaide! So close! There are multiple rest areas outside Mount Barker,\n'
          'and there is a McDonalds in Mount Barker.')
    c4 = input('Do you wish to\n'
               'A: Pull over at one of the many rest stops outside Mount Barker\n'
               'B: Head to Maccas in Mount Barker for another coffee\n'
               'C: Keep driving because you\'re only 30 minutes from Adelaide!')
    if c4 == 'A':
        score = score + 4
        print('Great choice! By pulling over outside Mount Barker,\n'
              'you are certain to be awake and alert as you enter the Adelaide Hills.\n'
              'You wont suffer any microsleeps or alertlessness at the wheel.\n'
              'You have earned double points for this round')
    print('Your final score is ' + str(score))
    if c4 == 'B':
        score = score + 2
        print('Good choice. By heading into Maccas for a coffee or food,\n'
              'you have had a break and a chance to regain alertness.\n'
              'On the other hand, you have wasted time driving in when you could\n'
              'just take a quick 10 minute break at the rest stop for free.')
    print('Your final score is ' + str(score))
    if c4 == 'C':
        score = score - 2
        print('A fatal choice. By not regaining concentration and alertness descending into the Adelaide hills,\n'
              'you have been dozing on and off while driving.\n'
              'Sadly, your car run a red light into the Glen Osmond Road intersection,\n'
              'and was hit by traffic from Portrush Road and Cross Road.')
    print('Your final score is ' + str(score))
    game_menu()


game_menu()
