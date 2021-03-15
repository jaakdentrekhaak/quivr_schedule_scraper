from getpass import getpass
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

def write_note(note, data):
    for el in data:
        note.add(el, False, gkeepapi.node.NewListItemPlacementValue.Bottom)

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
    email = input('Google email: ')
    passw = getpass('Google password: ')
    login(keep, email, passw)

    # Get note
    title = input('Title of Google Keep note: ')
    note = get_note(keep, title)

    # Edit note
    write_note(note, data)

    print('[Google Keep] New list: \n', note.text)

    # Save notes to server
    save_notes(keep)
