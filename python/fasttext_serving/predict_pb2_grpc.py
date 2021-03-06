# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import predict_pb2 as predict__pb2


class FasttextServingStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.predict = channel.stream_unary(
        '/fasttext_serving.FasttextServing/predict',
        request_serializer=predict__pb2.PredictRequest.SerializeToString,
        response_deserializer=predict__pb2.PredictResponse.FromString,
        )


class FasttextServingServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def predict(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FasttextServingServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'predict': grpc.stream_unary_rpc_method_handler(
          servicer.predict,
          request_deserializer=predict__pb2.PredictRequest.FromString,
          response_serializer=predict__pb2.PredictResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'fasttext_serving.FasttextServing', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
