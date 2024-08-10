import logging
from concurrent import futures

import grpc
from gen import server_pb2, server_pb2_grpc


class Server(server_pb2_grpc.ServerServicer):
    def GetServerInfo(self, request, context):
        response = server_pb2.ServerInfoResponse()
        response.server_name = "ml_examples"
        response.server_version = "0.1.0"
        response.server_status = "running"
        response.server_start_time = "2021-10-01T00:00:00Z"
        response.server_uptime = "1 day"
        return response


def serve():
    port = "9099"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
