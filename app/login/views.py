from . import login


@login.route('/login', methods=['GET'])
def login():
    return 'Done'
