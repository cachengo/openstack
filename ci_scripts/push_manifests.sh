export IMAGE_TAG=$(cat VERSION)

docker manifest create --amend cachengo/openstack-synchronizer:$IMAGE_TAG cachengo/openstack-synchronizer-x86_64:$IMAGE_TAG cachengo/openstack-synchronizer-aarch64:$IMAGE_TAG

docker manifest push cachengo/openstack-synchronizer:$IMAGE_TAG