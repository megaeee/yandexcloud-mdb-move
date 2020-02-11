# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from yandex.cloud.compute.v1 import instance_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2
from yandex.cloud.compute.v1 import instance_service_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class InstanceServiceStub(object):
  """A set of methods for managing Instance resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Get',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.GetInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2.Instance.FromString,
        )
    self.List = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/List',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstancesRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstancesResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Create',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.CreateInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Update = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Update',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.UpdateInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Delete = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Delete',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.DeleteInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.UpdateMetadata = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/UpdateMetadata',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.UpdateInstanceMetadataRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.GetSerialPortOutput = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/GetSerialPortOutput',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.GetInstanceSerialPortOutputRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.GetInstanceSerialPortOutputResponse.FromString,
        )
    self.Stop = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Stop',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.StopInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Start = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Start',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.StartInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.Restart = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/Restart',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.RestartInstanceRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.AttachDisk = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/AttachDisk',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.AttachInstanceDiskRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.DetachDisk = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/DetachDisk',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.DetachInstanceDiskRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
        )
    self.ListOperations = channel.unary_unary(
        '/yandex.cloud.compute.v1.InstanceService/ListOperations',
        request_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstanceOperationsRequest.SerializeToString,
        response_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstanceOperationsResponse.FromString,
        )


class InstanceServiceServicer(object):
  """A set of methods for managing Instance resources.
  """

  def Get(self, request, context):
    """Returns the specified Instance resource.

    To get the list of available Instance resources, make a [List] request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    """Retrieves the list of Instance resources in the specified folder.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    """Creates an instance in the specified folder.
    Method starts an asynchronous operation that can be cancelled while it is in progress.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Update(self, request, context):
    """Updates the specified instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    """Deletes the specified instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateMetadata(self, request, context):
    """Updates the metadata of the specified instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSerialPortOutput(self, request, context):
    """Returns the serial port output of the specified Instance resource.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    """Stops the running instance.

    You can start the instance later using the [InstanceService.Start] method.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Start(self, request, context):
    """Starts the stopped instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Restart(self, request, context):
    """Restarts the running instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AttachDisk(self, request, context):
    """Attaches the disk to the instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DetachDisk(self, request, context):
    """Detaches the disk from the instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListOperations(self, request, context):
    """Lists operations for the specified instance.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InstanceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.GetInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__pb2.Instance.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstancesRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstancesResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.CreateInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.UpdateInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.DeleteInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'UpdateMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateMetadata,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.UpdateInstanceMetadataRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'GetSerialPortOutput': grpc.unary_unary_rpc_method_handler(
          servicer.GetSerialPortOutput,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.GetInstanceSerialPortOutputRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.GetInstanceSerialPortOutputResponse.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.StopInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.StartInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'Restart': grpc.unary_unary_rpc_method_handler(
          servicer.Restart,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.RestartInstanceRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'AttachDisk': grpc.unary_unary_rpc_method_handler(
          servicer.AttachDisk,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.AttachInstanceDiskRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'DetachDisk': grpc.unary_unary_rpc_method_handler(
          servicer.DetachDisk,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.DetachInstanceDiskRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
      ),
      'ListOperations': grpc.unary_unary_rpc_method_handler(
          servicer.ListOperations,
          request_deserializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstanceOperationsRequest.FromString,
          response_serializer=yandex_dot_cloud_dot_compute_dot_v1_dot_instance__service__pb2.ListInstanceOperationsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'yandex.cloud.compute.v1.InstanceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
