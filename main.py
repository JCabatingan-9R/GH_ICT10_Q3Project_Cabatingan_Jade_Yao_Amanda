from pyscript import display, document


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