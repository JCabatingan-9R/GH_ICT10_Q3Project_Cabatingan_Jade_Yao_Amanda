from pyscript import display, document


def check(e):
    document.getElementById('output').innerHTML = '' # clear output

    # get username and password values with their id
    user = document.getElementById('user').value
    pw = document.getElementById('pw').value

    # turn variables into lists and get the number of characters using list() and len()
    lu = list(user)
    lp = list(pw)

    username = len(lu)
    password = len(lp)

    # finding out if characters are all letters or all numbers for future conditional statements
    pwlist = [pw.isdigit(), pw.isalpha()]

    # conditional statements
    if username >= 7: # username must contain 7 characters or more
        if password >= 10: # password must contain 10 characters or more
            if pw.isdigit() == True: # if all characters are digits
                display(f'There must be at least one letter in your password.', target="output")
            
            elif  pw.isalpha() == True: # if all characters are letters
                display(f'There must be at least one number in your password.', target="output")
            
            elif any(pwlist) == False: # if there are no True values in pwlist, meaning the password ins't all letters nor all numbers
                display(f'Congratulations! You have successfully signed up!', target="output")
        else:
            display(f'Your password must contain 10 characters.', target="output")
    else: 
        display(f'Your username must contain at least 7 characters.', target="output")


def sign(e):
    document.getElementById('output').innerHTML = '' #clear output
    #get values from html
    registration = document.querySelector('input[name="reg"]:checked').value
    medcert = document.querySelector('input[name="clearance"]:checked').value
    grade = document.getElementById('grade').value
    sect = document.getElementById('sect').value

    #conditional statements
    if registration == 'no' or medcert == 'no': # for incomplete requirememnts
        display(f'Please make sure to register online and obtain medical clearance before signing up.', target='output')

    elif grade == '11' or grade =='12': # for wrong grade level
        display(f'Oh no! You are in senior high...this is only for grades 7--10.', target='output')

    elif registration == 'yes' and medcert == 'yes': # eligible
        if sect == 'Ruby':
            display(f'Congratulations! You are part of the Blue Bears!', target='output') #congratulatory message and team
            document.getElementById("image").innerHTML="<img src='blue_bears.jpg' height='300' width='350'>" #display image
        elif sect == 'Sapphire':
            display(f'Congratulations! You are part of the Green Hornets!', target='output')
            document.getElementById("image").innerHTML="<img src='green_hornets.jpg' height='300' width='350'>"
        elif sect == 'Emerald':
            display(f'Congratulations! You are part of the Red Bulldogs!', target='output')
            document.getElementById("image").innerHTML="<img src='red_bulldogs.jpg' height='300' width='350'>"
        elif sect == 'Topaz':
            display(f'Congratulations! You are part of the Yellow Tigers!', target='output')
            document.getElementById("image").innerHTML="<img src='yellow_tigers.jpg' height='300' width='350'>"


def players(e):
    document.getElementById("players").innerHTML = ""

    teams = {
        "Blue Bears": ["sectuin1", "section3", "section3"],
        "Green Hornets": ["sectuin1", "section3", "section3"],
        "Red Bulldogs": ["sectuin1", "section3", "section3"],
        "Yellow Tigers": ["sectuin1", "section3", "section3"]
    }


    for team in teams.items():
        display(f"<h3>{team}</h3>", target="output")
