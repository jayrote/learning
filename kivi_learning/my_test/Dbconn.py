class DbConn:
    myConnection = None
    myCursor = None

    def __init__(self):

        import conn

        self.myConnection = conn.connect()

        self.myCursor = self.myConnection.cursor(dictionary=True)
