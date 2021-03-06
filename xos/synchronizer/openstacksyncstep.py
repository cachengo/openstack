
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


from synchronizers.new_base.syncstep import SyncStep

class OpenStackSyncStep(SyncStep):
    """ XOS Sync step for copying data to OpenStack
    """

    def __init__(self, *args, **kwargs):
        SyncStep.__init__(self, *args, **kwargs)

    # TODO(smbaker): This should be explained.
    def __call__(self, **args):
        return self.call(**args)
