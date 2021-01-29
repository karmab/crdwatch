simple crd watcher

## Running

### dev mode

You will need python3 and [kubernetes client python](https://github.com/kubernetes-client/python) that you can either install with pip or your favorite package manager. Then, provided you have set your KUBECONFIG environment variable, just run:

```
export CRD=guitars.kool.karmalabs.local
export VERSION=v1
python3 crdwatch.py
```

### standalone mode

You can run against an existing cluster after setting your KUBECONFIG env variable with the following invocation

```
export CRD=guitars.kool.karmalabs.local
IMAGE="karmab/crdwatch"
podman run -v $(dirname $KUBECONFIG):/kubeconfig -e CRD:$CRD -e VERSION:$VERSION -e KUBECONFIG=/kubeconfig/kubeconfig --rm -it karmab/crdwatch
```
