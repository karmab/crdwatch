from kubernetes import client, config, watch
import os


CRD = os.environ.get("CRD")
VERSION = os.environ.get("VERSION", "v1")


if __name__ == "__main__":
    if CRD is None:
        print("Missing env variable CRD set as crd.domain")
        os._exit(1)
    info = CRD.split('.')
    if len(info) == 1:
        print("Incorrect CRD %s" % CRD)
        os._exit(1)
    CRD = info[0]
    DOMAIN = ".".join(info[1:])
    if 'KUBERNETES_PORT' in os.environ:
        config.load_incluster_config()
    else:
        config.load_kube_config()
    # configuration = client.Configuration()
    # configuration.assert_hostname = False
    # api_client = client.api_client.ApiClient(configuration=configuration)
    api_client = client.api_client.ApiClient()
    v1 = client.CoreV1Api()
    crds = client.CustomObjectsApi(api_client)
    print("Starting main loop on %s %s %s..." % (CRD, DOMAIN, VERSION))
    resource_version = ''
    while True:
        print(DOMAIN, VERSION, CRD)
        stream = watch.Watch().stream(crds.list_cluster_custom_object, DOMAIN, VERSION, CRD,
                                      resource_version=resource_version)
        for event in stream:
            obj = event["object"]
            name = obj['metadata']['name']
            _type = event["type"]
            print("%s on %s" % (_type, name))
