import AnalyzerRpc_pb2 as pb2
import AnalyzerRpc_pb2_grpc as pb2_grpc
import grpc
from concurrent import futures

import logging

class Greeter(pb2_grpc.AnalyzerServicer):
    
    def Analyze(self, request, context):
        print (request)
        
        
        resultPayload = len(request.payload.split(" "))
        return pb2.Response(result=resultPayload)
    
    
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    pb2_grpc.add_AnalyzerServicer_to_server(Greeter(), server)
    
    server.add_insecure_port('[::]:7034')
    server.start()
    server.wait_for_termination()
    
    
if __name__ == '__main__':
    logging.basicConfig()
    serve()
