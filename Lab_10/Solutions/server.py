from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSBase, SAFRSAPI, jsonapi_rpc


db = SQLAlchemy()


class Message(SAFRSBase, db.Model):
    """
    description: This is Message
    """

    __tablename__ = "Messages"
    id = db.Column(db.Integer, primary_key=True)
    receiver = db.Column(db.String)
    sender = db.Column(db.String)
    content = db.Column(db.String)

    @classmethod
    @jsonapi_rpc(http_methods=["GET"])
    def get_messages_addressed_to(cls, **kwargs):
        """
        description: Get message
        args:
            receiver_name: receiver name
        """
        print(kwargs)
        messages = {'id': [], 'rec': [], 'sen': [], 'cont': []}
        # messages = {} #{'sender1': [mess11, mess12,..], 'sender2': [mess21, mess22, ...], ...}
        rec_name = kwargs['receiver_name']
        messages_to_receiver = db.session.query(Message).filter_by(receiver=rec_name).all()

        for mess in messages_to_receiver:
            messages['id'].append(mess.id)
            messages['rec'].append(mess.receiver)
            messages['sen'].append(mess.sender)
            messages['cont'].append(mess.content)

        return {'result': messages}


class User(SAFRSBase, db.Model):
    """
        description: User definition
    """

    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    password = db.Column(db.String)

    @classmethod
    @jsonapi_rpc(http_methods=['POST'])
    def send_message(cls, **kwargs):
        """
            description: Send message
            args:
                sender: "Piotrek"
                receiver: "Piotrek2"
                msg_content: "hello Piotrek2!"
        """
        msg = Message(receiver=kwargs.get('receiver'), sender=kwargs.get('sender'), content=kwargs.get('msg_content'))

        db.session.add(msg)
        db.session.commit()

        return {'result': 'success'}

    @classmethod
    @jsonapi_rpc(http_methods=['POST'])
    def login_or_register_user(cls, user_name, user_password):
        """
            description: Register or login user
            args:
                user_name: "Piotrek"
                user_password: "haslo123"
        """
        user = db.session.query(User).filter_by(name=user_name).first()
        if user is None:
            user = User(name=user_name, password=user_password)
            db.session.add(user)
            db.session.commit()
            return {'result': 'registered'}

        elif user.password == user_password:
            return {'result': 'logged_in'}

        else:
            return {'result': 'bad_credentials'}


def create_api(app, HOST="localhost", PORT=5000, API_PREFIX=""):
    api = SAFRSAPI(app, host=HOST, port=PORT, prefix=API_PREFIX)
    api.expose_object(Message)

    api.expose_object(User)
    print("Starting API: http://{}:{}/{}".format(HOST, PORT, API_PREFIX))


def create_app(config_filename=None, host="localhost"):
    app = Flask("demo_app")
    app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///:memory:')
    app.config.update(SQLALCHEMY_TRACK_MODIFICATIONS=False)
    db.init_app(app)
    SAFRSBase.db_commit = False
    with app.app_context():
        db.create_all()
        create_api(app, host)
    return app


host_name = 'localhost'
server_app = create_app(host=host_name)


def main():
    server_app.run(host=host_name, threaded=False)


if __name__ == "__main__":
    main()


