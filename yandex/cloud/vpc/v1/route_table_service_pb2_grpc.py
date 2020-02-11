# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.vpc.v1 import route_table_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__pb2
from yandex.cloud.vpc.v1 import route_table_service_pb2 as yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2


class RouteTableServiceStub(object):
  """A set of methods for managing RouteTable resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/Get',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.GetRouteTableRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__pb2.RouteTable.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/List',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTablesRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTablesResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/Create',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.CreateRouteTableRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/Update',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.UpdateRouteTableRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/Delete',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.DeleteRouteTableRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTableOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTableOperationsResponse.FromString,
        )
    self.Move = channel.unary_unary(
        '/yandex.cloud.vpc.v1.RouteTableService/Move',
        request_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.MoveRouteTableRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )


class RouteTableServiceServicer(object):
  """A set of methods for managing RouteTable resources.
  """

  def Get(self, request, context):
    """Returns the specified RouteTable resource.

    To get the list of available RouteTable resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of RouteTable resources in the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates a route table in the specified folder and network.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified route table.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified route table.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """List operations for the specified route table.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Move(self, request, context):
    """Move route table to another folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RouteTableServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.GetRouteTableRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__pb2.RouteTable.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTablesRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTablesResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.CreateRouteTableRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.UpdateRouteTableRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.DeleteRouteTableRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTableOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.ListRouteTableOperationsResponse.SerializeToString,
      ),
      'Move': grpc.unary_unary_rpc_method_handler(
          servicer.Move,
          request_deserializer=yandex_dot_cloud_dot_vpc_dot_v1_dot_route__table__service__pb2.MoveRouteTableRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.vpc.v1.RouteTableService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
