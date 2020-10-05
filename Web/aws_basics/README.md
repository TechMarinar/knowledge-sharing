# AWS

* Create new IAM user
* Configure AWS CLI

    * $ **vim ~/.aws/credentials**

            [default]
            aws_access_key_id = <ACCESS_KEY>
            aws_secret_access_key = <SECRET_KEY>

    * $ **vim ~/.aws/config** 

            [default]
            region=ap-south-1
            output=json

    * $ **aws iam get-user**

            {
                "User": {
                    "Arn": "arn:aws:iam::62NNNNNNNN21:user/username",
                    "UserName": "username",
                    "Path": "/",
                    "UserId": "USERID",
                    "CreateDate": "2020-10-05T11:06:55Z"
                }
            }

* Test Terraform Setup 

    * $ **vim terraform.tfvars**

            AWS_ACCESS_KEY="<ACCESS_KEY>"
            AWS_SECRET_KEY="<SECRET_KEY>"

    * $ **vim terraform.code.tf**

            # ************************
            # vars.tf
            # ************************

            variable "AWS_ACCESS_KEY" {}
            variable "AWS_SECRET_KEY" {}
            variable "AWS_REGION" {
            default = "ap-south-1"
            }
            variable "AMIS" {
            type = "map"
            default = {
                ap-south-1 = "ami-03cfb5e1fb4fac428"
            }
            }
            
            # ************************
            # provider.tf
            # ************************
            provider "aws" {
                access_key = "${var.AWS_ACCESS_KEY}"
                secret_key = "${var.AWS_SECRET_KEY}"
                region = "${var.AWS_REGION}"
            }
            
            # ************************
            # instance.tf
            # ************************
            resource "aws_instance" "null_DEVOPS_INSTANCE" {
            ami = "${lookup(var.AMIS, var.AWS_REGION)}"
            tags = { Name = "UDEMY" }
            instance_type = "t2.micro"
            provisioner "local-exec" {
                command = "echo ${aws_instance.null_DEVOPS_INSTANCE.private_ip} >> private_ips.txt"
            }
            }
            output "ip" {
                value = "${aws_instance.null_DEVOPS_INSTANCE.public_ip}"
            }

    * $ **terraform init**
    * $ **terraform apply**
    * $ **terraform destroy**

* Create an S3 bucket: `kops.null.co.in`
* Create a hosted zone: `kops.nullbangalore.site`
* Find full zone name for your region: `aws ec2 describe-availability-zones --region ap-south-1   `

* Setup a Kubernetes cluster using Terraform

    * $ **vim kops_cluster.sh**

            kops create cluster \
            --name=kops.nullbangalore.site \
            --state=s3://kops.null.co.in \
            --authorization RBAC \
            --zones=ap-south-1a \
            --node-count=2 \
            --node-size=t2.micro \
            --master-size=t2.micro \
            --master-count=1 \
            --dns-zone=kops.nullbangalore.site \
            --out=null_terraform \
            --target=terraform \
            --ssh-public-key=~/.ssh/null_terraform.pub

  * Troubleshooting: *"Terraform has initialized, but configuration upgrades may be needed."* 
    
        terraform 0.12upgrade
        terraform init
        terraform apply

    **Outputs:**

        cluster_name = kops.nullbangalore.site
        master_autoscaling_group_ids = [
        "master-ap-south-1a.masters.kops.nullbangalore.site",
        ]
        master_security_group_ids = [
        "sg-0701055adb32e03c2",
        ]
        masters_role_arn = arn:aws:iam::625077889421:role/masters.kops.nullbangalore.site
        masters_role_name = masters.kops.nullbangalore.site
        node_autoscaling_group_ids = [
        "nodes.kops.nullbangalore.site",
        ]
        node_security_group_ids = [
        "sg-072f49ef57ae19941",
        ]
        node_subnet_ids = [
        "subnet-07caa79d4303b009b",
        ]
        nodes_role_arn = arn:aws:iam::625077889421:role/nodes.kops.nullbangalore.site
        nodes_role_name = nodes.kops.nullbangalore.site
        region = ap-south-1
        route_table_public_id = rtb-08dcf341209c578f9
        subnet_ap-south-1a_id = subnet-07caa79d4303b009b
        vpc_cidr_block = 172.20.0.0/16
        vpc_id = vpc-0624da09a3c8a3ab1

  * $ **kubectl get nodes**

        NAME                                           STATUS   ROLES    AGE   VERSION
        ip-172-20-41-144.ap-south-1.compute.internal   Ready    node     10m   v1.17.12
        ip-172-20-43-234.ap-south-1.compute.internal   Ready    master   13m   v1.17.12
        ip-172-20-63-134.ap-south-1.compute.internal   Ready    node     10m   v1.17.12

* Deploy Nginx in Kubernetes cluster AWS
  
        kubectl \
            create deployment my-nginx-deployment \
            --image=nginx
    
    ---

        kubectl \
            expose deployment my-nginx-deployment \
            --port=80 \
            --type=NodePort \
            --name=my-nginx-service

    ---

        $ kubectl get nodes
        $ kubectl get pods,svc

* Update `Inbound rules` for `Security group for nodes` to expose the Nginx port
* Create a **configmap** object in Kubernetes, to store NGINX content

        $ kubectl create configmap nginx-content --from-file=index.html
        $ kubectl get cm nginx-content
        $ kubectl describe cm
        
* Deploy `deployment` and `service` with `Nginx`

        $ kubectl create -f deployment_file.yaml 
        $ kubectl delete cm nginx-content
        $ kubectl get pod
        $ kubectl exec -it nginx-deployment-5db549b6df-4xplk -- bash
        $ vim deployment_file.yaml 
        $ kubectl apply -f deployment_file.yaml
        $ kubectl delete pod nginx-deployment-5db549b6df-4xplk

* Cleanup
  * **kubectl delete all --all**
  * kubectl get svc --all-namespaces
  * kubectl get nodes
  * kubectl delete node --all
  * $ terraform state list
  * $ terraform destroy

