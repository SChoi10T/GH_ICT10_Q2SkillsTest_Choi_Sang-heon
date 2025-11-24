# Skills Test
from pyscript import display, document # pyright: ignore[reportMissingImports]

# School Club Information
def glee_information(e):
    document.getElementById('information').innerHTML = ""  # Clear Output

    # Student Clubs
    glee_club = document.getElementById('glee_club').value

    # Glee Club
    glee_keys = ['Name', 'Description', 'Meeting Time', 'Location', 'Club Moderator', 'Number of Members']
    glee_values = ['Glee Club', 'The singing club of OBMC.', 'Every Monday and Thursday 3:00-4:30 PM', 'HS Music Room', 'Mary Margery Loyola', 38]

    glee_club = dict(zip(glee_keys, glee_values))
    display(glee_club, target='information')

def commarts_information(e):
    document.getElementById('information').innerHTML = ""  # Clear Output

    # Student Clubs
    commarts_club = document.getElementById('commarts_club').value

     # Commarts Club
    commarts_keys = ['Name', 'Description', 'Meeting Time', 'Location', 'Club Moderator', 'Number of Members']
    commarts_values = ['Commarts Club', 'The communication and writing club of OBMC.', 'Every Tuesday and Wednesday 3:00-4:30 PM', 'HS Communication Room', 'Romand Gerard Loreto', 24]

    commarts_club = dict(zip(commarts_keys, commarts_values))
    display(commarts_club, target='information')

def dance_information(e):
    document.getElementById('information').innerHTML = ""  # Clear Output

    # Student Clubs
    dance_club = document.getElementById('dance_club').value

     # Dance Club
    dance_keys = ['Name', 'Description', 'Meeting Time', 'Location', 'Club Moderator', 'Number of Members']
    dance_values = ['Dance Club', 'The dancing club of OB.', 'Every Monday and Friday 3:00-4:30 PM', 'HS Dance Room', 'Akihiro Marutani', 28]

    dance_club = dict(zip(dance_keys, dance_values))
    display(dance_club, target='information')
