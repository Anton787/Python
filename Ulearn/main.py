import socket
import pandas as pd
import json

def handle_request(request, df):
    command = request.get("command")
    operation = request.get("operation")
    name = request.get("name")

    df['NormalizedName'] = df['Name'].str.strip().str.lower()
    org_info = df[df['NormalizedName'] == name.strip().lower()]
    if command == 'get_data':
        match operation:
            case "get_website":
                return {"result": org_info.iloc[0]['Website']}
            case "get_country":
                return {"result": org_info.iloc[0]['Country']}
            case "get_number_of_employees":
                return {"result": int(org_info.iloc[0]['Number of employees'])}
            case "get_description":
                return {"result": org_info.iloc[0]['Description']}

def start_server():
    df = pd.read_csv('organizations.csv')

    host = "127.0.0.32"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(10)

    try:
        client_socket, address = server_socket.accept()

        with client_socket:
            while True:
                try:
                    data = client_socket.recv(1024).decode()

                    if not data:
                        response = {"error": "No data received"}
                        client_socket.sendall(json.dumps(response).encode())
                        break

                    request = json.loads(data)

                except json.JSONDecodeError:
                    response = {"error": "Invalid JSON format"}
                    client_socket.sendall(json.dumps(response).encode())
                    break
                except Exception:
                    response = {"error": "Unexpected error"}
                    client_socket.sendall(json.dumps(response).encode())
                    break

                response = handle_request(request, df)
                client_socket.sendall(json.dumps(response).encode())

    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()