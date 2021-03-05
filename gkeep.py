import gkeepapi


def login(keep, email, passw):
    """
    Log in to Google Keep
    :param email: email string for login
    :param passw: password string for login
    :return: void
    """
    keep.login(email, passw)

def get_note(keep, title):
    """
    Get note with given title
    :param keep: google keep object
    :param title: title of note
    :return: keep note
    """
    return next(keep.find(query=title))

def save_notes(keep):
    """
    Save note to Google keep
    :param keep: google keep object
    :return: void
    """
    keep.sync()

def gkeep_main():
    """
    Run quivr code
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
