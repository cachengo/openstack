
# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from synchronizers.new_base.modelaccessor import OpenStackService
from newopenstacksyncstep import NewOpenStackSyncStep

class SyncOpenStackService(NewOpenStackSyncStep):
    provides=[OpenStackService]
    requested_interval=0
    observes=OpenStackService

    def sync_record(self, service):
        # nothing to do
        pass

    def delete_record(self, service):
        # nothing to do
        pass

