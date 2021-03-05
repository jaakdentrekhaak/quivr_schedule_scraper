import gkeepapi


def login(keep, email, passw):
    """Log in to Google Keep

    Args:
        keep (object): Google Keep object
        email (str): email for login
        passw (str): password for login
    """
    keep.login(email, passw)

def get_note(keep, title):
    """Get note with given title

    Args:
        keep (object): google keep object
        title (str): title of note

    Returns:
        object: google keep note object
    """
    return next(keep.find(query=title))

def save_notes(keep):
    """Save note to Google Keep

    Args:
        keep (object): Google keep object
    """
    keep.sync()

def gkeep_main(data):
    """Run gkeep code

    Args:
        data (list): contains items to put in notes list
    """

    keep = gkeepapi.Keep()

    # Login
    email = input('Enter email: ')
    passw = input('Enter password: ')
    login(keep, email, passw)

    # Get note
    title = input('Enter title of note: ')
    note = get_note(keep, title)

    # Test
    print(note.text)

    # # Edit note
    # data = ...
    # edit_note(keep, note, data)

    # # Save notes to server
    # save_notes(keep)
