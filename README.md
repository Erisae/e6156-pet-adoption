# e6156-pet-adoption
pet adoption microservice

### Dockerization
```shell
# build
docker build -t yuhanxia99/pet-adoption .
# launch container using image
docker run -p 8011:8011 yuhanxia99/pet-adoption
# push
docker push yuhanxia99/pet-adoption
```
### Create Amazon EKS cluster and nodes
```shell
# managed node linux, not fargate
eksctl create cluster --name pet-adoption --region us-east-2
# view kubernetes resources
kubectl get nodes -o wide
# view workloads running on cluster
kubectl get pods -A -o wide
```
### Deploy on EKS
```shell
# 
# create and delete namespace
kubectl delete namespace eks-pet-adoption
kubectl create namespace eks-pet-adoption
# apply yaml
kubectl apply -f eks-pet-adoption-deployment.yaml
kubectl apply -f eks-pet-adoption-service.yaml
# view all resources in namespace
kubectl get all -n eks-pet-adoption
# view details of deployed service
kubectl -n eks-pet-adoption describe service eks-pet-adoption-linux-service
```