from app import app, socketio
if __name__ == '__main__':
	socketio.run(app, debug=True, host = '127.0.0.1', port = 8009)
