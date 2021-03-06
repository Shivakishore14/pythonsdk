# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import plugin_pb2 as plugin__pb2


class PluginStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetJobs = channel.unary_stream(
        '/proto.Plugin/GetJobs',
        request_serializer=plugin__pb2.Empty.SerializeToString,
        response_deserializer=plugin__pb2.Job.FromString,
        )
    self.ExecuteJob = channel.unary_unary(
        '/proto.Plugin/ExecuteJob',
        request_serializer=plugin__pb2.Job.SerializeToString,
        response_deserializer=plugin__pb2.JobResult.FromString,
        )


class PluginServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetJobs(self, request, context):
    """GetJobs returns a stream of Job objects.
    Used to expose jobs to gaia.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecuteJob(self, request, context):
    """ExecuteJob signals the plugin to execute the given job.
    Used to execute one job from a pipeline.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PluginServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetJobs': grpc.unary_stream_rpc_method_handler(
          servicer.GetJobs,
          request_deserializer=plugin__pb2.Empty.FromString,
          response_serializer=plugin__pb2.Job.SerializeToString,
      ),
      'ExecuteJob': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteJob,
          request_deserializer=plugin__pb2.Job.FromString,
          response_serializer=plugin__pb2.JobResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Plugin', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
